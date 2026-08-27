import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

from argparse import ArgumentParser, Namespace
from typing import Dict, List

import torch
import numpy as np
import matplotlib.pyplot as plt

from core.const import M_TO_NM, FT_TO_NM, OUT_FEATURES, OUT_SHIFT_FEATURES
from core.utils import get_time_str, create_logger, mkdir, dump_json, load_npy
from common.const import FIGSIZE, FIGDPI, FIG_PARAMS

plt.rcParams.update(FIG_PARAMS)


def plot_boxplot(
    x,
    feat,
    savefig_fname,
    boxplot_kwargs: Dict = {},
    hline_y=None,
):
    # figsize = (7.5, 5.2)
    # figsize = (7.5, 4.8)
    # figsize = (7.5, 4.4)
    figsize = (7.5, 4.0)
    fig, ax = plt.subplots(figsize=figsize)

    if hline_y is not None:
        ax.axhline(y=hline_y, color='red', linestyle='--')

    ax.boxplot(x, **boxplot_kwargs, showmeans=True)

    num_steps = len(x)
    ax.set_xticks(range(1, num_steps + 1))
    ax.set_xticklabels([str(i * 10) for i in range(1, num_steps + 1)])
    ax.set_xlabel('Prediction horizon (seconds)')

    if feat in ['x', 's_x']:
        unit = "m"
        feat_name = feat.upper() + " position"  # + " (Longitude)"
    elif feat in ['y', 's_y']:
        unit = "m"
        feat_name = feat.upper() + " position"  # + " (Latitude)"
    elif feat in ['altitude', 's_altitude']:
        unit = "ft"
        feat_name = "Altitude"
    elif feat == 'dist_3d':
        unit = "NM"
        feat_name = "3D distance"

    ax.set_ylabel(f'{feat_name} error ({unit})')

    ax.grid(axis='y', linestyle='--', alpha=0.8)

    plt.tight_layout()
    plt.savefig(savefig_fname, dpi=FIGDPI, bbox_inches='tight')
    plt.close('all')

    print(f"plot_boxplot: {savefig_fname} SAVED!")
    return


# --- #


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--save-folder", required=True)

    parser.add_argument("--inf-folder-nargs", nargs='+', required=True)
    parser.add_argument("--ckpt-idx-nargs", nargs='+', required=True)

    parser.add_argument("--num-pred", type=int, required=True)

    args = parser.parse_args()
    return args


def extrapolate_polyfit(
    v: np.ndarray,
    degree: int,
    past_points: int,
    future_points: int,
):
    """
    Extrapolates future points by performing batched polynomial regression
    over the last `past_points` of the sequence.

    Supports input shape:
        (batch, time, feat)
        (batch1, batch2, time, feat)
        or generally (..., time, feat)

    Returns:
        Shape (..., future_points, feat)
    """
    v = torch.as_tensor(v, dtype=torch.float32)

    if v.ndim < 3:
        raise ValueError("v must have shape (..., time, feat)")

    time_len = v.shape[-2]
    feat_dim = v.shape[-1]

    if past_points > time_len:
        raise ValueError(
            "past_points cannot be larger than the time dimension")

    if past_points < degree + 1:
        raise ValueError("past_points must be at least degree + 1")

    kwargs = dict(dtype=torch.float32, device=v.device)

    batch_shape = v.shape[:-2]

    v_tail = v[..., -past_points:, :]  # (..., past_points, feat)

    flat_batch = int(np.prod(batch_shape))
    v_tail_flat = v_tail.reshape(flat_batch, past_points, feat_dim)

    t_known = torch.arange(-(past_points - 1), 1, **kwargs)
    X_known = torch.vander(t_known, N=degree + 1, increasing=True)

    X_known_batched = X_known.unsqueeze(0).expand(flat_batch, -1, -1)

    W = torch.linalg.lstsq(X_known_batched, v_tail_flat).solution

    t_future = torch.arange(1, future_points + 1, **kwargs)
    X_future = torch.vander(t_future, N=degree + 1, increasing=True)

    v_future_flat = torch.matmul(X_future.unsqueeze(0), W)

    v_future = v_future_flat.reshape(*batch_shape, future_points, feat_dim)
    return v_future.detach().cpu().numpy()


def get_stats(arr_1d):
    p_keys = list(range(0, 101, 5))

    p_values = np.nanpercentile(arr_1d, p_keys)
    percentiles = {
        f"p_{p:02d}": float(val)
        for p, val in zip(p_keys, p_values)
    }

    _dict = {
        "num": len(arr_1d),
        "min": float(np.nanmin(arr_1d)),
        "max": float(np.nanmax(arr_1d)),
        "avg": float(np.nanmean(arr_1d)),
        "std": float(np.nanstd(arr_1d)),
        "median": float(np.nanmedian(arr_1d)),
        **percentiles,
    }
    return _dict


def get_error(f: np.ndarray, fp_median: np.ndarray, fm: np.ndarray):
    l = int(fm.shape[-1])
    error_list = [None] * l

    _error = abs(f - fp_median)

    for j in range(l):
        _m = fm[..., j]
        _e = _error[..., j, :][~_m]
        error_list[j] = _e

    return error_list


def get_list_error(f: np.ndarray, fp_list: List[np.ndarray], fm: np.ndarray):
    l = int(fm.shape[-1])

    error_list = [None] * l
    for fp in fp_list:
        _error = abs(f - fp)
        for j in range(l):
            _m = fm[..., j]
            _e = _error[..., j, :][~_m]

            if error_list[j] is None:
                error_list[j] = _e
            else:
                error_list[j] = np.concatenate((error_list[j], _e), axis=0)
    return error_list


def pack_error_list(error_list_list):
    l = len(error_list_list)
    if l == 0:
        return None
    elif l == 1:
        return error_list_list[0]

    ll = len(error_list_list[0])
    error_list = [None] * ll
    for i in range(l):
        for j in range(ll):
            _e = error_list_list[i][j]
            if error_list[j] is None:
                error_list[j] = _e
            else:
                error_list[j] = np.concatenate((error_list[j], _e), axis=0)
    return error_list


def main(args):
    save_folder = args.save_folder
    save_folder = f"{args.save_folder}/{get_time_str()}"

    folders = args.inf_folder_nargs
    ckpt_idx_list = args.ckpt_idx_nargs
    num_pred = args.num_pred

    max_records = 1000000
    future_len = 15

    is_shift = False

    mkdir(save_folder)
    logger = create_logger(save_folder)
    logger.info(f"{args = }")

    #

    # --- hard-coded --- #
    # see OUT_FEATURES, OUT_SHIFT_FEATURES
    out_features = OUT_FEATURES
    if is_shift:
        out_features = OUT_SHIFT_FEATURES
    scale = np.array([M_TO_NM, M_TO_NM, FT_TO_NM], dtype=np.float32)
    # --- hard-coded --- #

    ckpt_error_dict = {f"{int(ckpt):06d}": None for ckpt in ckpt_idx_list}

    for folder in folders:
        for ckpt in ckpt_idx_list:
            ckpt_idx = int(ckpt)
            ckpt_str = f"{ckpt_idx:06d}"

            _error_list = []

            _error_1st_list = []
            _error_2nd_list = []

            try:
                for i in range(max_records):
                    i_str = f"{i:06d}"

                    fname = f"{folder}/{ckpt_str}/test/{i_str}-f.npy"
                    f = load_npy(fname)
                    fname = f"{folder}/{ckpt_str}/test/{i_str}-fm.npy"
                    fm = load_npy(fname)

                    # --- extrapolate --- #
                    fname = f"{folder}/{ckpt_str}/test/{i_str}-p.npy"
                    p = load_npy(fname)
                    p = p[..., :3]
                    fname = f"{folder}/{ckpt_str}/test/{i_str}-pm.npy"
                    pm = load_npy(fname)

                    fp_1st = extrapolate_polyfit(p, 1, 3, future_len)
                    fp_2nd = extrapolate_polyfit(p, 2, 7, future_len)

                    _mask_1st = pm[..., -3]
                    _mask_2nd = pm[..., -7]

                    fp_1st[_mask_1st] = f[_mask_1st]
                    fp_2nd[_mask_2nd] = f[_mask_2nd]

                    error = get_error(f, fp_1st, fm)
                    _error_1st_list.append(error)
                    error = get_error(f, fp_2nd, fm)
                    _error_2nd_list.append(error)
                    # --- extrapolate --- #

                    fp_collected = []
                    for j in range(num_pred):
                        fname = f"{folder}/{ckpt_str}/test/{i_str}-fp1-{j:03d}.npy"
                        fp_collected.append(load_npy(fname))

                    fp = np.median(np.stack(fp_collected, axis=0), axis=0)

                    error = get_error(f, fp, fm)
                    _error_list.append(error)
            except:
                pass

            error_list = pack_error_list(_error_list)
            error_1st_list = pack_error_list(_error_1st_list)
            error_2nd_list = pack_error_list(_error_2nd_list)
            if error_list is None or error_1st_list is None or error_2nd_list is None:
                continue

            if ckpt_error_dict[ckpt_str] is None:
                ckpt_error_dict[ckpt_str] = error_list
                ckpt_error_dict[f"{ckpt_str}_1st"] = error_1st_list
                ckpt_error_dict[f"{ckpt_str}_2nd"] = error_2nd_list
            else:
                ckpt_error_dict[ckpt_str] = pack_error_list(
                    [ckpt_error_dict[ckpt_str], error_list])
                ckpt_error_dict[f"{ckpt_str}_1st"] = pack_error_list(
                    [ckpt_error_dict[f"{ckpt_str}_1st"], error_1st_list])
                ckpt_error_dict[f"{ckpt_str}_2nd"] = pack_error_list(
                    [ckpt_error_dict[f"{ckpt_str}_2nd"], error_2nd_list])

    for k, v in ckpt_error_dict.items():
        logger.info(f"{k = }")
        for i in range(future_len):
            logger.info(f"{v[i].shape = }")
        logger.info("----")

    # 'y', 'x', 'altitude',
    features = out_features + ['dist_3d']
    # hline_y_list = [9260, 9260, 1000, 5]
    hline_y_list = [None, None, 1000, None]

    stats_dict = {}
    for k, v in ckpt_error_dict.items():
        v.append(np.vstack(v))
        stats_dict[k] = {}

        _save_folder = f"{save_folder}/{k}"
        mkdir(_save_folder, can_exists=True)

        raw_plot_data = {feat: [] for feat in features}

        for i in range(future_len + 1):  # future + total
            arr = v[i]
            stats_dict[k][i] = {}

            for j, feat in enumerate(out_features):
                feat_data = arr[:, j]
                stats_dict[k][i][feat] = get_stats(feat_data)
                raw_plot_data[feat].append(feat_data)

            dist_3d = np.sqrt(np.sum((arr * scale)**2, axis=1))
            stats_dict[k][i]['dist_3d'] = get_stats(dist_3d)
            raw_plot_data['dist_3d'].append(dist_3d)

        for feat, hline_y in zip(features, hline_y_list):
            plot_boxplot(
                raw_plot_data[feat][:-1],
                feat,
                f"{_save_folder}/boxplot_{feat}.png",
                hline_y=hline_y,
            )
            plot_boxplot(
                raw_plot_data[feat][:-1],
                feat,
                f"{_save_folder}/boxplot_{feat}-sym.png",
                boxplot_kwargs=dict(sym=''),
                hline_y=hline_y,
            )
            plot_boxplot(
                raw_plot_data[feat][:-1],
                feat,
                f"{_save_folder}/boxplot_{feat}-sym-5-95.png",
                boxplot_kwargs=dict(sym='', whis=(5, 95)),
                hline_y=hline_y,
            )
            plot_boxplot(
                raw_plot_data[feat][:-1],
                feat,
                f"{_save_folder}/boxplot_{feat}-sym-10-90.png",
                boxplot_kwargs=dict(sym='', whis=(10, 90)),
                hline_y=hline_y,
            )

    dump_json(stats_dict, f"{save_folder}/stats_dict.json")

    logger.info("DONE")
    return


if __name__ == '__main__':
    args = get_args()
    main(args)
