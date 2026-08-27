from typing import Dict, List
from argparse import ArgumentParser, Namespace
from pathlib import Path
from copy import deepcopy
import traceback

import torch
import numpy as np

from core.const import IN_FEATURES, OUT_FEATURES, OUT_SHIFT_FEATURES
from core.utils import (
    create_logger,
    get_gpu_status,
    set_torch_seeds,
    mkdir,
    dump_pkl,
    dump_npy,
)
from core.config import custom_type, SampleConfig, InteractionConfig
from core.norm import MinMaxNorm
from core.storage import OpenScope_DataStorage
from core.dataset import PackedDictDictDataset
from core.dataset.utils import pack, unpack
from core.factory import make_dataloader
from simulation.utils import gen_uuid
from simulation.convertor import GlideControl
from simulation import OpenScope_Env, Tape, Game
from common.workhouse import load_ckpt_workhouse

T1 = Dict[str, np.ndarray | Dict[str, np.ndarray]]


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--num-proc", type=int, required=True)

    parser.add_argument("--device", required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--batch-size", type=int, required=True)

    parser.add_argument("--ckpt-folder", required=True)
    parser.add_argument("--save-folder", required=True)
    parser.add_argument("--save-step", type=int, required=True)

    parser.add_argument("--num-exp", type=int, required=True)
    parser.add_argument("--num-pred", type=int, required=True)
    parser.add_argument("--ckpt-idx", type=custom_type, required=True)
    parser.add_argument('--nargs-take-idx', nargs='+', type=int, required=True)

    parser.add_argument("--assign-rwy", type=str, default=None)

    parser.add_argument("--num-timestamps", type=int, required=True)
    parser.add_argument('--render', action="store_true")

    args = parser.parse_args()
    return args


# --- #


def get_pred(pred: np.ndarray, sample: T1, mmn: MinMaxNorm, is_shift: bool):
    fm = sample['fm']

    np_fp = None
    if is_shift:
        np_fp = mmn.undo_norm_workhouse(pred, fm, OUT_SHIFT_FEATURES)

        _anchor = sample['fa']
        np_fp += _anchor
    else:
        np_fp = mmn.undo_norm_workhouse(pred, fm, OUT_FEATURES)

    _new_pred = np_fp
    # print(f"{_new_pred.shape = }")  # (new_shape, S, T, ?)
    return _new_pred


def get_norm(sample: List[np.ndarray], mmn: MinMaxNorm, num_pred: int):
    np_xyz, np_i, np_p, np_pm, np_f, np_fm = sample

    np_p_ori = np_p.copy()
    np_fm_ori = np_fm.copy()

    # fake the future mask
    # np_fm_ori = np_fm.copy()
    np_fm[:] = np_fm[..., 0:1]

    #

    # future anchor
    np_fa = np_f[..., 0:1, :].copy()
    np_fam = np_fm[..., 0:1].copy()

    # future shift
    np_fs = np_f[..., 1:, :].copy() - np_fa
    np_fsm = np_fm[..., 1:].copy()

    np_p[np_pm] = 0
    np_f[np_fm] = 0
    np_fs[np_fm[..., 1:]] = 0

    np_p_norm = mmn.do_norm_workhouse(np_p, np_pm, IN_FEATURES)
    np_f_norm = mmn.do_norm_workhouse(np_f, np_fm, OUT_FEATURES)
    np_fs_norm = mmn.do_norm_workhouse(np_fs, np_fsm, OUT_SHIFT_FEATURES)

    # see fn. make_dataset()
    norm_ds: T1
    norm_ds = dict(
        xyz=np_xyz,
        #
        i=np_i,
        p=np_p_norm,
        pm=np_pm,
        fa=np_fa,
        fam=np_fam,
        f=np_f_norm,
        fm=np_fm,
        fs=np_fs_norm,
        fsm=np_fsm,
        #
        p_ori=np_p_ori,
        fm_ori=np_fm_ori,
    )

    #

    new_ds: T1 = {}
    for k, v in norm_ds.items():
        if isinstance(v, Dict):
            new_ds[k] = {}
            for k1, v1 in v.items():
                ori_shape = v1.shape
                new1_shape = (num_pred * ori_shape[0], *ori_shape[1:])
                # _v1 = np.expand_dims(v1, axis=0)
                _v1 = v1
                _v1 = np.repeat(_v1, repeats=num_pred, axis=0)
                new_ds[k][k1] = _v1.reshape(new1_shape)
                # print(f"{k = } {k1 = } {new_ds[k][k1].shape = }")
        elif isinstance(v, np.ndarray):
            ori_shape = v.shape
            new1_shape = (num_pred * ori_shape[0], *ori_shape[1:])
            # _v = np.expand_dims(v, axis=0)
            _v = v
            _v = np.repeat(_v, repeats=num_pred, axis=0)
            new_ds[k] = _v.reshape(new1_shape)
            # print(f"{k = } {new_ds[k].shape = }")
        else:
            raise NotImplementedError
    return new_ds


# --- #


def make_game(uuid, save_folder, s_cfg: SampleConfig, assign_rwy, render):
    return Game(
        OpenScope_Env(uid=uuid, icao=s_cfg.icao, render=render),
        Tape(save_folder=f"{save_folder}/tape"),
        OpenScope_DataStorage(s_cfg, assign_rwy),
        save_folder,
    )


def dumper(
    save_folder: str,
    #
    ds: OpenScope_DataStorage,
    dump_ds: Dict[str, Dict[str, List | List[List]]],
    dump_all: Dict[str, List],
):
    # save raw

    for c in ds.storage.keys():
        _folder = f'{save_folder}/samples/{c}/raw/storage'
        mkdir(_folder, can_exists=True)

        s = ds.storage[c]
        for k in s.keys():
            fname = f'{_folder}/{k}.npy'
            dump_npy(s[k], fname)

    for c, v in dump_ds.items():
        _folder = f'{save_folder}/samples/{c}/raw/sample'
        mkdir(_folder, can_exists=True)
        dump_pkl(v, f"{_folder}/plot_dataset.pkl")

    _folder = f'{save_folder}/samples/'
    mkdir(_folder, can_exists=True)
    for k, v in dump_all.items():
        _v = np.vstack(v)
        print(f"{k = } {_v.shape = }")
        dump_npy(_v, f"{_folder}/{k}.npy")
    return


def worker(
    queue: torch.multiprocessing.Queue,
    #
    uuid: str,
    ckpt_fname: str,
    #
    device: str,
    seed: int,
    batch_size: int,
    #
    save_folder: str,
    save_step: int,
    #
    num_pred: int,
    take_idx: int,
    assign_rwy: str | None,
    #
    num_timestamps: int,
    render: bool = False,
):
    queue.put(uuid)

    mkdir(save_folder)
    set_torch_seeds(seed)

    logger = create_logger(save_folder, logger_name=uuid)

    try:

        kwargs = {
            "uuid": uuid,
            "ckpt_fname": ckpt_fname,
            #
            "device": device,
            "seed": seed,
            "batch_size": batch_size,
            #
            "save_folder": save_folder,
            "save_step": save_step,
            #
            "num_pred": num_pred,
            "take_idx": take_idx,
            #
            "assign_rwy": assign_rwy,
            #
            "num_timestamps": num_timestamps,
            "render": render,
        }
        logger.info(f'{kwargs = }')
        logger.info(get_gpu_status())

        s_cfg, p_cfg, cfg, mmn, _, pipeline = load_ckpt_workhouse(
            ckpt_fname, device)
        assert 1 <= take_idx and take_idx < s_cfg.future_len

        logger.info(f"{vars(s_cfg) = }")
        logger.info(f"{vars(p_cfg) = }")
        logger.info(f"{vars(cfg) = }")
        logger.info(get_gpu_status())

        is_single = s_cfg.mode == 'single'
        is_shift = cfg.out_mode == 'shift'

        #

        game = make_game(uuid, save_folder, s_cfg, assign_rwy, render)
        game.save(0)
        ds = game.ds  # OpenScope_DataStorage

        gc = GlideControl(s_cfg.icao, ds, take_idx)

        #

        dump_all = {'p': [], 'pm': [], 'f': [], 'fm': [], 'fp': []}
        dump_ds: Dict[str, Dict[str, List | List[List]]] = {}

        actions_list = []
        callsigns_ils_info = []
        for i in range(num_timestamps):
            ii = i + 1

            game.step_worker(actions_list, callsigns_ils_info)
            actions_list = []
            callsigns_ils_info = []

            ##

            if assign_rwy is not None:
                all_new_callsigns = ds.get_new_callsigns()
                if len(all_new_callsigns) > 0:
                    for c in all_new_callsigns:
                        action = f"{c} e {assign_rwy}"
                        actions_list.append(action)

            if ii % s_cfg.idx_step == 0:
                print(f"num timestamps: {i+1:05d} / {num_timestamps:05d}")

                all_callsigns = ds.get_callsigns()

                c_len = len(all_callsigns)
                if c_len == 0:
                    continue

                # sample data & model pred.

                _all_callsigns = all_callsigns[:s_cfg.max_num_aircraft]
                _ds = ds.sampler_multi(_all_callsigns)
                if _ds is None:
                    continue

                _norm_ds = get_norm(_ds, mmn, num_pred)
                _norm_ds2 = _norm_ds

                if is_single:
                    _norm_ds2 = deepcopy(_norm_ds)
                    _norm_ds2 = unpack(_norm_ds2)

                if is_shift:
                    _norm_ds2['f'] = _norm_ds2['fs']
                    _norm_ds2['fm'] = _norm_ds2['fsm']

                norm_ds = PackedDictDictDataset(_norm_ds2)
                loader = make_dataloader(norm_ds, batch_size, shuffle=False)
                preds, _ = pipeline.inference(loader, get_tensor=False)
                pred = get_pred(preds[0], _norm_ds2, mmn, is_shift)

                if is_single:
                    pred = pack(pred, s_cfg.max_num_aircraft)

                # save for plot

                for j, c in enumerate(_all_callsigns):
                    if c not in dump_ds.keys():
                        dump_ds[c] = {'samples': [], 'predictions': []}
                    c_ds = {}
                    for k, v in _norm_ds.items():
                        if isinstance(v, Dict):
                            c_ds[k] = {}
                            for k1, v1 in v.items():
                                c_ds[k][k1] = v1[:, j:j + 1]
                        elif isinstance(v, np.ndarray):
                            c_ds[k] = v[:, j:j + 1]
                        else:
                            raise NotImplementedError
                    dump_ds[c]['samples'].append(c_ds)

                    for m in range(num_pred):
                        if len(dump_ds[c]['predictions']) < num_pred:
                            dump_ds[c]['predictions'].append([])
                        _p = pred[m, j:j + 1]
                        dump_ds[c]['predictions'][m].append(_p)

                # real_fm = np.zeros_like(_norm_ds['fm']) == 0
                # real_fm[..., 0] = _norm_ds['fm'][..., 0]
                real_fm = _norm_ds['fm']
                dump_all['p'].append(_norm_ds['p_ori'][0:1])
                dump_all['pm'].append(_norm_ds['pm'][0:1])
                dump_all['f'].append(_norm_ds['f'][0:1])
                dump_all['fm'].append(real_fm[0:1])
                dump_all['fp'].append(np.expand_dims(pred.copy(), 0))

                # find next action

                pm = _norm_ds['pm']
                fa = _norm_ds['fa']
                fam = _norm_ds['fam']
                fm = _norm_ds['fm']
                for j, c in enumerate(_all_callsigns):
                    c_pm = pm[0, j]
                    c_fa = fa[0, j, 0]
                    fam_check = bool(fam[0, j, 0]) == True
                    fm_check = np.any(fm[0, j] == True)
                    fp = pred[:, j]

                    _pm = c_pm == False
                    valid_len = len(_pm) - np.argmax(_pm[::-1])

                    if c == 'PAD' or fam_check or fm_check:
                        # just in case
                        raise AssertionError

                    can_ctl = valid_len >= s_cfg.past_len

                    action, ils_info = gc.get_action(
                        c,
                        game.c_info[c],
                        ds.get_state(c),
                        c_fa,
                        fp,
                        can_ctl,
                    )

                    if action is not None:
                        actions_list.append(action)
                    if ils_info is not None:
                        callsigns_ils_info.append(ils_info)

                ###

            game.keep_time()

            ##

            if ii % save_step == 0:
                game.save(ii)

        #

        game.close_worker()
        game.save(-1)

        logger.info(get_gpu_status())
        logger.info("Half Done")

        dumper(save_folder, ds, dump_ds, dump_all)

        logger.info(get_gpu_status())
        logger.info("DONE")

    except Exception:
        logger.info("ERROR")
        logger.info(traceback.format_exc())

        try:
            game.save(-1)
            dumper(save_folder, ds, dump_ds, dump_all)
            logger.info("SAVED!")

        except Exception:
            logger.info("ERROR")
            logger.info(traceback.format_exc())

    queue.put(uuid)
    return


def main(i_cfg: InteractionConfig):
    mkdir(i_cfg.save_folder)
    set_torch_seeds(i_cfg.seed)

    uuid = gen_uuid(5)

    main_logger = create_logger(i_cfg.save_folder, logger_name=uuid)
    main_logger.info(f"{vars(i_cfg) = }")
    main_logger.info(get_gpu_status())

    #

    mp = torch.multiprocessing
    ctx = mp.get_context('spawn')
    pool = ctx.Pool(processes=i_cfg.num_proc)

    manager = mp.Manager()
    queue = manager.Queue()

    _id = 0
    map_iterable = []

    for ckpt_idx in i_cfg.nargs_ckpt_idx:
        _ckpt_str = f"{ckpt_idx:06d}"
        ckpt_fname = f"{i_cfg.ckpt_folder}/ckpt/{_ckpt_str}.pt"
        save_folder = f"{i_cfg.save_folder}/{_ckpt_str}/"

        if not Path(ckpt_fname).is_file():
            main_logger.info(f"File Not Found | {ckpt_fname}")
            continue

        for take_idx in i_cfg.nargs_take_idx:
            for i in range(i_cfg.num_exp):
                _id += 1
                _iterable = (
                    queue,
                    #
                    f"{uuid}-{_id:05d}",
                    ckpt_fname,
                    #
                    i_cfg.device,
                    i_cfg.seed + _id,
                    i_cfg.batch_size,
                    #
                    f"{save_folder}/{take_idx:02d}/{i_cfg.num_pred:03d}-{i:03d}/",
                    i_cfg.save_step,
                    #
                    i_cfg.num_pred,
                    take_idx,
                    #
                    i_cfg.assign_rwy,
                    #
                    i_cfg.num_timestamps,
                    i_cfg.render,
                )
                map_iterable.append(_iterable)

    # --- main_logger --- #
    for _iter in map_iterable:
        main_logger.info(f'{_iter = }')
    main_logger.info("####################")
    # --- main_logger --- #

    assert len(map_iterable) != 0

    result = pool.starmap_async(worker, map_iterable)

    # --- main_logger --- #
    _num_task = len(map_iterable)
    _start = set()
    _end = set()
    while True:
        _uuid = queue.get()

        if _uuid not in _start:
            _start.add(_uuid)
            main_logger.info(f"Worker: {_uuid} init!")

        else:
            _end.add(_uuid)
            main_logger.info(f"Worker: {_uuid} done!")

        if len(_end) == _num_task:
            break
    # --- main_logger --- #

    result.get()

    pool.close()
    pool.join()

    main_logger.info("ALL DONE")
    return


"""
usage: interaction.py [-h] --num-proc NUM_PROC --device DEVICE --seed SEED --batch-size BATCH_SIZE --ckpt-folder
                      CKPT_FOLDER --save-folder SAVE_FOLDER --save-step SAVE_STEP --num-exp NUM_EXP --num-pred
                      NUM_PRED --ckpt-idx CKPT_IDX --nargs-take-idx NARGS_TAKE_IDX [NARGS_TAKE_IDX ...]
                      [--assign-rwy ASSIGN_RWY] --num-timestamps NUM_TIMESTAMPS [--render]

options:
  -h, --help            show this help message and exit
  --num-proc NUM_PROC
  --device DEVICE
  --seed SEED
  --batch-size BATCH_SIZE
  --ckpt-folder CKPT_FOLDER
  --save-folder SAVE_FOLDER
  --save-step SAVE_STEP
  --num-exp NUM_EXP
  --num-pred NUM_PRED
  --ckpt-idx CKPT_IDX
  --nargs-take-idx NARGS_TAKE_IDX [NARGS_TAKE_IDX ...]
  --assign-rwy ASSIGN_RWY
  --num-timestamps NUM_TIMESTAMPS
  --render
"""
if __name__ == '__main__':
    args = get_args()
    i_cfg = InteractionConfig(args)
    main(i_cfg)
