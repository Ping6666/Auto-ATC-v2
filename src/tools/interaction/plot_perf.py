import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

from argparse import ArgumentParser, Namespace

import matplotlib.pyplot as plt

from core.utils import get_time_str, create_logger, mkdir, load_json
from common.const import FIGSIZE, FIGDPI, FIG_PARAMS

plt.rcParams.update(FIG_PARAMS)


def plot_value(x, ys, feats, savefig_fname):
    # figsize = (7, 5)
    figsize = (7, 4.85)

    fig, axs = plt.subplots(
        2,
        1,
        figsize=figsize,
        sharex=True,
        gridspec_kw={'height_ratios': [3, 1]},
    )
    ax_top, ax_bottom = axs

    fig.subplots_adjust(hspace=0.05)

    for y_data, feat in zip(ys, feats):
        means = [
            sum(pts) / len(pts) if isinstance(pts, list) else pts
            for pts in y_data
        ]

        linewidth = 2 if 'landing' in str(feat).lower() else 1.5

        line_top = ax_top.plot(x, means, linewidth=linewidth, zorder=3)[0]
        color = line_top.get_color()
        ax_bottom.plot(
            x,
            means,
            label=feat,
            linewidth=linewidth,
            color=color,
            zorder=3,
        )

        x_scatter = []
        y_scatter = []
        for xi, pts in zip(x, y_data):
            if isinstance(pts, list):
                x_scatter.extend([xi] * len(pts))
                y_scatter.extend(pts)
            else:
                x_scatter.append(xi)
                y_scatter.append(pts)

        ax_top.scatter(
            x_scatter,
            y_scatter,
            color=color,
            alpha=0.1,
            s=10,
            zorder=2,
        )
        ax_bottom.scatter(
            x_scatter,
            y_scatter,
            color=color,
            alpha=0.1,
            s=10,
            zorder=2,
        )

    ax_top.set_ylim(0.72, 1.02)
    ax_bottom.set_ylim(0, 0.72)

    # ax_top.set_ylim(0.73, 1.02)
    # ax_bottom.set_ylim(0, 0.73)

    # ax_top.set_xlim(1000, 91000)
    # ax_bottom.set_xlim(1000, 91000)

    ax_top.set_xlim(1000. / 3600, 91000. / 3600)
    ax_bottom.set_xlim(1000. / 3600, 91000. / 3600)

    ax_top.spines['bottom'].set_visible(False)
    ax_bottom.spines['top'].set_visible(False)
    ax_top.tick_params(labeltop=False, bottom=False)
    ax_bottom.xaxis.tick_bottom()

    d = 0.015
    kwargs = dict(transform=ax_top.transAxes,
                  color='gray',
                  clip_on=False,
                  linewidth=1.5)
    ax_top.plot((-d, +d), (-d, +d), **kwargs)
    ax_top.plot((1 - d, 1 + d), (-d, +d), **kwargs)

    kwargs.update(transform=ax_bottom.transAxes)
    ax_bottom.plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax_bottom.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    ax_top.grid(axis='y', linestyle='--', alpha=0.6)
    ax_bottom.grid(axis='y', linestyle='--', alpha=0.6)

    ax_bottom.legend(loc='lower right')
    ax_bottom.set_xlabel("Simulation timesteps (hour)")
    # fig.supylabel("Success rate")

    plt.savefig(savefig_fname, dpi=FIGDPI, bbox_inches='tight')
    plt.close('all')

    print(f"plot_value: {savefig_fname} SAVED!")
    return


# def plot_value(x, ys, feats, savefig_fname):
#     figsize = (7, 5)
#     fig, ax = plt.subplots(figsize=figsize)

#     for y_data, feat in zip(ys, feats):
#         means = [
#             sum(pts) / len(pts) if isinstance(pts, list) else pts
#             for pts in y_data
#         ]

#         linewidth = 2 if 'Landed' in feat else 1.5
#         line = ax.plot(x, means, label=feat, linewidth=linewidth, zorder=3)[0]
#         color = line.get_color()

#         x_scatter = []
#         y_scatter = []
#         for xi, pts in zip(x, y_data):
#             if isinstance(pts, list):
#                 x_scatter.extend([xi] * len(pts))
#                 y_scatter.extend(pts)
#             else:
#                 x_scatter.append(xi)
#                 y_scatter.append(pts)

#         ax.scatter(
#             x_scatter,
#             y_scatter,
#             color=color,
#             alpha=0.1,
#             s=10,
#             zorder=2,
#         )

#     ax.set_xlim(1000, 91000)
#     ax.legend()
#     ax.grid(axis='y', linestyle='--', alpha=0.6)

#     plt.tight_layout()
#     plt.savefig(savefig_fname, dpi=FIGDPI, bbox_inches='tight')
#     plt.close('all')

#     print(f"plot_value: {savefig_fname} SAVED!")
#     return

# --- #


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--save-folder", required=True)

    args = parser.parse_args()
    return args


def main(args):
    save_folder = args.save_folder
    save_folder = f"{args.save_folder}/{get_time_str()}"

    folder = "/path/to/int_report/YYYY_MM_DD-HH_MM_SS/score"

    save_step = 500
    num_timestamps = 90000

    mkdir(save_folder)
    logger = create_logger(save_folder)
    logger.info(f"{args = }")

    #

    x = []
    y_w_ils = []
    y_w_l = []
    y_wo_ils = []
    y_wo_l = []
    feats = [
        "ILS clearance rate",
        "Landing rate",
        "Adjusted ILS clearance rate",
        "Adjusted landing rate",
    ]

    # s = 0
    s = 2000
    while True:
        try:
            s += save_step
            if s > num_timestamps:
                break

            fname = f"{folder}/game_score-{s:05d}.json"
            _json = load_json(fname)

            top_level_key = list(_json.keys())[0]
            _data = _json[top_level_key]

            x.append(s / 3600.)

            y_w_ils.append(_data["with_less-can_ils_rate"])
            y_w_l.append(_data["with_less-land_rate"])
            y_wo_ils.append(_data["without_less-can_ils_rate"])
            y_wo_l.append(_data["without_less-land_rate"])

        except:
            break

    plot_value(
        x,
        (y_w_ils, y_w_l, y_wo_ils, y_wo_l),
        feats,
        f"{save_folder}/int_perf.png",
    )

    logger.info("DONE")
    return


if __name__ == '__main__':
    args = get_args()
    main(args)
