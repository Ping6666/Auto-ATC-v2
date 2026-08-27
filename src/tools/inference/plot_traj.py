import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

import numpy as np
import matplotlib.pyplot as plt

from core.utils import load_pkl, load_npy
from core.fms import np_get_xy
from core.config import SampleConfig
from common.const import FIGDPI, FIG_PARAMS

plt.rcParams.update(FIG_PARAMS)


def plot_traj(p, f, fp_list, savefig_fname: str):
    figsize = (7, 5.5)
    plt.subplots(figsize=figsize)

    plt.plot(p[..., 1], p[..., 0], 'b', label='Past')
    plt.plot(f[..., 1], f[..., 0], 'r', label='Future')

    for i, fp in enumerate(fp_list):
        label = 'Predictions' if i == 0 else None
        plt.plot(fp[..., 1], fp[..., 0], 'g--', linewidth=1, label=label)

    fp = np.median(np.stack(fp_list, axis=0), axis=0)
    plt.plot(fp[..., 1], fp[..., 0], 'k', label='Final prediction')

    plt.legend()
    plt.xlabel('X position (meter)')
    plt.ylabel('Y position (meter)')

    #

    ref_pos = [
        # ["N35d33m12.00", "E139d46m52.00"],
        35.55333,
        139.78111,
        0,
    ]
    scale_bar = {
        'point1': [35.55999, 139.76907],
        'point2': [35.53660, 139.78567],
        'text': '3.0 km',
    }

    scale_bar_x1, scale_bar_y1 = np_get_xy(scale_bar['point1'][0],
                                           scale_bar['point1'][1], ref_pos)
    scale_bar_x2, scale_bar_y2 = np_get_xy(scale_bar['point2'][0],
                                           scale_bar['point2'][1], ref_pos)

    scale_bar_length = np.sqrt((scale_bar_x1 - scale_bar_x2)**2 +
                               (scale_bar_y1 - scale_bar_y2)**2)

    x_lim = plt.gca().get_xlim()
    y_lim = plt.gca().get_ylim()
    y_shift = (y_lim[1] - y_lim[0])
    scale_bar_x = x_lim[0] + 0.95 * (x_lim[1] - x_lim[0])
    scale_bar_y = y_lim[0] + 0.05 * y_shift

    plt.hlines(
        y=scale_bar_y,
        xmin=scale_bar_x,
        xmax=scale_bar_x + scale_bar_length,
        colors='m',
        linewidth=2,
    )

    plt.text(
        scale_bar_x + scale_bar_length / 2,
        scale_bar_y + 0.025 * y_shift,
        scale_bar['text'],
        color='m',
        ha='center',
    )

    #

    plt.tight_layout()
    plt.savefig(savefig_fname, dpi=FIGDPI)
    plt.close('all')

    print(f"plot_traj: {savefig_fname} SAVED!")
    return


# --- #


def main():
    num_pred = 20

    packed_folder = "/path/to/packed/YYYY_MM_DD-HH_MM_SS/"
    fp_folder = "/path/to/inf/YYYY_MM_DD-HH_MM_SS/xxxxxx/test/"

    _s_cfg: SampleConfig = load_pkl(f"{packed_folder}/#s_cfg.pkl")

    _ds = load_pkl(f"{packed_folder}/test_ds.pkl")

    print(f"{_s_cfg = }")
    print(f"{_ds.keys() = }")

    # for i in range(max_records):
    #     i_str = f"{i:06d}"

    i_str = f"{0:06d}"

    fname = f"{fp_folder}/{i_str}-p.npy"
    p = load_npy(fname)
    fname = f"{fp_folder}/{i_str}-pm.npy"
    pm = load_npy(fname)

    fp_list = []
    for j in range(num_pred):
        fname = f"{fp_folder}/{i_str}-f.npy"
        f = load_npy(fname)
        fname = f"{fp_folder}/{i_str}-fm.npy"
        fm = load_npy(fname)

        fname = f"{fp_folder}/{i_str}-fp1-{j:03d}.npy"
        fp1 = load_npy(fname)
        fp_list.append(fp1)

    # for i in range(1024):

    i = 453
    _p = p[i]
    _pm = pm[i]
    _f = f[i]
    _fm = fm[i]
    _fp_list = [fp[i][~_fm] for fp in fp_list]
    plot_traj(_p[~_pm], _f[~_fm], _fp_list, f"./save/inf_plt/{i:04d}.png")

    print("DONE")
    return


if __name__ == '__main__':
    main()
