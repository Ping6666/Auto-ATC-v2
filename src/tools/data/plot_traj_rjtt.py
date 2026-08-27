import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

from typing import List

import numpy as np
import matplotlib.pyplot as plt

from core.storage import Opensky_DataStorage
from core.storage.utils import load_airport_info
from core.fms import np_get_xy
from common.const import FIGSIZE, FIGDPI, FIG_PARAMS

plt.rcParams.update(FIG_PARAMS)


def plot_raw_trajs(data, runways_order: List, savefig_fname: str):
    sc = ['k', 'g', 'k', 'b', 'r', 'c', 'y', 'm']

    figsize = (7, 5.5)
    plt.subplots(figsize=figsize)

    labeled_rwy = set()

    for ds in data:
        x = ds['x']
        y = ds['y']
        rwy = ds['rwy_ori']
        _sc = sc[runways_order.index(rwy)]

        if rwy in labeled_rwy:
            rwy = None
        else:
            labeled_rwy.add(rwy)

        plt.plot(x, y, _sc, label=rwy, linewidth=1.25)
        # plt.plot(x, y)

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
    scale_bar_x = x_lim[0] + 0.60 * (x_lim[1] - x_lim[0])
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

    print(f"plot_raw_trajs: {savefig_fname} SAVED!")
    return


def plot_raw_trajs2(data, runways_order: List, savefig_fname: str):
    sc = ['k', 'g', 'k', 'b', 'r', 'c', 'y', 'm']

    figsize = (7, 5.5)
    fig, ax = plt.subplots(figsize=figsize)

    labeled_rwy = set()

    for ds in data:
        x = ds['x']
        y = ds['y']
        rwy = ds['rwy_ori']
        _sc = sc[runways_order.index(rwy)]

        if rwy in labeled_rwy:
            rwy = None
        else:
            labeled_rwy.add(rwy)

        plt.plot(x, y, _sc, label=rwy, linewidth=1.25)
        # plt.plot(x, y)

    plt.xlabel('X position (meter)')
    plt.ylabel('Y position (meter)')

    ax.set_xlim((-15000, 25000))
    ax.set_ylim((-31000, 25000))

    #

    plt.tight_layout()
    plt.savefig(savefig_fname, dpi=FIGDPI)
    plt.close('all')

    print(f"plot_raw_trajs: {savefig_fname} SAVED!")
    return


def dump_raw_trajs(icao: str, ds: Opensky_DataStorage):
    runways_order = load_airport_info(icao)['runways_order']
    features = ['x', 'y', 'altitude', 'speed']

    # #

    # data = []
    # for c in ds.storage.keys():
    #     s = ds.storage[c]

    #     _d = {f: s[f] for f in features}

    #     _drop = False

    #     rwy_ori = None
    #     for l in s['rwy_list']:
    #         if rwy_ori is None:
    #             rwy_ori = l['rwy_ori']
    #         if rwy_ori != l['rwy_ori']:
    #             _drop = True
    #             break

    #     if _drop:
    #         continue

    #     _d['rwy_ori'] = rwy_ori
    #     data.append(_d)

    # #

    # plot_raw_trajs(data, runways_order, f'./trajs.png')

    # --- #

    tail = 300

    data = []
    for c in ds.storage.keys():
        s = ds.storage[c]

        # _d = {f: s[f] for f in features}
        _d = {f: s[f][-tail:] for f in features}

        _drop = False

        rwy_ori = None
        for l in s['rwy_list']:
            if rwy_ori is None:
                rwy_ori = l['rwy_ori']
            if rwy_ori != l['rwy_ori']:
                _drop = True
                break

        if _drop:
            continue

        _d['rwy_ori'] = rwy_ori
        data.append(_d)

    #

    plot_raw_trajs2(data, runways_order, f'./trajs-{tail}.png')

    return


def main():
    icao = "RJTT"
    data_folder = "./opensky_save/RJTT/2024-07-24_2024-07-31/"
    only_ifr = False

    ds = Opensky_DataStorage(icao, only_ifr)
    ds.load(data_folder)

    dump_raw_trajs(icao, ds)

    print("DONE")
    return


if __name__ == '__main__':
    main()
