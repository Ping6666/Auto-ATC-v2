from typing import Dict, List, Tuple
from argparse import ArgumentParser, Namespace

import numpy as np

from core.const import (
    NORM_FEATURES,
    XYZ_FEATURES,
    IN_FEATURES,
    OUT_FEATURES,
    OUT_SHIFT_FEATURES,
)
from core.utils import (
    create_logger,
    set_torch_seeds,
    mkdir,
    dump_pkl,
    load_pkl,
    load_npy,
    get_dict_len,
    make_dict_split,
    dict_random_select,
)
from core.config import SampleConfig, PackConfig
from core.norm import MinMaxNorm, MeanStdNorm


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--sample-folder", required=True)
    parser.add_argument("--save-folder", required=True)

    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--sampling-probability", type=float, required=True)

    args = parser.parse_args()
    return args


# --- #


def main(p_cfg: PackConfig):
    # NOTE only use mmn for now

    save_folder = p_cfg.save_folder
    mkdir(save_folder)

    set_torch_seeds(p_cfg.seed)

    sample_folder = p_cfg.sample_folder
    s_cfg: SampleConfig = load_pkl(f"{sample_folder}/#cfg.pkl")

    logger = create_logger(p_cfg.save_folder)
    logger.info(f"{vars(p_cfg) = }")
    logger.info(f"{vars(s_cfg) = }")

    dump_pkl(p_cfg, f"{p_cfg.save_folder}/#p_cfg.pkl")
    dump_pkl(s_cfg, f"{p_cfg.save_folder}/#s_cfg.pkl")

    #

    is_single = s_cfg.mode == 'single'

    #

    _np_i: np.ndarray
    np_xyz: np.ndarray
    np_i: Dict[str, np.ndarray]
    np_im: np.ndarray
    np_o: np.ndarray
    np_om: np.ndarray
    np_p: np.ndarray
    np_pm: np.ndarray
    np_f: np.ndarray
    np_fm: np.ndarray

    if is_single:
        np_im = load_npy(f"{sample_folder}/im.npy", allow_pickle=True)
        np_o = load_npy(f"{sample_folder}/o.npy", allow_pickle=True)
        np_om = load_npy(f"{sample_folder}/om.npy", allow_pickle=True)
    else:  # is_multi
        np_xyz = load_npy(f"{sample_folder}/xyz.npy", allow_pickle=True)

    _np_i = load_npy(f"{sample_folder}/i.npy", allow_pickle=True)
    np_i = _np_i.item()  # to dict

    np_p = load_npy(f"{sample_folder}/p.npy", allow_pickle=True)
    np_pm = load_npy(f"{sample_folder}/pm.npy", allow_pickle=True)

    np_f = load_npy(f"{sample_folder}/f.npy", allow_pickle=True)
    np_fm = load_npy(f"{sample_folder}/fm.npy", allow_pickle=True)

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

    if is_single:
        logger.info(f"{np_im.shape = }")
        logger.info(f"{np_o.shape = } {np_om.shape = }")
    else:  # is_multi
        logger.info(f"{np_xyz.shape = }")

    for k in np_i.keys():
        logger.info(f"{k = } {np_i[k].shape = }")
    logger.info(f"{np_p.shape = } {np_pm.shape = }")
    logger.info(f"{np_fa.shape = } {np_fam.shape = }")
    logger.info(f"{np_f.shape = } {np_fm.shape = }")
    logger.info(f"{np_fs.shape = } {np_fsm.shape = }")

    #

    mmn = MinMaxNorm()
    msn = MeanStdNorm()

    args_list: List[Tuple[np.ndarray, np.ndarray, List[str]]] = [
        (np_p, np_pm, IN_FEATURES),
        (np_f, np_fm, OUT_FEATURES),
        (np_fs, np_fsm, OUT_SHIFT_FEATURES),
    ]
    if is_single:
        args_list.append((np_o, np_om, IN_FEATURES))
    else:  # is_multi
        np_xyzm = np_pm[..., -1]
        args_list.append((np_xyz, np_xyzm, XYZ_FEATURES))
    for f in NORM_FEATURES:
        v = None
        for vv, mm, ff in args_list:
            if f not in ff:
                continue

            i = ff.index(f)
            _vv = vv[..., i][~mm]

            if v is None:
                v = _vv
            else:
                # print(f"{v.shape = }")
                # print(f"{_vv.shape = }")
                v = np.concatenate((v, _vv), axis=-1)

        if v is not None:
            mmn.register(f, v)
            msn.register(f, v)

    logger.info(f"{mmn.norm = }")
    logger.info(f"{msn.norm = }")

    dump_pkl(mmn, f"{save_folder}/mmn.pkl")
    dump_pkl(msn, f"{save_folder}/msn.pkl")

    np_p_norm = mmn.do_norm_workhouse(np_p, np_pm, IN_FEATURES)
    np_f_norm = mmn.do_norm_workhouse(np_f, np_fm, OUT_FEATURES)
    np_fs_norm = mmn.do_norm_workhouse(np_fs, np_fsm, OUT_SHIFT_FEATURES)

    if is_single:
        np_o = mmn.do_norm_workhouse(np_o, np_om, IN_FEATURES)
    # else:  # is_multi
    #     np_xyz_norm = mmn.do_norm_workhouse(np_xyz, np_xyzm, XYZ_FEATURES)

    #

    _norm_ds = dict(
        i=np_i,
        p=np_p_norm,
        pm=np_pm,
        fa=np_fa,
        fam=np_fam,
        f=np_f_norm,
        fm=np_fm,
        fs=np_fs_norm,
        fsm=np_fsm,
    )
    if is_single:
        _norm_ds['im'] = np_im
        _norm_ds['o'] = np_o
        _norm_ds['om'] = np_om
    else:  # is_multi
        _norm_ds['xyz'] = np_xyz

    logger.info(f"{get_dict_len(_norm_ds) = }")

    norm_ds = dict_random_select(_norm_ds, p_cfg.sampling_probability)
    logger.info(f"{get_dict_len(norm_ds) = }")

    _train_ds, _val_ds, _test_ds = make_dict_split(
        norm_ds,
        [0.7, 0.2, 0.1],
        do_shuffle=False,
    )

    dump_pkl(_train_ds, f"{save_folder}/train_ds.pkl")
    dump_pkl(_val_ds, f"{save_folder}/val_ds.pkl")
    dump_pkl(_test_ds, f"{save_folder}/test_ds.pkl")

    logger.info("DONE")
    return


"""
usage: packer.py [-h] --sample-folder SAMPLE_FOLDER --save-folder SAVE_FOLDER --seed SEED --sampling-probability SAMPLING_PROBABILITY

options:
  -h, --help            show this help message and exit
  --sample-folder SAMPLE_FOLDER
  --save-folder SAVE_FOLDER
  --seed SEED
  --sampling-probability SAMPLING_PROBABILITY
"""
if __name__ == '__main__':
    args = get_args()
    p_cfg = PackConfig(args)
    main(p_cfg)
