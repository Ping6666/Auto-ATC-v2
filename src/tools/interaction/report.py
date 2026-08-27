import sys
from pathlib import Path

# add src folder
sys.path.append(str(Path(__file__).absolute().parent.parent.parent))

# --- #

from typing import Dict, List
from argparse import ArgumentParser, Namespace

from core.utils import get_time_str, create_logger, mkdir, dump_json, load_json
from core.config import custom_type


def get_args() -> Namespace:
    parser = ArgumentParser()

    parser.add_argument("--save-folder", required=True)

    parser.add_argument("--nargs-int-folder", nargs='+', required=True)

    parser.add_argument("--num-pred", type=int, required=True)

    parser.add_argument("--ckpt-idx", type=custom_type, required=True)
    parser.add_argument('--nargs-take-idx', nargs='+', type=int, required=True)

    parser.add_argument("--num-exp", type=int, required=True)

    parser.add_argument("--save-step", type=int, required=True)
    parser.add_argument("--num-timestamps", type=int, required=True)

    args = parser.parse_args()
    return args


# --- #


def to_game_str(ckpt_idx: int, take_idx: int):
    return f"{ckpt_idx:06d}/{take_idx:02d}"


def from_game_str(_str1: str):
    ckpt_idx, take_idx = _str1.split('/')
    return int(ckpt_idx), int(take_idx)


def p(res: List[Dict]):
    _count = len(res)
    _can_ils_count = sum(t['can_ils'] == True for t in res)
    _done_ils_count = sum(t['done_ils'] == True for t in res)
    _good_ils_count = sum(t.get('good_ils') == True for t in res)
    _on_ils_count = sum(t.get('established_on_ils') == True for t in res)
    _missed_count = sum(t.get('missed_approach') == True for t in res)

    _avg_len = 0
    if _count != 0:
        _avg_len = sum(t.get('len', 0) for t in res) / _count
    return _count, _can_ils_count, _done_ils_count, _good_ils_count, _on_ils_count, _missed_count, _avg_len


def get_perf(info: Dict[str, Dict], less_len: int = 2000):
    _finished = False

    res = {
        'total': [],
        'land': [],
        'leave': [],
        'lost': [],  # including collided
        'less': [],
        'other': [],
    }

    for k, v in info.items():
        if not _finished:
            if 'len' in v.keys():
                _finished = True

        _d = {'callsign': k, **v}

        res['total'].append(_d)

        _key = None

        if v.get('land', False):
            _key = 'land'

        elif v.get('leave', False):
            _key = 'leave'

        elif v.get('lost', False):
            _key = 'lost'

        elif v.get('len', 0) < less_len:
            _key = 'less'

        else:
            _key = 'other'

        if _key is not None:
            res[_key].append(_d)

    # see fn. get_callsigns_info()
    # a or b: with or without less included
    # 1.      land rate                # good
    # 1.1.    ils rate
    # 1.2.    good ils rate            # cleared ILS
    # 1.2.    on ils rate              # successfully intercepted the ILS signal
    # 2.      lost rate                # bad
    # 3.      leave rate + other rate  # not so bad

    t_c, t_ci_c, t_di_c, t_gi_c, t_oi_c, t_m_c, t_avg_l = p(res['total'])
    la_c, la_ci_c, la_di_c, la_gi_c, la_oi_c, la_m_c, la_avg_l = p(res['land'])
    _res = p(res['leave'])
    lea_c, lea_ci_c, lea_di_c, lea_gi_c, lea_oi_c, lea_m_c, lea_avg_l = _res
    lo_c, lo_ci_c, lo_di_c, lo_gi_c, lo_oi_c, lo_m_c, lo_avg_l = p(res['lost'])
    le_c, le_ci_c, le_di_c, le_gi_c, le_oi_c, le_m_c, le_avg_l = p(res['less'])
    o_c, o_ci_c, o_di_c, o_gi_c, o_oi_c, o_m_c, o_avg_l = p(res['other'])

    # a

    a_la_rate = la_c / t_c
    a_ci_rate = t_ci_c / t_c
    a_di_rate = t_di_c / t_c
    a_gi_rate = t_gi_c / t_c
    a_oi_rate = t_oi_c / t_c
    a_lo_rate = lo_c / t_c
    a_lea_rate = lea_c / t_c
    a_le_rate = le_c / t_c
    a_o_rate = o_c / t_c
    a_lea_le_o_rate = (lea_c + le_c + o_c) / t_c

    # b

    no_le_count = t_c - le_c
    if no_le_count == 0:
        no_le_count = 1e9

    b_la_rate = la_c / no_le_count
    b_ci_rate = (t_ci_c - le_ci_c) / no_le_count
    b_di_rate = (t_di_c - le_di_c) / no_le_count
    b_gi_rate = (t_gi_c - le_gi_c) / no_le_count
    b_oi_rate = (t_oi_c - le_oi_c) / no_le_count
    b_lo_rate = lo_c / no_le_count
    b_lea_rate = lea_c / no_le_count
    b_o_rate = o_c / no_le_count
    b_lea_o_rate = (lea_c + o_c) / no_le_count

    _perf: Dict[str, int | float] = {
        #
        'raw-total': t_c,
        'raw-total-can-ils': t_ci_c,
        'raw-total-done-ils': t_di_c,
        'raw-total-good-ils': t_gi_c,
        'raw-total-on-ils': t_oi_c,
        'raw-total-missed': t_m_c,
        'raw-total-avg_len': t_avg_l,
        ##
        'raw-land': la_c,
        'raw-land-can-ils': la_ci_c,
        'raw-land-done-ils': la_di_c,
        'raw-land-good-ils': la_gi_c,
        'raw-land-on-ils': la_oi_c,
        'raw-land-missed': la_m_c,
        'raw-land-avg_len': la_avg_l,
        ##
        'raw-leave': lea_c,
        'raw-leave-can-ils': lea_ci_c,
        'raw-leave-done-ils': lea_di_c,
        'raw-leave-good-ils': lea_gi_c,
        'raw-leave-on-ils': lea_oi_c,
        'raw-leave-missed': lea_m_c,
        'raw-leave-avg_len': lea_avg_l,
        ##
        'raw-lost': lo_c,
        'raw-lost-can-ils': lo_ci_c,
        'raw-lost-done-ils': lo_di_c,
        'raw-lost-good-ils': lo_gi_c,
        'raw-lost-on-ils': lo_oi_c,
        'raw-lost-missed': lo_m_c,
        'raw-lost-avg_len': lo_avg_l,
        ##
        'raw-less': le_c,
        'raw-less-can-ils': le_ci_c,
        'raw-less-done-ils': le_di_c,
        'raw-less-good-ils': le_gi_c,
        'raw-less-on-ils': le_oi_c,
        'raw-less-missed': le_m_c,
        'raw-less-avg_len': le_avg_l,
        ##
        'raw-other': o_c,
        'raw-other-can-ils': o_ci_c,
        'raw-other-done-ils': o_di_c,
        'raw-other-good-ils': o_gi_c,
        'raw-other-on-ils': o_oi_c,
        'raw-other-missed': o_m_c,
        'raw-other-avg_len': o_avg_l,
        #
        'with_less-land_rate': a_la_rate,
        'with_less-can_ils_rate': a_ci_rate,
        'with_less-done_ils_rate': a_di_rate,
        'with_less-good_ils_rate': a_gi_rate,
        'with_less-on_ils_rate': a_oi_rate,
        'with_less-lost_rate': a_lo_rate,
        'with_less-leave_rate': a_lea_rate,
        'with_less-less_rate': a_le_rate,
        'with_less-other_rate': a_o_rate,
        'with_less-leave+less+other_rate': a_lea_le_o_rate,
        #
        'without_less-land_rate': b_la_rate,
        'without_less-can_ils_rate': b_ci_rate,
        'without_less-done_ils_rate': b_di_rate,
        'without_less-good_ils_rate': b_gi_rate,
        'without_less-on_ils_rate': b_oi_rate,
        'without_less-lost_rate': b_lo_rate,
        'without_less-leave_rate': b_lea_rate,
        'without_less-other_rate': b_o_rate,
        'without_less-leave+other_rate': b_lea_o_rate,
        #
    }
    return _perf


def load_exp(fname: str):
    _json = None
    try:
        _json = load_json(fname)
    except:
        pass
    if _json is None:
        return None
    return {'fname': fname, **get_perf(_json)}


def main(args):
    save_folder = args.save_folder
    save_folder = f"{args.save_folder}/{get_time_str()}"

    nargs_int_folder: List = args.nargs_int_folder

    num_pred = args.num_pred
    ckpt_idx_list: List = args.ckpt_idx
    take_idx_list: List = args.nargs_take_idx
    num_exp = args.num_exp

    save_step = args.save_step
    num_timestamps = args.num_timestamps

    mkdir(save_folder)
    logger = create_logger(save_folder)
    logger.info(f"{args = }")

    #

    exp_idx_list = list(range(num_exp))
    time_idx_list = list(range(save_step, num_timestamps + 1, save_step))

    logger.info(f"{exp_idx_list = }")
    logger.info(f"{time_idx_list = }")

    # --- #

    game_name_list = []
    for ckpt_idx in ckpt_idx_list:
        for take_idx in take_idx_list:
            _str = to_game_str(ckpt_idx, take_idx)
            game_name_list.append(_str)
    logger.info(f"{game_name_list = }")

    #

    for time_idx in time_idx_list:
        game_score_dict: Dict[str, Dict[str, List]] = {}
        for int_folder in nargs_int_folder:
            for exp_idx in exp_idx_list:
                for game_name in game_name_list:
                    if game_name not in game_score_dict.keys():
                        game_score_dict[game_name] = {}

                    folder = f"{int_folder}/{game_name}/{num_pred:03d}-{exp_idx:03d}"
                    fname = f"{folder}/parsed/callsigns_info-{time_idx:05d}.json"

                    score = load_exp(fname)
                    if score is None:
                        continue

                    if len(game_score_dict[game_name].keys()) == 0:
                        for k in score.keys():
                            game_score_dict[game_name][k] = []

                    for k, v in score.items():
                        game_score_dict[game_name][k].append(v)

        folder = f"{save_folder}/score/"
        mkdir(folder, can_exists=True)
        dump_json(game_score_dict, f"{folder}/game_score-{time_idx:05d}.json")

    logger.info("DONE")
    return


"""
usage: report.py [-h] --save-folder SAVE_FOLDER --nargs-int-folder NARGS_INT_FOLDER [NARGS_INT_FOLDER ...] --num-pred NUM_PRED --ckpt-idx CKPT_IDX --nargs-take-idx
                 NARGS_TAKE_IDX [NARGS_TAKE_IDX ...] --num-exp NUM_EXP --save-step SAVE_STEP --num-timestamps NUM_TIMESTAMPS

options:
  -h, --help            show this help message and exit
  --save-folder SAVE_FOLDER
  --nargs-int-folder NARGS_INT_FOLDER [NARGS_INT_FOLDER ...]
  --num-pred NUM_PRED
  --ckpt-idx CKPT_IDX
  --nargs-take-idx NARGS_TAKE_IDX [NARGS_TAKE_IDX ...]
  --num-exp NUM_EXP
  --save-step SAVE_STEP
  --num-timestamps NUM_TIMESTAMPS
"""
if __name__ == '__main__':
    args = get_args()
    main(args)
