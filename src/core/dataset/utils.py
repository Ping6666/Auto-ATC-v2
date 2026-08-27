from typing import Dict, List
from copy import deepcopy
import logging

from tqdm import tqdm
import numpy as np

from core.utils import get_dict_len

T1 = Dict[str, np.ndarray]
T2 = Dict[str, Dict[str, np.ndarray]]


def pack(v: np.ndarray, ll: int):
    return v.reshape((-1, ll, *v.shape[1:]))


def unpack(
    ds: Dict[str, np.ndarray | Dict[str, np.ndarray]],
    logger: logging.Logger = None,
):
    """
    see fn. sample_single()
    """
    # ['i', 'p', 'pm', 'fa', 'fam', 'f', 'fm', 'fs', 'fsm', 'xyz'] => ['i', 'im', 'o', 'om', 'p', 'pm', 'fa', 'fam', 'f', 'fm', 'fs', 'fsm']

    if logger is not None:
        for k, v in ds.items():
            try:
                logger.info(f"{k = } {v.shape = }")
            except:
                pass

    info_dict: Dict[str, List] = {}
    info_mask = []
    other_curr, other_curr_mask = [], []
    past, past_mask = [], []
    anchor, anchor_mask = [], []
    future, future_mask = [], []
    future_shift, future_shift_mask = [], []

    l = get_dict_len(ds)
    for idx1 in tqdm(range(l)):
        xyz = ds['xyz'][idx1]
        i = {k: v[idx1] for k, v in ds['i'].items()}

        p = ds['p'][idx1]
        pm = ds['pm'][idx1]
        fa = ds['fa'][idx1]
        fam = ds['fam'][idx1]
        f = ds['f'][idx1]
        fm = ds['fm'][idx1]
        fs = ds['fs'][idx1]
        fsm = ds['fsm'][idx1]

        ll = len(xyz)
        cs_len = np.sum(fam == False)
        empty_idx = np.arange(cs_len, ll)

        for idx2 in tqdm(range(ll), leave=False):
            ego_p = p[idx2]
            ego_pm = pm[idx2]
            ego_fa = fa[idx2]
            ego_fam = fam[idx2]
            ego_f = f[idx2]
            ego_fm = fm[idx2]
            ego_fs = fs[idx2]
            ego_fsm = fsm[idx2]

            ego_xyz = xyz[idx2:idx2 + 1].copy()
            valid_xyz = (xyz - ego_xyz)[:cs_len]
            valid_l2 = np.linalg.norm(valid_xyz, axis=-1)
            valid_idx = np.argsort(valid_l2)

            _valid_idx = np.concatenate((valid_idx, empty_idx))
            other_i = deepcopy(i)
            for k in other_i.keys():
                v = other_i[k]
                other_i[k] = v[_valid_idx]
            # NOTE: im will not change
            other_im = fam.copy().squeeze(axis=-1)
            other_c = p[_valid_idx][:, -1, :]
            other_cm = pm[_valid_idx][:, -1]

            ##

            past.append(ego_p)
            past_mask.append(ego_pm)
            anchor.append(ego_fa)
            anchor_mask.append(ego_fam)
            future.append(ego_f)
            future_mask.append(ego_fm)
            future_shift.append(ego_fs)
            future_shift_mask.append(ego_fsm)

            if len(info_dict.keys()) == 0:
                info_dict = {k: [] for k in other_i.keys()}
            for k, v in other_i.items():
                info_dict[k].append(v)
            info_mask.append(other_im)
            other_curr.append(other_c)
            other_curr_mask.append(other_cm)

    #

    np_info_dict: Dict[str, np.ndarray] = {}
    for k, v in info_dict.items():
        if 'emb' in k:
            np_info_dict[k] = np.array(v, dtype=np.int32)
        else:
            np_info_dict[k] = np.array(v, dtype=np.float32)

    new_ds: T1 | T2 = {
        'i': np_info_dict,
        'im': np.array(info_mask, dtype=bool),
        'o': np.array(other_curr, dtype=np.float32),
        'om': np.array(other_curr_mask, dtype=bool),
        'p': np.array(past, dtype=np.float32),
        'pm': np.array(past_mask, dtype=bool),
        'fa': np.array(anchor, dtype=np.float32),
        'fam': np.array(anchor_mask, dtype=bool),
        'f': np.array(future, dtype=np.float32),
        'fm': np.array(future_mask, dtype=bool),
        'fs': np.array(future_shift, dtype=np.float32),
        'fsm': np.array(future_shift_mask, dtype=bool),
    }

    if logger is not None:
        for k in new_ds['i'].keys():
            logger.info(f"{k = } {new_ds['i'][k].shape = }")
        logger.info(f"{new_ds['im'].shape = }")
        logger.info(f"{new_ds['o'].shape = } {new_ds['om'].shape = }")
        logger.info(f"{new_ds['p'].shape = } {new_ds['pm'].shape = }")
        logger.info(f"{new_ds['fa'].shape = } {new_ds['fam'].shape = }")
        logger.info(f"{new_ds['f'].shape = } {new_ds['fm'].shape = }")
        logger.info(f"{new_ds['fs'].shape = } {new_ds['fsm'].shape = }")
    return new_ds
