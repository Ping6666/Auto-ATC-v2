from typing import Dict, List, Tuple, Callable, Optional
from copy import deepcopy
import math
import re

from numpy.lib.stride_tricks import sliding_window_view
import numpy as np
import pandas as pd

from core.const import NM_TO_KM, HAMPEL_WINDOW_SIZE, MODEL_ICAO, AIRPORTS
from core.utils import load_json, get_dict_len
from core.fms import (
    get_shift_degrees,
    get_degrees,
    np_get_xy,
    get_haversine_dist_km,
    get_Rhumb_lines_bearing,
    angle_offset,
)

# --- #


def interp_hampel_filter(
    data: np.ndarray,
    window_size: int = HAMPEL_WINDOW_SIZE,
    threshold: int = 3,
):
    """
    Args:
        data: with shape (S, )
    """

    assert window_size % 2 == 1
    k = (window_size - 1) // 2
    assert k > 0

    n = len(data)

    _data = data.copy()

    if n < window_size:
        return _data

    # windows.shape: (S - (2 * k), window_size)
    windows = sliding_window_view(_data, window_shape=window_size)

    medians = np.median(windows, axis=-1)
    mads = np.median(np.abs(windows - medians[:, None]), axis=-1)

    centers = np.arange(k, n - k)
    mask = np.abs(_data[centers] - medians) > threshold * mads

    full_mask = np.zeros(n, dtype=bool)
    full_mask[centers] = mask

    known_idx = np.nonzero(~full_mask)[0]
    known_v = _data[known_idx]

    masked_idx = np.nonzero(full_mask)[0]

    if masked_idx.size > 0:
        masked_v = np.interp(masked_idx, known_idx, known_v)
        _data[masked_idx] = masked_v

    return _data


# --- #


def split_callsign(s):
    try:
        match = re.match(r"([A-Z]+)(\d+)", s)

        if match:
            letters = match.group(1)
            digits = match.group(2)
            return letters, digits

    except:
        pass

    return None, None


# --- #


def check_ifr(
    latitudes: np.ndarray,
    longitudes: np.ndarray,
    tgt_rwy: str,
    #
    magnetic_north: float,
    runways_dict: Dict[str, Dict[str, Tuple[float] | bool]],
    #
    d_km: float = 4.0 * NM_TO_KM,  # km
    angle_threshold: float = 5,  # degree
    check_len: int = 90,
    magic_time_shift: int = 10,
) -> bool:
    """
    Instrument Flight Rules
    """

    _this = runways_dict[tgt_rwy]['this']
    _rwy_bearing = runways_dict[tgt_rwy]['rwy_bearing']

    is_ifr = True
    start_check = False

    for i in range(len(latitudes)):
        ii = i + 1

        if not start_check:
            _curr = (latitudes[-ii], longitudes[-ii])

            _d = get_haversine_dist_km(_this, _curr)
            if _d >= d_km:
                start_check = True

        else:
            if i < magic_time_shift:
                continue

            _ii = -ii + magic_time_shift
            _prev = (latitudes[_ii], longitudes[_ii])
            _curr = (latitudes[-ii], longitudes[-ii])

            if check_len > 0:
                _h1 = get_Rhumb_lines_bearing(
                    _curr,
                    _prev,
                    magnetic_north=magnetic_north,
                )
                _h2 = get_Rhumb_lines_bearing(
                    _curr,
                    _this,
                    magnetic_north=magnetic_north,
                )

                _d1 = abs(angle_offset(_h1, _rwy_bearing))
                _d2 = abs(angle_offset(_h2, _rwy_bearing))

                if (_d1 + _d2) > angle_threshold:
                    is_ifr = False
                    break

                check_len -= 1
            else:
                break

    return is_ifr


def get_tgt_rwy(
    latitudes: np.ndarray,
    longitudes: np.ndarray,
    #
    runways_dict: Dict[str, Dict[str, Tuple[float] | bool]],
    #
    prev_idx: int,
    last_idx: int,
    magnetic_north: float,
):
    # see file ./atc/src/flight_rwy_check.py
    _kwargs = {'magnetic_north': magnetic_north}

    _prev = (latitudes[prev_idx], longitudes[prev_idx])
    _curr = (latitudes[last_idx], longitudes[last_idx])

    _prev_idx = prev_idx
    _diff = prev_idx - last_idx

    # getting none dulp.
    while _prev == _curr:
        _prev_idx -= 1
        _prev = (latitudes[_prev_idx], longitudes[_prev_idx])

    # keep the same offset
    _prev = (latitudes[_prev_idx + _diff], longitudes[_prev_idx + _diff])

    #

    b_curr = get_Rhumb_lines_bearing(_prev, _curr, **_kwargs)

    rwy_diff = []
    for rwy_name, _rwy in runways_dict.items():
        if not _rwy['ils']:
            continue

        _rwy_bearing = _rwy['rwy_bearing']
        b_to_rwy = get_Rhumb_lines_bearing(_curr, _rwy['other'], **_kwargs)

        d0 = abs(angle_offset(b_curr, _rwy_bearing))
        d1 = abs(angle_offset(b_to_rwy, _rwy_bearing))

        _info = {'name': rwy_name, 'd0': d0, 'd1': d1}
        rwy_diff.append(_info)

    _diff = sorted(rwy_diff, key=lambda rwy: (rwy['d0'] + rwy['d1']))
    return _diff[0]['name']


# --- split fn --- #


def go_around_split(
    altitudes: List,
    alt_threshold: int = 3000,
    t_threshold: int = 10,
):
    """
    Args:
        alt_threshold: the alt. threshold (in ft.)
        t_threshold: the time threshold (in sec.)

    """

    n = len(altitudes)
    split_idx = []

    # RJAA -> RJTT
    if altitudes[0] < alt_threshold:
        split_idx.append(n)
        return split_idx

    had_down = False
    t_num = 0

    last_min_idx = None
    idx_shift = 10

    for i in range(n):
        if ((last_min_idx is None)
                or (altitudes[last_min_idx] >= altitudes[i])):
            last_min_idx = i

        if not had_down:
            if altitudes[i] < alt_threshold:
                had_down = True
                t_num = 0

        else:
            if altitudes[i] > alt_threshold:
                t_num += 1

                if t_num > t_threshold:
                    _idx = max(0, last_min_idx - idx_shift)
                    split_idx.append(_idx)

                    last_min_idx = None
                    had_down = False

    split_idx.append(n)
    return split_idx


def no_split(altitudes: List, *args, **kwargs):
    n = len(altitudes)
    return [n]


# --- loader --- #


def load_intervals(fname: str):
    intervals_list = load_json(fname)

    intervals_dict = {}
    for i in intervals_list:
        intervals_dict[i['fname']] = i

    return intervals_dict


def load_airport_info(icao: str, get_raw: bool = False):
    if icao not in AIRPORTS.keys():
        raise KeyError

    airports = deepcopy(AIRPORTS[icao])

    magnetic_north = airports['magnetic_north']
    position = airports['position']
    runways_order = airports['runways_order']

    #

    runways = airports['runways']
    runways_dict: Dict[str, Dict] = deepcopy(runways)

    for _rwy in runways_dict.keys():
        _this = runways_dict[_rwy]['this']
        _other = runways_dict[_rwy]['other']

        _b = get_Rhumb_lines_bearing(
            _this,
            _other,
            magnetic_north=magnetic_north,
        )
        _b2 = get_Rhumb_lines_bearing(
            _other,
            _this,
            magnetic_north=magnetic_north,
        )
        runways_dict[_rwy]['rwy_bearing'] = _b
        runways_dict[_rwy]['rwy_bearing_2'] = _b2

    _info = {
        'icao': icao,
        'magnetic_north': magnetic_north,
        'position': position,
        'runways_order': runways_order,
        'runways_dict': runways_dict,
    }
    if get_raw:
        _info['RAW'] = airports
    return _info


def load_flight(
    fname: str,
    #
    airport_info: Dict,
    #
    tgt_rwy_kwargs: Dict,
    split_fn: Callable[[List], List[int]],
    #
    only_ifr: bool = False,
    #
    # hampel_filter, interp_hampel_filter
    filter_fn: Optional[Callable] = interp_hampel_filter,
):
    magnetic_north: float = airport_info['magnetic_north']
    position: Tuple[float, float] = airport_info['position']
    runways_order: List = airport_info['runways_order']
    runways_dict: Dict = airport_info['runways_dict']

    # NOTE the unit for each col.
    # please refer to file /opensky/src/opensky_trino/download.py fn. save_flight()

    df = pd.read_csv(fname)

    latitudes = df['latitude'].to_numpy()
    longitudes = df['longitude'].to_numpy()

    # altitudes = df['altitude'].to_numpy()
    altitudes = df['geoaltitude'].to_numpy()

    # NOTE The track (aka. heading) refers to the aircraft's direction relative to true north.
    headings = df['track'].to_numpy()

    speeds = df['groundspeed'].to_numpy()

    xs, ys = np_get_xy(latitudes, longitudes, position)

    #

    # NOTE: do filter for the later first and second order derivative
    altitudes = filter_fn(altitudes)
    xs = filter_fn(xs)
    ys = filter_fn(ys)

    #

    flight: Dict[str, np.ndarray]
    flight = {
        #
        'time': np.arange(len(latitudes)) + 1,
        #
        'latitude': latitudes,
        'longitude': longitudes,
        'altitude': altitudes,
        'heading': headings,  # ground track
        'speed': speeds,  # ground speed
        #
        'x': xs,
        'y': ys,
        #
        'heading-sin': np.sin(np.deg2rad(headings)),
        'heading-cos': np.cos(np.deg2rad(headings)),
        #
    }

    # do length check
    data_len = get_dict_len(flight)

    #

    idx_list = split_fn(altitudes)
    rwy_list: List[Dict[str, int | float]] = []

    p_idx = 0
    for _idx in idx_list:
        _latitudes = latitudes[max(0, p_idx):_idx].copy()
        _longitudes = longitudes[max(0, p_idx):_idx].copy()
        p_idx = _idx

        #

        rwy = get_tgt_rwy(
            _latitudes,
            _longitudes,
            runways_dict=runways_dict,
            **tgt_rwy_kwargs,
        )

        is_ifr = check_ifr(
            _latitudes,
            _longitudes,
            rwy,
            magnetic_north,
            runways_dict,
        )

        #

        _rwy_list = {
            'idx': _idx,
            'rwy_ori': rwy,
            'rwy_vec': runways_order.index(rwy),
            'is_ifr': is_ifr,
        }
        rwy_list.append(_rwy_list)

        # ifr, vfr switch
        if only_ifr and not is_ifr:
            return None, 0

    flight['rwy_list'] = rwy_list
    return flight, data_len


# --- #


def get_callsign(v: Dict | str):
    _v = None
    try:
        if isinstance(v, Dict):
            _callsign = str(v['airlineId'] + v['flightNumber'])
            # _callsign = str(v['id'] + '_' + v['airlineId'] + v['flightNumber'])
        elif isinstance(v, str):
            _callsign = v
        else:
            raise NotImplementedError
        _v = str(_callsign).strip().lower()
    except:
        pass
    return _v


def get_callsigns_state(state: List[Dict], airport_info: Dict):
    magnetic_north = airport_info['magnetic_north']
    ref_pos = airport_info['position']

    callsigns_table = {}

    for s in state:
        c = get_callsign(s)
        if c is None:
            continue

        lat = s['positionModel']['latitude']
        long = s['positionModel']['longitude']
        x, y = np_get_xy(lat, long, ref_pos)

        # 0~2π -> 0~359
        magnetic_heading = get_degrees(s['heading'], do_shift=False)

        # 0~359
        _h1 = magnetic_heading + magnetic_north
        true_heading = get_shift_degrees(_h1, do_shift=False)

        # 0~2π -> 0~359
        magnetic_track = get_degrees(s['groundTrack'], do_shift=False)

        # 0~359
        _h2 = magnetic_track + magnetic_north
        true_track = get_shift_degrees(_h2, do_shift=False)

        # --- #

        altitude = s['altitude']
        heading = true_track
        speed = s['groundSpeed']

        callsigns_table[c] = {
            #
            # -90~90
            'latitude': lat,
            # -180~180
            'longitude': long,
            #
            # --- #
            #
            'altitude': altitude,
            'heading': heading,
            'speed': speed,
            #
            # --- #
            #
            'x': x,
            'y': y,
            #
            'heading-sin': math.sin(math.radians(heading)),
            'heading-cos': math.cos(math.radians(heading)),
            #
            # --- #
            #
            'flightThroughAirVector': s['flightThroughAirVector'],
            'windVector': s['windVector'],
            'flightPathVector': s['flightPathVector'],
            'trueAirspeedIncreaseFactor': s['trueAirspeedIncreaseFactor'],
            'indicatedAirspeed': s['speed'],  # unit knots
            'magneticHeading': magnetic_heading,
            'magneticTrack': magnetic_track,
            #
            'flight_phase': s['fms']['currentPhase'],
            'openscope_can_ils': s['fms']['can_ils'],
            'on_course': s['fms']['on_course'],
            'on_glidepath': s['fms']['on_glidepath'],
            #
        }
    return callsigns_table


def get_callsigns_spec(
    state: List[Dict],
    airport_info: Dict,
    *,
    assign_rwy: str = None,
):
    runways_order: List = airport_info['runways_order']

    callsigns_table = {}

    for s in state:
        c = get_callsign(s)
        if c is None:
            continue

        rwy = s['fms']['arrivalRunwayModel']['name']
        if assign_rwy is not None:
            rwy = assign_rwy
        rwy_idx = runways_order.index(rwy)

        _icao = s['model']['icao']
        _icao_idx = MODEL_ICAO.index(_icao)

        callsigns_table[c] = {
            #
            'model_name': s['model']['name'],
            'model_ceiling': s['model']['ceiling'],
            'model_speed_max': s['model']['speed']['max'],
            'model_speed_min': s['model']['speed']['min'],
            'model_speed_cruise': s['model']['speed']['cruise'],
            'model_speed_landing': s['model']['speed']['landing'],
            #
            'model_icao_ori': _icao,
            'model_icao_vec': _icao_idx,
            #
            # --- #
            #
            # model / plot & dump & interaction
            'rwy_ori': rwy,
            'rwy_vec': rwy_idx,
            #
        }
    return callsigns_table


def get_callsigns_info(info_list: List, callsign_list: List):
    _scan_dict = {
        # NOTE cleared ILS doesn't implying successful interception, just OpenScope aware.
        'cleared ILS': 'good_ils',
        'successfully intercepted the ILS signal': 'established_on_ils',
        'unable ILS': 'bad_ils',
        'intercepted localizer above glideslope': 'above_ils',
        'missed approach': 'missed_approach',
        #
        'good day': 'land',
        #
        'leaving radar coverage': 'leave',
        'loss of separation': 'loss_sep',
        'without adequate separation': 'no_takeoff_sep',
        #
        'collided': 'collided',
        'Lost radar contact': 'lost',  # due to collided
    }
    info: Dict[str, str]

    scanned_info: Dict[str, List] = {}
    for info in info_list:
        for k, v in _scan_dict.items():

            message = info['message']
            if k in message:
                # if got message, then try to get the target callsign
                for m in message.split(','):

                    _m = m.strip()
                    # callsign will at the first place or end place or both
                    c1 = str(_m.split(' ')[0]).strip().lower()
                    c2 = str(_m.split(' ')[-1]).strip().lower()

                    cs = [c1] if c1 == c2 else [c1, c2]
                    for c in cs:
                        if c not in callsign_list:
                            continue
                        if c not in scanned_info.keys():
                            scanned_info[c] = []
                        scanned_info[c].append(v)
    return scanned_info
