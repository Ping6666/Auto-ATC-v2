from typing import Dict, List
from argparse import ArgumentParser, Namespace
from pathlib import Path
import logging

from tqdm import tqdm
import numpy as np

from core.const import IN_FEATURES, OUT_FEATURES, OUT_SHIFT_FEATURES
from core.utils import (
    create_logger,
    get_gpu_status,
    set_torch_seeds,
    mkdir,
    load_pkl,
    dump_npy,
    get_dict_len,
    make_dict_split,
)
from core.config import SampleConfig, InferenceConfig
from core.dataset import PackedDictDictDataset
from core.dataset.utils import pack, unpack
from core.factory import make_dataloader, make_dataset
from common.workhouse import load_ckpt_workhouse

T1 = Dict[str, np.ndarray]
T2 = Dict[str, Dict[str, np.ndarray]]


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--ckpt-folder", required=True)
    parser.add_argument("--packed-folder", required=True)
    parser.add_argument("--save-folder", required=True)

    parser.add_argument("--device")
    parser.add_argument("--seed", type=int, required=True)

    parser.add_argument("--batch-size", type=int, required=True)
    parser.add_argument("--inf-len", type=int, required=True)
    parser.add_argument("--num-pred", type=int, required=True)

    parser.add_argument("--ckpt-idx-nargs", nargs='+', required=True)

    args = parser.parse_args()
    return args


# --- #


def loader(
    ckpt_folder: str,
    packed_folder: str,
    ckpt_idx_list: List[int],
    inf_len: int,
    device,
    logger: logging.Logger,
):
    args_list = [
        # {
        #     'save_folder': "/val/",
        #     'ds_fname': "/val_ds.pkl",
        # },
        {
            'save_folder': "/test/",
            'ds_fname': "/test_ds.pkl",
        },
        # {
        #     'save_folder': "/train/",
        #     'ds_fname': "/train_ds.pkl",
        # },
    ]

    #

    ckpt_fname = None
    for ckpt_idx in ckpt_idx_list:
        _ckpt_fname = f"{ckpt_folder}/ckpt/{ckpt_idx}.pt"

        if not Path(_ckpt_fname).exists():
            continue

        ckpt_fname = _ckpt_fname
        break
    assert ckpt_fname is not None

    #

    s_cfg, p_cfg, cfg, mmn, _, _ = load_ckpt_workhouse(ckpt_fname, device)
    logger.info("load_ckpt_workhouse")
    logger.info(f"{vars(s_cfg) = }")
    logger.info(f"{vars(p_cfg) = }")
    logger.info(f"{vars(cfg) = }")

    _s_cfg: SampleConfig = load_pkl(f"{packed_folder}/#s_cfg.pkl")

    logger.info("load_pkl")
    logger.info(f"{vars(_s_cfg) = }")

    do_pack = False
    assert s_cfg.max_num_aircraft == _s_cfg.max_num_aircraft
    if s_cfg.mode == 'single':
        if _s_cfg.mode == 'multiple':
            do_pack = True
            logger.info("Will do pack!!!")
    elif s_cfg.mode == 'multiple':
        assert _s_cfg.mode == 'multiple'

    for i in range(len(args_list)):
        ds_fname = args_list[i]['ds_fname']
        ds_fname = f"{packed_folder}/{ds_fname}"

        _ds: T1 | T2
        _ds = load_pkl(ds_fname)

        _inf_len = inf_len
        if do_pack:
            _ds = unpack(_ds, logger)
            _inf_len = inf_len * s_cfg.max_num_aircraft

        _ds = make_dataset(s_cfg.mode, cfg.out_mode, _ds)
        logger.info(f"{_ds.keys() = }")

        l = get_dict_len(_ds)
        _r = _inf_len / l
        _r_list = [_inf_len] * (int(1. / _r))
        if l != sum(_r_list):
            _r_list += [l - sum(_r_list)]
        logger.info(f"{_r_list = }")

        # fake the future mask
        _ds['ori_fm'] = _ds['fm'].copy()
        _ds['fm'] = np.zeros_like(_ds['fm']) != 0

        ds_list: List[T1] | List[T2]
        ds_list = make_dict_split(
            _ds,
            _r_list,
            do_shuffle=False,
            is_ratio=False,
        )
        del _ds

        args_list[i]['ds_list'] = ds_list
    return s_cfg, cfg, mmn, args_list, do_pack


def main(i_cfg: InferenceConfig):
    mkdir(i_cfg.save_folder)
    set_torch_seeds(i_cfg.seed)

    logger = create_logger(i_cfg.save_folder)
    logger.info(f"{vars(i_cfg) = }")
    logger.info(get_gpu_status())

    #

    s_cfg, cfg, mmn, args_list, do_pack = loader(
        i_cfg.ckpt_folder,
        i_cfg.packed_folder,
        i_cfg.ckpt_idx_list,
        i_cfg.inf_len,
        i_cfg.device,
        logger,
    )
    ll = s_cfg.max_num_aircraft if do_pack else None
    is_shift = cfg.out_mode == 'shift'

    # --- #

    in_features = IN_FEATURES

    out_features = OUT_FEATURES
    if is_shift:
        out_features = OUT_SHIFT_FEATURES

    for ckpt_idx in i_cfg.ckpt_idx_list:
        ckpt_fname = f"{i_cfg.ckpt_folder}/ckpt/{ckpt_idx}.pt"

        if not Path(ckpt_fname).exists():
            continue

        _save_folder1 = f"{i_cfg.save_folder}/{ckpt_idx}"
        mkdir(_save_folder1, can_exists=True)

        for i in tqdm(range(len(args_list))):
            logger.info(get_gpu_status())

            _save_folder2 = args_list[i]['save_folder']
            _s_folder = f"{_save_folder1}/{_save_folder2}"
            mkdir(_s_folder, can_exists=True)

            ret = load_ckpt_workhouse(ckpt_fname, i_cfg.device)
            pipeline = ret[-1]

            ds_list: List[T1] | List[T2] = args_list[i]['ds_list']

            for j in tqdm(range(len(ds_list))):
                jj = f"{j:06d}"

                _ds = ds_list[j]

                np_pm_ori = _ds['pm']
                np_p_ori = mmn.undo_norm_workhouse(
                    _ds['p'],
                    np_pm_ori,
                    in_features,
                )
                np_f_ori = mmn.undo_norm_workhouse(
                    _ds['f'],
                    _ds['fm'],
                    out_features,
                )
                np_fm_ori = _ds['ori_fm']

                ds = PackedDictDictDataset(_ds)
                dl = make_dataloader(
                    ds,
                    batch_size=i_cfg.batch_size,
                    shuffle=False,
                )

                if is_shift:
                    _anchor = _ds['fa']
                    np_f_ori += _anchor

                if do_pack:
                    # 3d -> 4d
                    np_p_ori = pack(np_p_ori, ll)
                    np_pm_ori = pack(np_pm_ori, ll)
                    np_f_ori = pack(np_f_ori, ll)
                    np_fm_ori = pack(np_fm_ori, ll)

                dump_npy(np_p_ori, f"{_s_folder}/{jj}-p.npy")
                dump_npy(np_pm_ori, f"{_s_folder}/{jj}-pm.npy")
                dump_npy(np_f_ori, f"{_s_folder}/{jj}-f.npy")
                dump_npy(np_fm_ori, f"{_s_folder}/{jj}-fm.npy")

                for k in tqdm(range(i_cfg.num_pred), leave=False):
                    preds, _ = pipeline.inference(dl, get_tensor=False)
                    # del pipeline

                    pred: np.ndarray = preds[0]
                    logger.info(f"{pred.shape = }")

                    np_fp1_ori = mmn.undo_norm_workhouse(
                        pred,
                        _ds['fm'],
                        out_features,
                    )
                    np_fp2_ori = mmn.undo_norm_workhouse(
                        pred,
                        ~_ds['fm'],
                        out_features,
                    )

                    if is_shift:
                        _anchor = _ds['fa']
                        np_fp1_ori += _anchor
                        np_fp2_ori += _anchor

                    if do_pack:
                        # 3d -> 4d
                        np_fp1_ori = pack(np_fp1_ori, ll)
                        np_fp2_ori = pack(np_fp2_ori, ll)

                    dump_npy(np_fp1_ori, f"{_s_folder}/{jj}-fp1-{k:03d}.npy")
                    dump_npy(np_fp2_ori, f"{_s_folder}/{jj}-fp2-{k:03d}.npy")

            del pipeline

    logger.info(get_gpu_status())
    logger.info("DONE")
    return


"""
usage: inference.py [-h] --ckpt-folder CKPT_FOLDER --packed-folder PACKED_FOLDER --save-folder SAVE_FOLDER [--device DEVICE] --seed SEED --batch-size BATCH_SIZE --inf-len INF_LEN --num-pred NUM_PRED --ckpt-idx-nargs CKPT_IDX_NARGS [CKPT_IDX_NARGS ...]

options:
  -h, --help            show this help message and exit
  --ckpt-folder CKPT_FOLDER
  --packed-folder PACKED_FOLDER
  --save-folder SAVE_FOLDER
  --device DEVICE
  --seed SEED
  --batch-size BATCH_SIZE
  --inf-len INF_LEN
  --num-pred NUM_PRED
  --ckpt-idx-nargs CKPT_IDX_NARGS [CKPT_IDX_NARGS ...]
"""
if __name__ == '__main__':
    args = get_args()
    i_cfg = InferenceConfig(args)
    main(i_cfg)
