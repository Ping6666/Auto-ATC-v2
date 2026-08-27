import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

from typing import Dict, List
from argparse import ArgumentParser, Namespace

from tqdm import tqdm
from matplotlib.axes._axes import Axes
from matplotlib.text import Annotation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from core.utils import mkdir, load_json
from core.fms import np_get_xy, np_get_latlong
from core.storage.utils import load_airport_info, get_callsigns_state, get_callsigns_info
from common.const import FIGSIZE, FIG_PARAMS

plt.rcParams.update(FIG_PARAMS)


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--folder", required=True)
    parser.add_argument("--save-folder", required=True)

    parser.add_argument("--icao", required=True)

    parser.add_argument("--map-zoom", default=12, type=int)
    parser.add_argument("--map", action="store_true")

    parser.add_argument("--last-frame", default=10, type=int)
    parser.add_argument("--fps", default=30, type=int)
    parser.add_argument("--dpi", default=150, type=int)

    args = parser.parse_args()
    return args


# --- #


def get_lim(ori_lim, data_max, data_min, range_ratio):
    _min, _max = data_min, data_max
    if ori_lim is not None:
        _max = ori_lim[1]
        _min = ori_lim[0]

    _range = (_max - _min) * range_ratio
    new_min, new_max = _min - abs(_range), _max + abs(_range)
    return new_min, new_max


def plot_game_animate(
    last_frame: int,
    list_data: List[Dict[str, Dict[str, float | str]]],
    airport_info: Dict,
    #
    fps: int,
    dpi: int,
    title_label: str,
    xlabel: str,
    ylabel: str,
    savefig_fname: str,
):
    ax: Axes
    annotations: List[Annotation]

    range_ratio = 0.025
    annotations = []

    max_annotations = 20
    annotations_vacancy = [True for _ in range(max_annotations)]
    annotations_dict = {}
    _x_base = 0.03
    _y_base = 0.94
    _y_shift = -0.06

    _bbox = dict(boxstyle='round', fc='gray')
    _arrowprops = dict(
        arrowstyle="->",
        connectionstyle="angle,angleA=0,angleB=90,rad=10",
    )

    xs, ys, alts = [], [], []
    data_in_sec = []
    text_in_sec = []

    total, land, collide, leave = 0, 0, 0, 0
    callsigns = set()
    for data in list_data:
        _data_in_sec = []

        for k, v in data.items():
            xs.append(v['x'])
            ys.append(v['y'])
            alts.append(v['altitude'])

            _info = v.get('info')
            if _info is not None:
                _info = f"{k} {_info}"

                if 'land' in _info:
                    land += 1
                elif 'leave' in _info:
                    leave += 1
                elif 'lost' in _info:
                    collide += 1

            _data_in_sec.append((
                v['x'],
                v['y'],
                v['altitude'],
                _info,
            ))

            callsigns.add(k)

        data_in_sec.append(_data_in_sec)

        total = len(callsigns)
        _text = (f"  total: {total:>5}\n"
                 f"   land: {land:>5}\n"
                 f"collide: {collide:>5}\n"
                 f"  leave: {leave:>5}")
        text_in_sec.append(_text)

    assert len(data_in_sec) != 0

    fig = plt.figure(figsize=FIGSIZE)
    _suptitle = plt.suptitle(title_label, fontsize=20)

    ax = plt.subplot()

    ref_pos = airport_info['position']
    scale_bar = {
        'point1': [35.55999, 139.76907],
        'point2': [35.53660, 139.78567],
        'text': '3.0 km',
    }

    scale_bar_x1, scale_bar_y1 = np_get_xy(scale_bar['point1'][0],
                                           scale_bar['point1'][1], ref_pos)
    scale_bar_x2, scale_bar_y2 = np_get_xy(scale_bar['point2'][0],
                                           scale_bar['point2'][1], ref_pos)

    for _, rwy in airport_info['RAW']['runways'].items():
        x1, y1 = np_get_xy(rwy['this'][0], rwy['this'][1], ref_pos)
        x2, y2 = np_get_xy(rwy['other'][0], rwy['other'][1], ref_pos)
        ax.plot([x1, x2], [y1, y2], color='gray', linewidth=2, zorder=1)

    alt_lim = get_lim(None, np.max(alts), np.min(alts), range_ratio)
    co = ax.scatter(
        [],
        [],
        c=[],
        cmap='jet',
        vmin=alt_lim[0],
        vmax=alt_lim[1],
        zorder=3,
    )
    plt.colorbar(co, ax=ax, label="Altitude (ft)")

    te = ax.text(
        0.98,
        0.98,
        '',
        ha='right',
        va='top',
        transform=ax.transAxes,
        fontfamily='monospace',
    )

    def init():
        _suptitle.set_text(f'{title_label} init')

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        x_lim = get_lim(None, np.max(xs), np.min(xs), range_ratio)
        ax.set_xlim(*x_lim)

        y_lim = get_lim(None, np.max(ys), np.min(ys), range_ratio)
        ax.set_ylim(*y_lim)

        scale_bar_length = np.sqrt((scale_bar_x1 - scale_bar_x2)**2 +
                                   (scale_bar_y1 - scale_bar_y2)**2)

        y_shift = (y_lim[1] - y_lim[0])
        scale_bar_x = x_lim[0] + 0.05 * (x_lim[1] - x_lim[0])
        scale_bar_y = y_lim[0] + 0.05 * y_shift

        ax.hlines(
            y=scale_bar_y,
            xmin=scale_bar_x,
            xmax=scale_bar_x + scale_bar_length,
            colors='m',
            linewidth=2,
        )

        ax.text(
            scale_bar_x + scale_bar_length / 2,
            scale_bar_y + 0.025 * y_shift,
            scale_bar['text'],
            color='m',
            ha='center',
        )

        plt.tight_layout()
        return

    def update(idx: int):
        """
        Args:
            idx: curr. frame idx

        """

        _suptitle.set_text(f'{title_label} {idx:05d}')

        for _annotation in annotations:
            _annotation.remove()
        annotations.clear()

        _xs = []
        _ys = []
        _cs = []

        _pending_annotations = []

        _first_frame = max(0, idx - last_frame + 1)
        for i in range(_first_frame, idx + 1):
            for _data in data_in_sec[i]:
                __x = _data[0]
                __y = _data[1]
                __c = _data[2]
                __info = _data[3]

                _xs.append(__x)
                _ys.append(__y)
                _cs.append(__c)

                if __info is not None:
                    _pending_annotations.append(((__x, __y), __info))

        old_keys = list(annotations_dict.keys())
        new_keys = [_p[-1] for _p in _pending_annotations]

        for k in old_keys:
            if k not in new_keys:
                old_idx = annotations_dict.pop(k)
                annotations_vacancy[old_idx] = True

        old_keys = list(annotations_dict.keys())
        for _p in _pending_annotations:
            _point, _info = _p

            new_idx = -1
            if _info in old_keys:
                new_idx = annotations_dict[_info]

            else:
                for i in range(max_annotations):
                    if annotations_vacancy[i] == True:
                        new_idx = i
                        break

                if new_idx != -1:
                    annotations_vacancy[new_idx] = False
                    annotations_dict[_info] = new_idx

                else:
                    print(f"{_info = }")
                    print(f"{_point = }")
                    print(f"{annotations_vacancy = }")
                    print(f"{annotations_dict = }")
                    print()

            if new_idx != -1:
                _annotation = ax.annotate(
                    _info,
                    _point,
                    xycoords='data',
                    xytext=(_x_base, _y_base + _y_shift * new_idx),
                    textcoords='axes fraction',
                    bbox=_bbox,
                    arrowprops=_arrowprops,
                    fontsize=15,
                    ha='left',
                    va='top',
                    clip_on=True,
                )
                annotations.append(_annotation)

        co.set_offsets(np.array([_xs, _ys]).T)
        co.set_array(_cs)

        te.set_text(text_in_sec[idx])
        return

    kwargs = {
        'frames': tqdm(range(len(list_data)), file=sys.stdout),
        'init_func': init,
        'blit': False,
    }
    _ani = animation.FuncAnimation(fig, update, **kwargs)
    _writer = animation.FFMpegWriter(fps=fps)

    _ani.save(savefig_fname, writer=_writer, dpi=dpi)
    plt.close('all')

    print(f"plot_game_animate: {savefig_fname} SAVED!")
    return


def plot_game_animate_map(
    last_frame: int,
    list_data: List[Dict[str, Dict[str, float | str]]],
    airport_info: Dict,
    #
    fps: int,
    dpi: int,
    map_zoom: int,
    title_label: str,
    savefig_fname: str,
):
    import cartopy.crs as ccrs
    from cartopy.io.img_tiles import OSM

    annotations: List[Annotation]

    annotations = []

    max_annotations = 20
    annotations_vacancy = [True for _ in range(max_annotations)]
    annotations_dict = {}
    _x_base = 0.0175
    _y_base = 0.975
    _y_shift = -0.075

    _bbox = dict(boxstyle='round', fc='gray')
    _arrowprops = dict(
        arrowstyle="->",
        connectionstyle="angle,angleA=0,angleB=90,rad=10",
    )

    ref_pos = airport_info['position']
    data_crs = ccrs.PlateCarree()

    alts = []
    lats, longs = [], []
    data_in_sec = []
    text_in_sec = []

    total, land, collide, leave = 0, 0, 0, 0
    callsigns = set()
    for data in list_data:
        _data_in_sec = []

        for k, v in data.items():
            x = v['x']
            y = v['y']
            alt = v['altitude']
            lat, long = np_get_latlong(
                np.array([x]),
                np.array([y]),
                ref_pos,
            )
            lat = lat[0]
            long = long[0]

            alts.append(alt)
            lats.append(lat)
            longs.append(long)

            _info = v.get('info')
            if _info is not None:
                _info = f"{k} {_info}"

                if 'land' in _info:
                    land += 1
                elif 'leave' in _info:
                    leave += 1
                elif 'lost' in _info:
                    collide += 1

            _data_in_sec.append((
                long,
                lat,
                alt,
                _info,
            ))

            callsigns.add(k)

        data_in_sec.append(_data_in_sec)

        total = len(callsigns)
        _text = (f"  total: {total:>5}\n"
                 f"   land: {land:>5}\n"
                 f"collide: {collide:>5}\n"
                 f"  leave: {leave:>5}")
        text_in_sec.append(_text)

    assert len(data_in_sec) != 0

    frame_longs = []
    frame_lats = []
    frame_alts = []
    frame_annotations = []
    for idx in range(len(data_in_sec)):
        _longs = []
        _lats = []
        _cs = []
        _pending_annotations = []

        _first_frame = max(0, idx - last_frame + 1)
        for i in range(_first_frame, idx + 1):
            for _data in data_in_sec[i]:
                __long = _data[0]
                __lat = _data[1]
                __c = _data[2]
                __info = _data[3]

                _longs.append(__long)
                _lats.append(__lat)
                _cs.append(__c)

                if __info is not None:
                    _pending_annotations.append(((__long, __lat), __info))

        frame_longs.append(_longs)
        frame_lats.append(_lats)
        frame_alts.append(_cs)
        frame_annotations.append(_pending_annotations)

    runway_lats = []
    runway_longs = []
    runway_segments = []
    runway_segment_keys = set()
    for _, rwy in airport_info['RAW']['runways'].items():
        runway_lats.extend([rwy['this'][0], rwy['other'][0]])
        runway_longs.extend([rwy['this'][1], rwy['other'][1]])

        p1 = tuple(rwy['this'])
        p2 = tuple(rwy['other'])
        key = tuple(sorted([p1, p2]))
        if key in runway_segment_keys:
            continue
        runway_segment_keys.add(key)
        runway_segments.append((p1, p2))

    all_lat = np.concatenate([
        np.array(lats).reshape(-1),
        np.array(runway_lats).reshape(-1),
    ])
    all_long = np.concatenate([
        np.array(longs).reshape(-1),
        np.array(runway_longs).reshape(-1),
    ])

    lon_margin = 0.01
    lat_margin = 0.01

    lon_min = np.nanmin(all_long) - lon_margin
    lon_max = np.nanmax(all_long) + lon_margin
    lat_min = np.nanmin(all_lat) - lat_margin
    lat_max = np.nanmax(all_lat) + lat_margin

    tile = OSM(cache=True)
    fig_bg = plt.figure(figsize=FIGSIZE)
    fig_bg.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax_bg = plt.axes([0, 0, 1, 1], projection=data_crs)
    ax_bg.set_extent(
        [lon_min, lon_max, lat_min, lat_max],
        crs=data_crs,
    )
    ax_bg.set_aspect('auto')
    ax_bg.add_image(tile, map_zoom)

    for p1, p2 in runway_segments:
        ax_bg.plot(
            [p1[1], p2[1]],
            [p1[0], p2[0]],
            color='gray',
            linewidth=2,
            transform=data_crs,
            zorder=1,
        )

    ax_bg.set_axis_off()
    fig_bg.canvas.draw()
    map_img = np.asarray(fig_bg.canvas.buffer_rgba()).copy()

    map_height, map_width = map_img.shape[:2]

    def to_pixel(_longs, _lats):
        _longs = np.asarray(_longs, dtype=float)
        _lats = np.asarray(_lats, dtype=float)
        if len(_longs) == 0:
            return [], []

        pts = np.stack([_longs, _lats], axis=-1)
        pix = data_crs._as_mpl_transform(ax_bg).transform(pts)
        return pix[:, 0], pix[:, 1]

    frame_xs = []
    frame_ys = []
    frame_pixel_annotations = []
    for _longs, _lats, _annotations in zip(
            frame_longs,
            frame_lats,
            frame_annotations,
    ):
        _xs, _ys = to_pixel(_longs, _lats)
        frame_xs.append(_xs)
        frame_ys.append(_ys)

        _pixel_annotations = []
        for _point, _info in _annotations:
            _px, _py = to_pixel([_point[0]], [_point[1]])
            _pixel_annotations.append(((_px[0], _py[0]), _info))
        frame_pixel_annotations.append(_pixel_annotations)

    lon_ticks = np.linspace(lon_min, lon_max, 5)
    lat_ticks = np.linspace(lat_min, lat_max, 5)

    x_ticks, _ = to_pixel(lon_ticks, np.full_like(lon_ticks, lat_min))
    _, y_ticks = to_pixel(np.full_like(lat_ticks, lon_min), lat_ticks)

    plt.close(fig_bg)

    fig, ax = plt.subplots(figsize=FIGSIZE)
    _suptitle = plt.suptitle(title_label, fontsize=20)
    _suptitle.set_animated(True)

    ax.imshow(
        map_img,
        extent=[0, map_width, 0, map_height],
        origin='upper',
        aspect='auto',
        zorder=0,
    )
    ax.set_xlim(0, map_width)
    ax.set_ylim(0, map_height)

    alt_lim = get_lim(None, np.max(alts), np.min(alts), 0.025)
    co = ax.scatter(
        [],
        [],
        c=[],
        cmap='jet',
        vmin=alt_lim[0],
        vmax=alt_lim[1],
        zorder=3,
    )
    co.set_animated(True)
    plt.colorbar(co, ax=ax, label="Altitude (ft)")

    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    ax.set_xticklabels([f"{v:.3f}" for v in lon_ticks])
    ax.set_yticklabels([f"{v:.3f}" for v in lat_ticks])

    ax.tick_params(
        axis='both',
        which='major',
        labelsize=plt.rcParams.get("xtick.labelsize", None),
    )

    te = ax.text(
        0.98,
        0.98,
        '',
        ha='right',
        va='top',
        transform=ax.transAxes,
        fontfamily='monospace',
    )
    te.set_animated(True)

    plt.tight_layout()

    def init():
        return [_suptitle, co, te]

    def update(idx: int):
        """
        Args:
            idx: curr. frame idx

        """

        _suptitle.set_text(f'{title_label} {idx:05d}')

        for _annotation in annotations:
            _annotation.remove()
        annotations.clear()

        _xs = frame_xs[idx]
        _ys = frame_ys[idx]
        _cs = frame_alts[idx]
        _pending_annotations = frame_pixel_annotations[idx]

        old_keys = list(annotations_dict.keys())
        new_keys = [_p[-1] for _p in _pending_annotations]

        for k in old_keys:
            if k not in new_keys:
                old_idx = annotations_dict.pop(k)
                annotations_vacancy[old_idx] = True

        old_keys = list(annotations_dict.keys())
        for _p in _pending_annotations:
            _point, _info = _p

            new_idx = -1
            if _info in old_keys:
                new_idx = annotations_dict[_info]

            else:
                for i in range(max_annotations):
                    if annotations_vacancy[i] == True:
                        new_idx = i
                        break

                if new_idx != -1:
                    annotations_vacancy[new_idx] = False
                    annotations_dict[_info] = new_idx

                else:
                    print(f"{_info = }")
                    print(f"{_point = }")
                    print(f"{annotations_vacancy = }")
                    print(f"{annotations_dict = }")
                    print()

            if new_idx != -1:
                _annotation = ax.annotate(
                    _info,
                    _point,
                    xycoords='data',
                    xytext=(_x_base, _y_base + _y_shift * new_idx),
                    textcoords='axes fraction',
                    bbox=_bbox,
                    arrowprops=_arrowprops,
                    fontsize=15,
                    ha='left',
                    va='top',
                    clip_on=True,
                )
                _annotation.set_animated(True)
                annotations.append(_annotation)

        co.set_offsets(np.array([_xs, _ys]).T)
        co.set_array(_cs)

        te.set_text(text_in_sec[idx])
        return [_suptitle, co, te] + annotations

    kwargs = {
        'frames': tqdm(range(len(list_data)), file=sys.stdout),
        'init_func': init,
        'blit': True,
    }
    _ani = animation.FuncAnimation(fig, update, **kwargs)
    _writer = animation.FFMpegWriter(fps=fps)

    _ani.save(savefig_fname, writer=_writer, dpi=dpi)
    plt.close('all')

    print(f"plot_game_animate_map: {savefig_fname} SAVED!")
    return


# --- #


def get_packed_records(folder: str, airport_info: Dict):
    states = load_json(f"{folder}/tape/state.json")
    actions = load_json(f"{folder}/tape/action.json")
    infos = load_json(f"{folder}/tape/info.json")

    #

    callsigns = set()
    packed_records: List[Dict] = []

    for _state, _, _info in zip(states, actions, infos):
        state = get_callsigns_state(_state, airport_info)
        callsigns.update(state.keys())

        info = get_callsigns_info(_info, callsigns)

        for k, v in info.items():
            try:
                for i in range(len(packed_records)):
                    ii = i + 1
                    if k in packed_records[-ii].keys():
                        packed_records[-ii][k]['info'] = '/'.join(v)
                        break

            except Exception as e:
                print(f"{e = }")
                print(f"{k = } {v = }")
                print()
                pass

        packed_records.append(state)

    # packed_records = packed_records[1500:2500]
    return packed_records


def main(args):
    print(f"{args = }")

    last_frame = args.last_frame
    fps = args.fps
    dpi = args.dpi

    icao = args.icao

    folder = args.folder
    save_folder = args.save_folder

    mkdir(save_folder, can_exists=True)

    save_name = str(Path(folder).name)
    if save_name == '':
        save_name = str(Path(folder).parent.name)

    airport_info = load_airport_info(icao, get_raw=True)

    packed_records = get_packed_records(folder, airport_info)
    if args.map:
        plot_game_animate_map(
            last_frame,
            packed_records,
            airport_info,
            #
            fps,
            dpi,
            args.map_zoom,
            f'{save_name} Game Records',
            f'{save_folder}/{save_name}_game-traj-ani-map.mp4',
        )
    else:
        plot_game_animate(
            last_frame,
            packed_records,
            airport_info,
            #
            fps,
            dpi,
            f'{save_name} Game Records',
            'X (meter)',
            'Y (meter)',
            f'{save_folder}/{save_name}_game-traj-ani.mp4',
        )

    print("DONE")
    return


"""
Generates an animated video for the entire interaction experiment, with support
for multiple games.

usage:
    animate_traj.py [-h] [--last-frame LAST_FRAME] [--fps FPS] [--dpi DPI]
                    [--map] [--map-zoom MAP_ZOOM]
                    --folder FOLDER --save-folder SAVE_FOLDER
"""
if __name__ == '__main__':
    args = get_args()
    main(args)
