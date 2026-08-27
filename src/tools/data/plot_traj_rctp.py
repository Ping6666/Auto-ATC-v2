import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

from typing import Dict, List
from argparse import ArgumentParser, Namespace

import numpy as np
import matplotlib.pyplot as plt

from core.utils import mkdir
from core.storage import Opensky_DataStorage
from core.storage.utils import load_airport_info
from core.fms import np_get_xy, np_get_latlong
from common.const import FIGSIZE, FIGDPI, FIG_PARAMS

plt.rcParams.update(FIG_PARAMS)

MAP_BACKGROUND_CACHE = {}


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument('--icao')
    parser.add_argument('--only-ifr', action='store_true')

    parser.add_argument('--data-folder')
    parser.add_argument('--save-folder')

    parser.add_argument('--map', action='store_true')
    parser.add_argument('--map-zoom', default=12, type=int)

    args = parser.parse_args()
    return args


def get_plot_lim(data, margin_ratio: float = 0.05):
    if len(data) == 0:
        return None, None

    all_x = np.concatenate([d['x'].reshape(-1) for d in data])
    all_y = np.concatenate([d['y'].reshape(-1) for d in data])

    x_min, x_max = np.nanmin(all_x), np.nanmax(all_x)
    y_min, y_max = np.nanmin(all_y), np.nanmax(all_y)

    x_margin = max((x_max - x_min) * margin_ratio, 1.0)
    y_margin = max((y_max - y_min) * margin_ratio, 1.0)

    x_lim = (x_min - x_margin, x_max + x_margin)
    y_lim = (y_min - y_margin, y_max + y_margin)
    return x_lim, y_lim


def get_single_runway_data(ds: Opensky_DataStorage, features: List):
    data = []
    for c in ds.storage.keys():
        s = ds.storage[c]

        d = {f: s[f] for f in features}

        drop = False
        rwy_ori = None
        for l in s['rwy_list']:
            if rwy_ori is None:
                rwy_ori = l['rwy_ori']
            if rwy_ori != l['rwy_ori']:
                drop = True
                break

        if drop:
            continue

        d['rwy_ori'] = rwy_ori
        data.append((c, d))

    return data


def plot_raw_trajs(data, runways_order: List, savefig_fname: str):
    # ['05L', '23R', '05R', '23L']
    sc = ['g', 'b', 'r', 'y']

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
        # N25d04m39.83 E121d13m58.16
        25.08027,
        121.23222,
        0,
    ]
    scale_bar = {
        'point1': [25.07289, 121.21598],
        'point2': [25.09449, 121.24344],
        'text': '3.66 km',
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


def plot_raw_trajs_map(
    data,
    runways_order: List,
    airport_info: Dict,
    map_zoom: int,
    savefig_fname: str,
    x_lim=None,
    y_lim=None,
):
    import cartopy.crs as ccrs
    from cartopy.io.img_tiles import OSM

    # ['05L', '23R', '05R', '23L']
    sc = ['g', 'b', 'r', 'y']

    figsize = (7, 5.5)
    data_crs = ccrs.PlateCarree()
    ref_pos = airport_info['position']
    scale_bar = {
        'point1': [25.07289, 121.21598],
        'point2': [25.09449, 121.24344],
        'text': '3.66 km',
    }

    if x_lim is None or y_lim is None:
        all_lat = []
        all_long = []
        for ds in data:
            lat, long = np_get_latlong(ds['x'], ds['y'], ref_pos)
            all_lat.append(lat.reshape(-1))
            all_long.append(long.reshape(-1))

        if len(all_lat) == 0:
            all_lat = np.array([ref_pos[0]])
            all_long = np.array([ref_pos[1]])
        else:
            all_lat = np.concatenate(all_lat)
            all_long = np.concatenate(all_long)

        lon_margin = 0.01
        lat_margin = 0.01

        lon_min = np.nanmin(all_long) - lon_margin
        lon_max = np.nanmax(all_long) + lon_margin
        lat_min = np.nanmin(all_lat) - lat_margin
        lat_max = np.nanmax(all_lat) + lat_margin

    else:
        x = np.array([x_lim[0], x_lim[1], x_lim[0], x_lim[1]])
        y = np.array([y_lim[0], y_lim[0], y_lim[1], y_lim[1]])
        all_lat, all_long = np_get_latlong(x, y, ref_pos)

        lon_min = np.nanmin(all_long)
        lon_max = np.nanmax(all_long)
        lat_min = np.nanmin(all_lat)
        lat_max = np.nanmax(all_lat)

    map_cache_key = (
        map_zoom,
        figsize,
        round(lon_min, 7),
        round(lon_max, 7),
        round(lat_min, 7),
        round(lat_max, 7),
    )
    if map_cache_key in MAP_BACKGROUND_CACHE:
        map_img = MAP_BACKGROUND_CACHE[map_cache_key]
    else:
        tile = OSM(cache=True)
        fig_bg = plt.figure(figsize=figsize)
        fig_bg.subplots_adjust(left=0, right=1, bottom=0, top=1)
        ax_bg = plt.axes([0, 0, 1, 1], projection=data_crs)
        ax_bg.set_extent(
            [lon_min, lon_max, lat_min, lat_max],
            crs=data_crs,
        )
        ax_bg.set_aspect('auto')
        ax_bg.add_image(tile, map_zoom)
        ax_bg.set_axis_off()
        fig_bg.canvas.draw()
        map_img = np.asarray(fig_bg.canvas.buffer_rgba()).copy()
        plt.close(fig_bg)
        MAP_BACKGROUND_CACHE[map_cache_key] = map_img

    map_height, map_width = map_img.shape[:2]

    def to_pixel(_longs, _lats):
        _longs = np.asarray(_longs, dtype=float)
        _lats = np.asarray(_lats, dtype=float)
        if len(_longs) == 0:
            return [], []

        xs = (_longs - lon_min) / (lon_max - lon_min) * map_width
        ys = (_lats - lat_min) / (lat_max - lat_min) * map_height
        return xs, ys

    plot_data = []
    labeled_rwy = set()

    for ds in data:
        lat, long = np_get_latlong(ds['x'], ds['y'], ref_pos)
        rwy = ds['rwy_ori']
        _sc = sc[runways_order.index(rwy)]

        if rwy in labeled_rwy:
            rwy = None
        else:
            labeled_rwy.add(rwy)

        xs, ys = to_pixel(long, lat)
        plot_data.append((xs, ys, _sc, rwy))

    lon_ticks = np.linspace(lon_min, lon_max, 5)
    lat_ticks = np.linspace(lat_min, lat_max, 5)

    x_ticks, _ = to_pixel(lon_ticks, np.full_like(lon_ticks, lat_min))
    _, y_ticks = to_pixel(np.full_like(lat_ticks, lon_min), lat_ticks)

    scale_bar_x1, scale_bar_y1 = np_get_xy(scale_bar['point1'][0],
                                           scale_bar['point1'][1], ref_pos)
    scale_bar_x2, scale_bar_y2 = np_get_xy(scale_bar['point2'][0],
                                           scale_bar['point2'][1], ref_pos)
    scale_bar_length = np.sqrt((scale_bar_x1 - scale_bar_x2)**2 +
                               (scale_bar_y1 - scale_bar_y2)**2)

    x_extent, _ = np_get_xy(
        np.array([ref_pos[0], ref_pos[0]]),
        np.array([lon_min, lon_max]),
        ref_pos,
    )
    x_range = max(abs(x_extent[1] - x_extent[0]), 1.0)
    scale_bar_length_px = scale_bar_length / x_range * map_width
    scale_bar_length_px = min(scale_bar_length_px, map_width * 0.30)

    scale_bar_x = map_width * 0.60
    scale_bar_y = map_height * 0.07
    scale_bar_text_x = scale_bar_x + scale_bar_length_px / 2
    scale_bar_text_y = scale_bar_y + map_height * 0.025

    fig, ax = plt.subplots(figsize=figsize)
    ax.imshow(
        map_img,
        extent=[0, map_width, 0, map_height],
        origin='upper',
        aspect='auto',
        zorder=0,
    )
    ax.set_xlim(0, map_width)
    ax.set_ylim(0, map_height)

    for xs, ys, _sc, rwy in plot_data:
        ax.plot(xs, ys, _sc, label=rwy, linewidth=1.25, zorder=2)

    plt.legend()

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    ax.set_xticklabels([f'{v:.3f}' for v in lon_ticks])
    ax.set_yticklabels([f'{v:.3f}' for v in lat_ticks])

    ax.tick_params(
        axis='both',
        which='major',
        labelsize=plt.rcParams.get('xtick.labelsize', None),
    )

    ax.plot(
        [scale_bar_x, scale_bar_x + scale_bar_length_px],
        [scale_bar_y, scale_bar_y],
        color='m',
        linewidth=2,
        zorder=3,
    )

    ax.text(
        scale_bar_text_x,
        scale_bar_text_y,
        scale_bar['text'],
        color='m',
        ha='center',
        va='bottom',
        zorder=3,
    )

    plt.tight_layout()
    plt.savefig(savefig_fname, dpi=FIGDPI)
    plt.close('all')

    print(f"plot_raw_trajs_map: {savefig_fname} SAVED!")
    return


def plot_raw_trajs2_map(
    data,
    runways_order: List,
    airport_info: Dict,
    map_zoom: int,
    savefig_fname: str,
):
    plot_raw_trajs_map(
        data,
        runways_order,
        airport_info,
        map_zoom,
        savefig_fname,
        x_lim=(-31000, 31000),
        y_lim=(-31000, 31000),
    )
    return


def plot_raw_trajs2(data, runways_order: List, savefig_fname: str):
    # ['05L', '23R', '05R', '23L']
    sc = ['g', 'b', 'r', 'y']

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

    ax.set_xlim((-31000, 31000))
    ax.set_ylim((-31000, 31000))

    #

    plt.tight_layout()
    plt.savefig(savefig_fname, dpi=FIGDPI)
    plt.close('all')

    print(f"plot_raw_trajs: {savefig_fname} SAVED!")
    return


def dump_raw_trajs(
    icao: str,
    ds: Opensky_DataStorage,
    save_folder: str,
    use_map: bool,
    map_zoom: int,
):
    mkdir(save_folder, can_exists=True)

    airport_info = load_airport_info(icao)
    runways_order = airport_info['runways_order']
    features = ['x', 'y', 'altitude', 'speed']
    flight_data = get_single_runway_data(ds, features)
    all_flight_data = [d for _, d in flight_data]
    map_x_lim, map_y_lim = get_plot_lim(all_flight_data)

    data = all_flight_data

    if use_map:
        plot_raw_trajs_map(
            data,
            runways_order,
            airport_info,
            map_zoom,
            f'{save_folder}/trajs-map.png',
            x_lim=map_x_lim,
            y_lim=map_y_lim,
        )
    else:
        plot_raw_trajs(data, runways_order, f'{save_folder}/trajs.png')

    # --- #

    for tgt_rwy in runways_order:
        data = [d for _, d in flight_data if d['rwy_ori'] == tgt_rwy]

        if use_map:
            plot_raw_trajs_map(
                data,
                runways_order,
                airport_info,
                map_zoom,
                f'{save_folder}/trajs-{tgt_rwy}-map.png',
                x_lim=map_x_lim,
                y_lim=map_y_lim,
            )
        else:
            plot_raw_trajs(
                data,
                runways_order,
                f'{save_folder}/trajs-{tgt_rwy}.png',
            )

    # --- #

    for tail in range(100, 2100, 100):
        data = []
        for _, d in flight_data:
            tail_d = {f: d[f][-tail:] for f in features}
            tail_d['rwy_ori'] = d['rwy_ori']
            data.append(tail_d)

        if use_map:
            plot_raw_trajs2_map(
                data,
                runways_order,
                airport_info,
                map_zoom,
                f'{save_folder}/trajs-{tail}-map.png',
            )
        else:
            plot_raw_trajs2(
                data,
                runways_order,
                f'{save_folder}/trajs-{tail}.png',
            )

    # --- #

    mkdir(f'{save_folder}/flights', can_exists=True)
    for c, _d in flight_data:
        _c = c.replace('\n', '_')

        if use_map:
            plot_raw_trajs_map(
                [_d],
                runways_order,
                airport_info,
                map_zoom,
                f'{save_folder}/flights/trajs-{_c}-map.png',
                x_lim=map_x_lim,
                y_lim=map_y_lim,
            )
        else:
            plot_raw_trajs(
                [_d],
                runways_order,
                f'{save_folder}/flights/trajs-{_c}.png',
            )
    return


def main():
    args = get_args()

    ds = Opensky_DataStorage(args.icao, args.only_ifr)
    ds.load(args.data_folder)

    dump_raw_trajs(args.icao, ds, args.save_folder, args.map, args.map_zoom)

    print("DONE")
    return


if __name__ == '__main__':
    main()
