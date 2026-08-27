import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

from cartopy.io.img_tiles import OSM
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from core.utils import load_pkl, load_npy
from core.fms import np_get_xy, np_get_latlong
from common.const import FIGSIZE, FIGDPI, FIG_PARAMS

plt.rcParams.update(FIG_PARAMS)


def plot_traj(x, y, c, fp, savefig_fname: str):
    figsize = (7, 5.5)
    plt.subplots(figsize=figsize)

    plt.plot(
        fp[..., 1],
        fp[..., 0],
        'g--',
        linewidth=1.25,
        # label='Commanded path',
        label='Target waypoints',
    )

    scatter = plt.scatter(
        x,
        y,
        c=c,
        s=20,
        cmap='jet',
        # label='Executed flight path',
        label='Actual trajectory',
    )
    plt.colorbar(scatter, label="Altitude (ft)")

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
    scale_bar_x = x_lim[0] + 0.90 * (x_lim[1] - x_lim[0])
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


def plot_traj_map(x, y, c, fp, savefig_fname: str):
    figsize = (7, 5.5)

    ref_pos = [
        35.55333,
        139.78111,
        0,
    ]

    tile = OSM(cache=True)
    data_crs = ccrs.PlateCarree()

    fig, ax = plt.subplots(
        figsize=figsize,
        subplot_kw={
            'projection': tile.crs,
        },
    )

    lat, long = np_get_latlong(x, y, ref_pos)
    fp_lat, fp_long = np_get_latlong(fp[..., 1], fp[..., 0], ref_pos)

    all_lat = np.concatenate([lat.reshape(-1), fp_lat.reshape(-1)])
    all_long = np.concatenate([long.reshape(-1), fp_long.reshape(-1)])

    lon_margin = 0.01
    lat_margin = 0.01

    lon_min = np.nanmin(all_long) - lon_margin
    lon_max = np.nanmax(all_long) + lon_margin
    lat_min = np.nanmin(all_lat) - lat_margin
    lat_max = np.nanmax(all_lat) + lat_margin

    ax.set_extent(
        [lon_min, lon_max, lat_min, lat_max],
        crs=data_crs,
    )

    ax.add_image(tile, 13)

    ax.plot(
        fp_long,
        fp_lat,
        'g--',
        linewidth=1.25,
        label='Target waypoints',
        transform=data_crs,
    )

    scatter = ax.scatter(
        long,
        lat,
        c=c,
        s=20,
        cmap='jet',
        label='Actual trajectory',
        transform=data_crs,
    )

    plt.colorbar(scatter, ax=ax, label="Altitude (ft)")

    plt.legend()

    # ------------------------------------------------------------
    # Keep the same map layout, but show x/y axis values as lon/lat
    # ------------------------------------------------------------
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    lon_ticks = np.linspace(lon_min, lon_max, 5)
    lat_ticks = np.linspace(lat_min, lat_max, 5)

    ax.set_xticks(lon_ticks, crs=data_crs)
    ax.set_yticks(lat_ticks, crs=data_crs)

    ax.set_xticklabels([f"{v:.3f}" for v in lon_ticks])
    ax.set_yticklabels([f"{v:.3f}" for v in lat_ticks])

    ax.tick_params(
        axis='both',
        which='major',
        labelsize=plt.rcParams.get("xtick.labelsize", None),
    )

    # ------------------------------------------------------------
    # Scale bar
    # ------------------------------------------------------------
    scale_bar = {
        'point1': [35.55999, 139.76907],
        'point2': [35.53660, 139.78567],
        'text': '3.0 km',
    }

    scale_bar_x1, scale_bar_y1 = np_get_xy(
        scale_bar['point1'][0],
        scale_bar['point1'][1],
        ref_pos,
    )
    scale_bar_x2, scale_bar_y2 = np_get_xy(
        scale_bar['point2'][0],
        scale_bar['point2'][1],
        ref_pos,
    )

    scale_bar_length = np.sqrt((scale_bar_x1 - scale_bar_x2)**2 +
                               (scale_bar_y1 - scale_bar_y2)**2)

    x_lim = ax.get_xlim()
    y_lim = ax.get_ylim()

    y_shift = y_lim[1] - y_lim[0]
    scale_bar_x = x_lim[0] + 0.75 * (x_lim[1] - x_lim[0])
    scale_bar_y = y_lim[0] + 0.05 * y_shift

    scale_bar_lat, scale_bar_long = np_get_latlong(
        np.array([scale_bar_x, scale_bar_x + scale_bar_length]),
        np.array([scale_bar_y, scale_bar_y]),
        ref_pos,
    )

    ax.plot(
        scale_bar_long,
        scale_bar_lat,
        color='m',
        linewidth=2,
        transform=data_crs,
    )

    scale_bar_text_lat, scale_bar_text_long = np_get_latlong(
        np.array([scale_bar_x + scale_bar_length / 2]),
        np.array([scale_bar_y + 0.025 * y_shift]),
        ref_pos,
    )

    ax.text(
        scale_bar_text_long[0],
        scale_bar_text_lat[0],
        scale_bar['text'],
        color='m',
        ha='center',
        transform=data_crs,
    )

    plt.tight_layout()
    plt.savefig(savefig_fname, dpi=FIGDPI)
    plt.close('all')

    print(f"plot_traj_map: {savefig_fname} SAVED!")
    return


def main():
    folder = ""
    take_idx = -1

    plot_dataset = load_pkl(f"{folder}/sample/plot_dataset.pkl")

    print(f"{type(plot_dataset) = }")
    print(f"{plot_dataset.keys() = }")
    print(f"{type(plot_dataset['samples']) = }")
    print(f"{type(plot_dataset['predictions']) = }")
    print(f"{type(plot_dataset['samples'][0]) = }")
    print(f"{plot_dataset['samples'][0].keys() = }")
    print(f"{len(plot_dataset['predictions']) = }")
    print(f"{len(plot_dataset['predictions'][0]) = }")
    print(f"{plot_dataset['predictions'][0][0].shape = }")
    print(f"{type(plot_dataset['predictions'][0]) = }")
    print(f"{type(plot_dataset['predictions'][0][0]) = }")

    fp_list = []
    preds = plot_dataset['predictions']
    for pred in preds:
        fp = []
        for _fp in pred:
            fp.append(_fp[0, take_idx, :])
        fp_list.append(fp)

    np_fp = np.array(fp_list)
    np_fp_median = np.median(np_fp, axis=0)
    print(f"{np_fp_median.shape = }")
    # input()

    x = load_npy(f"{folder}/storage/x.npy")
    y = load_npy(f"{folder}/storage/y.npy")
    alt = load_npy(f"{folder}/storage/altitude.npy")

    print(f"{x.shape = }")
    print(f"{y.shape = }")
    print(f"{alt.shape = }")

    plot_traj(x, y, alt, np_fp_median, "./tbd.png")
    plot_traj_map(x, y, alt, np_fp_median, "./tbd_map.png")

    print("DONE")
    return


if __name__ == '__main__':
    main()
