from typing import List
from argparse import ArgumentParser, Namespace
from datetime import timedelta
from functools import partial
import os

import torch
import torch.distributed as dist

from core.const import M_TO_NM, FT_TO_NM, OUT_FEATURES, OUT_SHIFT_FEATURES
from core.utils import (
    Timer,
    create_logger,
    get_gpu_status,
    set_torch_seeds,
    mkdir,
    dump_json,
    load_pkl,
)
from core.config import SampleConfig, PackConfig, Config
from core.norm import MinMaxNorm, MeanStdNorm
from core.dataset import PackedDictDictDataset
from core.factory import make_ddp_dataloader, make_pipeline, make_dataset
from common.workhouse import save_ckpt_workhouse


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--packed-folder", required=True)
    parser.add_argument("--save-folder", required=True)

    parser.add_argument("--device")
    parser.add_argument("--seed", type=int, required=True)

    parser.add_argument("--num-epochs", type=int, required=True)
    parser.add_argument("--inf-per-num-epochs", type=int, required=True)
    parser.add_argument("--save-ckpt-per-num-epochs", type=int, required=True)

    parser.add_argument("--batch-size", type=int, required=True)
    parser.add_argument("--inf-batch-size", type=int, required=True)

    parser.add_argument("--out-mode", required=True)

    parser.add_argument("--diffuser", required=True)
    parser.add_argument("--model-key-nargs", nargs='+', required=True)
    parser.add_argument("--opt-key-nargs", nargs='+', required=True)

    parser.add_argument('--cold-inf', action="store_true")

    args = parser.parse_args()
    return args


# --- #


def ddp_setup():
    assert torch.cuda.is_available()
    dist.init_process_group('nccl', timeout=timedelta(hours=1))
    return


def ddp_cleanup():
    dist.destroy_process_group()
    return


def sync_value(
    v: List[torch.Tensor],
    op=dist.ReduceOp.SUM,
    dtype: torch.dtype = None,
    device: torch.device = None,
):
    l = len(v)
    for i in range(l):
        if not isinstance(v[i], torch.Tensor):
            _v = torch.tensor(v[i], dtype=dtype, device=device)
        else:
            _v = v[i]
            # _v = v[i].clone().detach()
        dist.all_reduce(_v, op=op)
        v[i] = _v
    return v


# --- #


def l_to_str(_list: List):
    l_str = ""
    for _l in _list:
        l_str += f" {_l:.5f}"
    return l_str


def main(cfg: Config):
    # TODO flow matching
    # TODO compute the pred. ori. while training also compute the pred error

    # TODO intention fixed point (fine-grained intention)
    # TODO confidence score model use brain's output only
    # TODO sep. loss fn. (do norm first) (also use as classifier-free guidance)

    p_folder = cfg.packed_folder
    _record_folder = f"{cfg.save_folder}/record"
    _ckpt_folder = f"{cfg.save_folder}/ckpt"

    s_cfg: SampleConfig = load_pkl(f"{p_folder}/#s_cfg.pkl")
    p_cfg: PackConfig = load_pkl(f"{p_folder}/#p_cfg.pkl")

    mmn: MinMaxNorm = load_pkl(f"{p_folder}/mmn.pkl")
    msn: MeanStdNorm = load_pkl(f"{p_folder}/msn.pkl")

    timer = Timer()

    is_shift = cfg.out_mode == 'shift'

    #

    ddp_setup()
    set_torch_seeds(cfg.seed)

    rank = dist.get_rank()
    world_size = dist.get_world_size()
    local_rank = int(os.environ.get(
        'LOCAL_RANK',
        rank % torch.cuda.device_count(),
    ))
    device = torch.device('cuda', local_rank)
    torch.cuda.set_device(device)

    is_master = rank == 0
    if is_master:
        assert cfg.batch_size % world_size == 0
        assert cfg.inf_batch_size % world_size == 0
        assert cfg.num_epochs % cfg.inf_per_num_epochs == 0

        mkdir(cfg.save_folder)
        mkdir(_record_folder, can_exists=True)
        mkdir(_ckpt_folder, can_exists=True)

    logger = create_logger(cfg.save_folder, is_master=is_master)
    logger.info(f"{vars(cfg) = }")
    logger.info(f"{vars(s_cfg) = }")
    logger.info(f"{vars(p_cfg) = }")
    logger.info(f"{mmn.norm = }")
    logger.info(f"{msn.norm = }")
    logger.info(get_gpu_status())

    _batch_size = int(cfg.batch_size // world_size)
    _i_batch_size = int(cfg.inf_batch_size // world_size)

    logger.info(f"{world_size = } {_batch_size = } {_i_batch_size = }")

    dist.barrier()

    #

    pipeline = make_pipeline(
        s_cfg,
        cfg,
        device,
        logger=logger,
        use_ddp=True,
    )

    # --- hard-coded --- #
    # see OUT_FEATURES, OUT_SHIFT_FEATURES
    out_features = OUT_FEATURES
    if is_shift:
        out_features = OUT_SHIFT_FEATURES
    undo_norm_hldr = partial(mmn.undo_norm_workhouse, features=out_features)
    scale = torch.tensor([M_TO_NM, M_TO_NM, FT_TO_NM])
    # --- hard-coded --- #

    dist.barrier()

    #

    _train_ds = load_pkl(f"{p_folder}/train_ds.pkl")
    _val_ds = load_pkl(f"{p_folder}/val_ds.pkl")

    _train_ds = make_dataset(s_cfg.mode, cfg.out_mode, _train_ds)
    _val_ds = make_dataset(s_cfg.mode, cfg.out_mode, _val_ds)

    train_ds = PackedDictDictDataset(_train_ds)
    val_ds = PackedDictDictDataset(_val_ds)
    logger.info(f"{len(train_ds) = } {len(val_ds) = }")
    del _train_ds
    del _val_ds

    _args = (world_size, rank, cfg.seed, _batch_size)
    train_sampler, train_dl = make_ddp_dataloader(train_ds, *_args)
    val_sampler, val_dl = make_ddp_dataloader(val_ds, *_args)
    logger.info(f"{len(train_dl) = } {len(val_dl) = }")

    _args = (world_size, rank, cfg.seed, _i_batch_size)
    inf_train_sampler, inf_train_dl = make_ddp_dataloader(train_ds, *_args)
    inf_val_sampler, inf_val_dl = make_ddp_dataloader(val_ds, *_args)
    logger.info(f"{len(inf_train_dl) = } {len(inf_val_dl) = }")

    dist.barrier()

    #

    _kwargs = dict(dtype=torch.float32, device=device)

    tl_list, vl_list, time_list = [], [], []
    itl_list, ivl_list, time_list_recon = [], [], []
    if is_master:
        num_recon = (cfg.num_epochs // cfg.inf_per_num_epochs) + 1
        tl_list = [0] * cfg.num_epochs
        vl_list = [0] * cfg.num_epochs
        time_list = [0] * cfg.num_epochs
        itl_list = [0] * num_recon
        ivl_list = [0] * num_recon
        time_list_recon = [0] * num_recon

    if cfg.cold_inf:
        logger.info(get_gpu_status())

        timer.start()
        torch.cuda.synchronize()
        _, itl = pipeline.inference(
            inf_train_dl,
            use_pbar=is_master,
            undo_norm_hldr=undo_norm_hldr,
            scale=scale,
        )
        _, ivl = pipeline.inference(
            inf_val_dl,
            use_pbar=is_master,
            undo_norm_hldr=undo_norm_hldr,
            scale=scale,
        )
        torch.cuda.synchronize()
        timer.end()
        _t2 = timer.get_time_spend()

        itl = sync_value(itl, **_kwargs)
        ivl = sync_value(ivl, **_kwargs)

        itl = [l.item() for l in itl]
        ivl = [l.item() for l in ivl]

        _str = f"round: {0:06d}/{cfg.num_epochs:06d}; "
        _str += f"itl:{l_to_str(itl)}, ivl:{l_to_str(ivl)}, t2: {_t2:.5f}. "
        logger.info(_str)

        if is_master:
            itl_list[0] = itl
            ivl_list[0] = ivl
            time_list_recon[0] = _t2

    for i in range(cfg.num_epochs):
        if i == 0 or i == 1 or i == cfg.inf_per_num_epochs:
            logger.info(get_gpu_status())

        train_sampler.set_epoch(i)
        val_sampler.set_epoch(i)

        inf_train_sampler.set_epoch(i)
        inf_val_sampler.set_epoch(i)

        #

        ii = i + 1
        _str = f"round: {ii:06d}/{cfg.num_epochs:06d}; "

        timer.start()
        torch.cuda.synchronize()
        tl, vl = pipeline.train(train_dl, val_dl, use_pbar=is_master)
        torch.cuda.synchronize()
        timer.end()
        _t1 = timer.get_time_spend()

        tl = sync_value(tl, **_kwargs)
        vl = sync_value(vl, **_kwargs)

        tl = [l.item() for l in tl]
        vl = [l.item() for l in vl]

        _str += f"tl:{l_to_str(tl)}, vl:{l_to_str(vl)}, t1: {_t1:.5f}; "

        if is_master:
            tl_list[i] = tl
            vl_list[i] = vl
            time_list[i] = _t1

        if ii % cfg.inf_per_num_epochs == 0:
            _ii = ii // cfg.inf_per_num_epochs

            timer.start()
            torch.cuda.synchronize()
            _, itl = pipeline.inference(
                inf_train_dl,
                use_pbar=is_master,
                undo_norm_hldr=undo_norm_hldr,
                scale=scale,
            )
            _, ivl = pipeline.inference(
                inf_val_dl,
                use_pbar=is_master,
                undo_norm_hldr=undo_norm_hldr,
                scale=scale,
            )
            torch.cuda.synchronize()
            timer.end()
            _t2 = timer.get_time_spend()

            itl = sync_value(itl, **_kwargs)
            ivl = sync_value(ivl, **_kwargs)

            itl = [l.item() for l in itl]
            ivl = [l.item() for l in ivl]

            _str += f"itl:{l_to_str(itl)}, ivl:{l_to_str(ivl)}, t2: {_t2:.5f}. "

            if is_master:
                itl_list[_ii] = itl
                ivl_list[_ii] = ivl
                time_list_recon[_ii] = _t2

        if is_master:
            logger.info(_str)

            dump_json(tl_list, f"{_record_folder}/train_ds-loss.json")
            dump_json(vl_list, f"{_record_folder}/val_ds-loss.json")
            dump_json(itl_list, f"{_record_folder}/train_ds-recon_error.json")
            dump_json(ivl_list, f"{_record_folder}/val_ds-recon_error.json")
            dump_json(time_list, f"{_record_folder}/time-training.json")
            dump_json(time_list_recon, f"{_record_folder}/time-recon.json")

            if ii % cfg.save_ckpt_per_num_epochs == 0:
                ckpt = {
                    "sample_config": s_cfg,
                    "pack_config": p_cfg,
                    "config": cfg,
                    "min_max_norm": mmn,
                    "mean_std_norm": msn,
                    "model": pipeline.model_handler.state_dict(),
                    "optimizer": pipeline.optimizer.state_dict(),
                }
                save_ckpt_workhouse(ckpt, f"{_ckpt_folder}/{ii:06d}.pt")

        dist.barrier()
        # input()

    #

    logger.info(get_gpu_status())
    logger.info("DONE")
    ddp_cleanup()
    return


"""
usage: train.py [-h] --packed-folder PACKED_FOLDER --save-folder SAVE_FOLDER [--device DEVICE] --seed SEED --num-epochs NUM_EPOCHS --inf-per-num-epochs INF_PER_NUM_EPOCHS --batch-size BATCH_SIZE --inf-batch-size INF_BATCH_SIZE --out-mode OUT_MODE --diffuser DIFFUSER
                --model-key-nargs MODEL_KEY_NARGS [MODEL_KEY_NARGS ...] --opt-key-nargs OPT_KEY_NARGS [OPT_KEY_NARGS ...] [--cold-inf]

options:
  -h, --help            show this help message and exit
  --packed-folder PACKED_FOLDER
  --save-folder SAVE_FOLDER
  --device DEVICE
  --seed SEED
  --num-epochs NUM_EPOCHS
  --inf-per-num-epochs INF_PER_NUM_EPOCHS
  --batch-size BATCH_SIZE
  --inf-batch-size INF_BATCH_SIZE
  --out-mode OUT_MODE
  --diffuser DIFFUSER
  --model-key-nargs MODEL_KEY_NARGS [MODEL_KEY_NARGS ...]
  --opt-key-nargs OPT_KEY_NARGS [OPT_KEY_NARGS ...]
  --cold-inf
"""
if __name__ == '__main__':
    args = get_args()
    cfg = Config(args)
    main(cfg)
