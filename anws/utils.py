from typing import Dict, List, Tuple
from multiprocessing import Pool
from datetime import datetime, timezone
from pathlib import Path
import os
import json
import math

from tqdm import tqdm
import numpy as np
import pandas as pd

# earth's radius
EARTH_R = 6371000  # in meter

M_TO_KM = 0.001

# lat min, lat max, long min, long max
# # see TAIPEI FIR EN ROUTE CHART
# AIRSPACE = (21, 29, 117.5, 124)
# see openScope
# AIRSPACE = (23, 25.8, 119.40, 122.45)  # v1
AIRSPACE = (24.3, 25.8, 120.0, 122.3)  # v2

AIRPORTS_ICAO = {
    #
    'RCTP': (25.076389, 121.223889),  # 臺灣桃園國際機場
    'RCSS': (25.069722, 121.5525),  ### 臺北松山機場
    'RCKH': (22.576944, 120.350278),  # 高雄國際機場
    'RCMQ': (24.265, 120.620833),  #### 臺中國際機場
    'RCFN': (22.755278, 121.100278),  # 臺東機場
    'RCNN': (22.949167, 120.211111),  # 臺南機場
    'RCKU': (23.454444, 120.403333),  # 嘉義機場
    'RCLY': (22.027778, 121.534722),  # 蘭嶼機場
    'RCYU': (24.023333, 121.61),  ##### 花蓮機場
    'RCQC': (23.568611, 119.628333),  # 澎湖機場
    'RCBS': (24.428889, 118.361111),  # 金門機場
    'RCMT': (26.224167, 120.002778),  # 馬祖北竿機場
    'RCFG': (26.159722, 119.958333),  # 馬祖南竿機場
    'RCGI': (22.673333, 121.466111),  # 綠島機場
    'RCCM': (23.213056, 119.4175),  ### 七美機場
    'RCWA': (23.367361, 119.502278),  # 望安機場
    'RCKW': (22.040833, 120.730278),  # 恆春機場
    'RCAY': (22.781098, 120.261404),  # 空軍岡山基地
    'RCRA': (22.700470, 120.281244),  # 海軍左營基地
    'RCQS': (22.787216, 121.174022),  # 中華民國空軍志航基地
    '???1': (22.586778, 121.000361),  # 空軍太麻里靶場
    #
    'ZSWZ': (27.911944, 120.851944),  # 溫州龍灣國際機場
    'ZSFZ': (25.935, 119.663056),  #### 福州長樂國際機場
    'ZSQZ': (24.798889, 118.589444),  # 泉州晉江國際機場 
    'ZSAM': (24.543889, 118.1275),  ### 廈門高崎國際機場
    '???2': (24.044330, 117.848706),  # 漳浦空軍基地
    '???3': (24.102971, 117.899540),  # china
    '???4': (27.816859, 121.149519),  # china
    #
}

# --- #


def mkdir(folder, can_exists: bool = False, verbose: bool = False):
    p = Path(folder)

    if p.exists():
        if not can_exists:
            print(f"ERROR | mkdir folder: {folder} exists!")
            raise FileExistsError

        if verbose:
            print(f"WARNING | mkdir folder: {folder} exists!")

    p.mkdir(parents=True, exist_ok=True)
    return


def _listdir(
    folder: str,
    do_join: bool = False,
    get_file: bool = False,
    get_dir: bool = False,
):
    result = []

    _listdir = os.listdir(folder)
    for _dir in _listdir:
        _tmp = os.path.join(folder, _dir)

        _dir1 = _dir
        if do_join:
            _dir1 = _tmp

        if get_file and os.path.isfile(_tmp):
            result.append(_dir1)

        if get_dir and os.path.isdir(_tmp):
            result.append(_dir1)

    return result


def listdir(
    folder: str,
    do_join: bool = False,
    get_file: bool = False,
    get_dir: bool = False,
    level: int = -1,
):
    level = int(level)
    assert level >= -1

    result = []
    if level == -1:
        res = _listdir(
            folder,
            do_join=do_join,
            get_file=get_file,
            get_dir=get_dir,
        )
        result.extend(res)

        _folders = _listdir(
            folder,
            do_join=True,
            get_file=False,
            get_dir=True,
        )
        for f in _folders:
            res = listdir(
                f,
                do_join=do_join,
                get_file=get_file,
                get_dir=get_dir,
                level=level,
            )
            result.extend(res)

    elif level == 0:
        res = _listdir(
            folder,
            do_join=do_join,
            get_file=get_file,
            get_dir=get_dir,
        )
        result.extend(res)

    else:
        _folders = _listdir(
            folder,
            do_join=True,
            get_file=False,
            get_dir=True,
        )
        for f in _folders:
            res = listdir(
                f,
                do_join=do_join,
                get_file=get_file,
                get_dir=get_dir,
                level=level - 1,
            )
            result.extend(res)

    return result


def dump_json(_data, fname: str):
    with open(fname, 'w') as f:
        json.dump(_data, f, indent=2)
        print(f"dump_json: {fname} SAVED!")
    return


def load_json(fname: str):
    _data = None
    with open(fname, 'r') as f:
        _data = json.load(f)
        print(f"load_json: {fname} SUCCESSFUL!")
    return _data


def get_radians(value: float):
    """
    Args:
        value: the angle in degrees
    Return:
        the angle in radians in range [0 ~ 2π)
    """
    value = math.radians(value)
    value = value % (2 * math.pi)
    return value


def get_haversine_dist_km(
    _from: Tuple[float, float],
    _to: Tuple[float, float],
    is_radians: bool = False,
):
    """
    compute the distance according to the haversine formula

    Return:
        the distance in km

    ref.: https://www.movable-type.co.uk/scripts/latlong.html

        all angles in radians!!!
        where: φ is latitude, λ is longitude, R is earth's radius (mean radius = 6,371km);
        note that angles need to be in radians to pass to trig functions!

        const R = 6371e3; // metres
        const φ1 = lat1 * Math.PI/180; // φ, λ in radians
        const φ2 = lat2 * Math.PI/180;
        const Δφ = (lat2-lat1) * Math.PI/180;
        const Δλ = (lon2-lon1) * Math.PI/180;

        const a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
                Math.cos(φ1) * Math.cos(φ2) *
                Math.sin(Δλ/2) * Math.sin(Δλ/2);
        const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));

        const d = R * c; // in R's unit
    """
    if is_radians:
        latitude_1, longitude_1 = _from[0], _from[1]
        latitude_2, longitude_2 = _to[0], _to[1]
    else:
        latitude_1, longitude_1 = get_radians(_from[0]), get_radians(_from[1])
        latitude_2, longitude_2 = get_radians(_to[0]), get_radians(_to[1])

    delta_latitude = latitude_2 - latitude_1
    delta_longitude = longitude_2 - longitude_1

    a = ((math.sin(delta_latitude / 2) * math.sin(delta_latitude / 2)) +
         (math.cos(latitude_1) * math.cos(latitude_2) *
          math.sin(delta_longitude / 2) * math.sin(delta_longitude / 2)))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    d = EARTH_R * M_TO_KM * c
    return d


# --- #


def get_timestamp(d: str):
    d = datetime.strptime(d, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
    return int(d.timestamp())


def add_unix_column(df: pd.DataFrame):
    datetime_col = pd.to_datetime(
        df['datetime'],
        format="%Y-%m-%d %H:%M:%S",
        utc=True,
        errors='coerce',
    )
    unix = datetime_col.astype('int64') // 10**9
    df['unix'] = np.where(datetime_col.notna(), unix, np.nan)
    return df


def is_valid_callsign(c: str):
    if c is None or pd.isna(c) or c == "????????":
        return False
    return True


def get_all_callsign_info(fname: str):
    df = pd.read_csv(fname, dtype={'callsign': str})
    df = add_unix_column(df)
    callsigns = df['callsign'].to_list()
    datetimes = df['unix'].to_list()

    # sweep twice

    latest_callsign = None
    callsign_list = []
    for c in callsigns:
        if c != latest_callsign:
            if is_valid_callsign(c):
                callsign_list.append(c)
                latest_callsign = c

    if len(callsign_list) == 0:
        return None, None

    _callsign_list = callsign_list[:]

    #

    firstseen_idx, lastseen_idx = None, None
    firstseen, lastseen = None, None
    callsigns_info = []

    for i, (c, d) in enumerate(zip(callsigns, datetimes)):
        dd = int(d)
        if c == _callsign_list[0]:
            if firstseen is None:
                # first hit
                firstseen = dd
                firstseen_idx = i
            # last hit
            lastseen = dd
            lastseen_idx = i

        if len(_callsign_list) > 1:
            # has next
            if c == _callsign_list[1]:
                # hit next

                # 1. save prev
                assert firstseen is not None
                assert lastseen >= firstseen
                _dict = {
                    'callsign': _callsign_list[0],
                    'firstseen': firstseen,
                    'firstseen_idx': firstseen_idx,
                    'lastseen': lastseen,
                    'lastseen_idx': lastseen_idx,
                }
                callsigns_info.append(_dict)
                firstseen_idx, lastseen_idx = None, None
                firstseen, lastseen = None, None

                _callsign_list.pop(0)
                if len(_callsign_list) == 0:
                    return callsign_list, callsigns_info

                # 2. reset for next
                firstseen = dd
                firstseen_idx = i
                lastseen = dd
                lastseen_idx = i

    if len(_callsign_list) != 1:
        raise RuntimeError

    _dict = {
        'callsign': _callsign_list[0],
        'firstseen': firstseen,
        'firstseen_idx': firstseen_idx,
        'lastseen': lastseen,
        'lastseen_idx': lastseen_idx,
    }
    callsigns_info.append(_dict)
    return callsign_list, callsigns_info


def get_flightlist(flight_folder: str):
    fname_list = listdir(flight_folder, do_join=False, get_file=True, level=0)

    flights = []
    for fname in tqdm(fname_list):
        icao24, firstseen, lastseen = (str(fname).split('.')[0]).split('_')
        c_list, c_info = get_all_callsign_info(f"{flight_folder}/{fname}")
        _dict = {
            'icao24': icao24,
            'firstseen': int(firstseen),
            'lastseen': int(lastseen),
            'callsign_list': c_list,
            'callsigns_info': c_info,
        }
        if c_list is None or c_info is None:
            continue
        flights.append(_dict)
    return flights


def get_flight_valid_time(
    fname: str,
    callsign_info: Dict,
    t_thres: int = 0,
    df: pd.DataFrame = None,
):
    feat_keys = [
        'datetime',
        'latitude',
        'longitude',
        'groundspeed',
        'geo_altitude',
    ]

    lat1, lat2, long1, long2 = AIRSPACE
    t_c = -1
    t_in, t_out = -1, -1

    valid_now = False

    in_count = 0
    out_count = 0

    #

    if df is None:
        df = pd.read_csv(fname)
        df = add_unix_column(df)

    firstseen_idx = callsign_info['firstseen_idx']
    lastseen_idx = callsign_info['lastseen_idx']
    df = df.iloc[firstseen_idx:lastseen_idx + 1]

    rows = df[feat_keys + ['unix']].to_numpy()
    for i, row in zip(df.index.to_numpy(), rows):
        try:
            if pd.isna(row[:-1]).sum() != 0:
                continue

            lat, long = row[1], row[2]
            t_c = row[-1]

            if lat1 <= lat and lat <= lat2 and long1 <= long and long <= long2:
                # in airspace
                valid_now = True
                in_count += 1
                out_count = 0
                if t_in == -1 and in_count >= t_thres:
                    t_in = int(t_c)
                    # t_in = int(t_c) - t_thres + 1

            else:
                # out of airspace
                if valid_now:
                    # had in airspace once
                    out_count += 1
                    if t_out == -1 and out_count >= t_thres:
                        # confirm out now
                        t_out = int(t_c) - t_thres - 1
                        break

        except Exception as e:
            print(f"{i = } {row = }")
            print(f"{e = }")
            print()
            return None, False

    if t_out == -1:
        t_out = int(t_c)

    if t_in == -1:
        return None, False
    if t_in >= t_out:
        return None, False
    _res = (t_in, t_out)
    return _res, True


def is_flight_valid(
    fname: str,
    callsign_info: Dict,
    t_in: int,
    t_out: int,
    t_thres: float = 1.,
    df: pd.DataFrame = None,
):
    feat_keys = [
        'datetime',
        'latitude',
        'longitude',
        'groundspeed',
        'geo_altitude',
    ]

    lat1, lat2, long1, long2 = AIRSPACE
    t_p = None

    valid_now = False

    isna_count = 0
    out_count = 0

    invalid_count = 0

    #

    if df is None:
        df = pd.read_csv(fname)
        df = add_unix_column(df)

    firstseen_idx = callsign_info['firstseen_idx']
    lastseen_idx = callsign_info['lastseen_idx']
    df = df.iloc[firstseen_idx:lastseen_idx + 1]

    rows = df[feat_keys + ['unix']].to_numpy()
    for i, row in zip(df.index.to_numpy(), rows):
        try:
            if pd.isna(row[:-1]).sum() != 0:
                if valid_now:
                    isna_count += 1
                continue

            t_c = row[-1]
            if not (t_in <= int(t_c) and int(t_c) <= t_out):
                if valid_now:
                    break
                continue

            valid_now = True
            lat, long = row[1], row[2]

            if not (lat1 <= lat and lat <= lat2 and long1 <= long
                    and long <= long2):
                if valid_now:
                    out_count += 1

            if t_p is not None and t_c - t_p > t_thres:
                invalid_count += 1
            t_p = t_c

        except Exception as e:
            print(f"{i = } {row = }")
            print(f"{e = }")
            print()
            return None, False

    _res = (isna_count, out_count, invalid_count)
    return _res, True


def valid_flights(
    from_folder: str,
    to_folder: str,
    #
    lerp_thres: float = 0.6,
    out_thres: int = 0,
    invalid_thres: float = 0.6,
):
    mkdir(to_folder, can_exists=True)
    mkdir(f'{to_folder}/flights', can_exists=True)

    intervals_json_fname = f'{to_folder}/flights/_intervals.json'
    full_fname = Path(intervals_json_fname)
    if full_fname.is_file():
        return

    flightlist = get_flightlist(from_folder)
    flightlist_fname = f"{to_folder}/flightlist.json"
    dump_json(flightlist, flightlist_fname)

    #

    # c = 100

    valid_flights_list = []
    intervals = []
    for f in tqdm(flightlist):
        try:
            icao24 = f['icao24']
            start = f['firstseen']
            stop = f['lastseen']
            callsigns_info = f['callsigns_info']

        except Exception as e:
            print(f"{f = }")
            print(f"{e = }")
            print()
            continue

        _from_fname = f"{icao24}_{start}_{stop}"
        from_fname = f'{from_folder}/{_from_fname}.csv'
        flight_df = pd.read_csv(from_fname)
        flight_df = add_unix_column(flight_df)

        for ci in callsigns_info:
            callsign = ci['callsign']
            _start = ci['firstseen']
            _stop = ci['lastseen']

            _to_fname = f"{icao24}_{_start}_{_stop}"
            fname = f"{_from_fname}-{_to_fname}"

            ts, is_valid = get_flight_valid_time(from_fname, ci, df=flight_df)
            if not is_valid:
                print("FAIL | get_flight_valid_time")
                continue
            t_in, t_out = ts
            count = t_out - t_in

            res, is_valid = is_flight_valid(
                from_fname,
                ci,
                t_in,
                t_out,
                df=flight_df,
            )
            if not is_valid:
                print("FAIL | is_flight_valid")
                continue
            isna_count, out_count, invalid_count = res

            bad_rate = (isna_count) / count if count > 0 else 1
            invalid_rate = invalid_count / count if count > 0 else 1

            print(
                f"{fname} | " + f"{isna_count:05d}, {out_count:05d} | " +
                f"{invalid_count:05d}, {count:05d} | {bad_rate:.2f} {invalid_rate:.2f}  ",
                end="",
            )

            is_good = bad_rate <= lerp_thres and out_count <= out_thres and invalid_rate <= invalid_thres
            if is_good:
                # c -= 1

                valid_flights_list.append(fname)
                intervals.append({
                    #
                    'fname': fname,
                    #
                    'icao24': icao24,
                    'callsign': callsign,
                    #
                    'start': _start,
                    'stop': _stop,
                    #
                    'inbox': t_in,
                    'outbox': t_out,
                    #
                })
                print("GOOD ", end="")

            else:
                print("BAD ", end="")
            print()

        # if c <= 0:
        #     break

    #

    valid_flights_fname = f"{to_folder}/valid_flights.json"
    dump_json(valid_flights_list, valid_flights_fname)
    dump_json(intervals, intervals_json_fname)
    return


# --- #


def parse_flight(fname: str, t_in: int, t_out: int, t_thres: int, _fname: str):
    feat_keys = [
        'latitude',
        'longitude',
        'geo_altitude',
        'groundspeed',
        'track',  # heading
    ]

    full_fname = Path(_fname)
    if full_fname.is_file():
        return

    df = pd.read_csv(fname)
    df = add_unix_column(df)
    df = df.dropna(subset=['unix'])
    df['unix'] = df['unix'].astype(int)
    df = df[(t_in <= df['unix']) & (df['unix'] <= t_out)]
    df = df.sort_values('unix')
    df = df.drop_duplicates(subset='unix', keep='first')

    cond = df[feat_keys].isna().any(axis=1)
    df.loc[cond, feat_keys] = np.nan

    full_index = pd.RangeIndex(start=t_in, stop=t_out + 1, name='unix')
    df = df.set_index('unix')
    df = df.reindex(full_index)
    df[feat_keys] = df[feat_keys].interpolate(
        method='linear',
        limit_area='inside',
    )
    df = df.reset_index()

    df['datetime'] = pd.to_datetime(df['unix'], unit='s', utc=True)
    df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S+00:00')
    df = df[['datetime'] + feat_keys]

    # NOTE this is dangerous move
    df = df.dropna(subset=feat_keys)

    df = df.rename(columns={
        'datetime': 'timestamp',
        'geo_altitude': 'geoaltitude',
    })

    df.to_csv(_fname, index=False)
    print(f"parse_flight: {_fname} SAVED!")
    return


def process_file(args):
    return parse_flight(*args)


def parse_flights(
    from_folder: str,
    to_folder: str,
    t_thres: float = 1.,
    processes: int = 24,
):
    intervals_json_fname = f'{to_folder}/flights/_intervals.json'
    intervals = load_json(intervals_json_fname)

    mkdir(f"{to_folder}/flights/parsed", can_exists=True)

    #

    args_list = []
    for interval in tqdm(intervals):
        _from_fname, _to_fname = interval['fname'].split('-')
        from_fname = f"{from_folder}/{_from_fname}.csv"
        to_fname = f"{to_folder}/flights/parsed/{_to_fname}.csv"

        t_in, t_out = interval['inbox'], interval['outbox']
        _args = (from_fname, t_in, t_out, t_thres, to_fname)
        args_list.append(_args)

    if processes == 0:
        for _args in args_list:
            process_file(_args)
    else:
        with Pool(processes) as pool:
            pool.map(process_file, args_list)
    return


def plot_map(
    lat_long_points,
    savefig_fname: str,
    *,
    zoom: int = 12,
    point_size: int = 5,
):
    from cartopy.io.img_tiles import OSM
    import numpy as np
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

    # ------------------------------------------------------------
    # Input format:
    # [(lat, lon), (lat, lon), ...]
    # ------------------------------------------------------------
    points = np.asarray(lat_long_points, dtype=float)

    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError(
            "lat_long_points must be a list-like object of (lat, long) pairs, "
            "for example: [(25.0, 121.0), (24.5, 118.1)]")

    lat = points[:, 0]
    lon = points[:, 1]

    valid = np.isfinite(lat) & np.isfinite(lon)
    lat = lat[valid]
    lon = lon[valid]

    if len(lat) == 0:
        raise ValueError("No valid finite lat/long points to plot.")

    # ------------------------------------------------------------
    # Plot style
    # ------------------------------------------------------------
    plt.rcParams.update({
        "axes.titlesize": 20,
        "axes.labelsize": 18,
        "legend.fontsize": 16,
        "xtick.labelsize": 14,
        "ytick.labelsize": 14,
        "font.size": 14,
        "font.family": "Times New Roman",
    })

    figsize = (14, 11)

    tile = OSM(cache=True)
    data_crs = ccrs.PlateCarree()

    fig, ax = plt.subplots(
        figsize=figsize,
        subplot_kw={"projection": tile.crs},
    )

    # ------------------------------------------------------------
    # Auto-compute map extent
    # ------------------------------------------------------------
    lat_min, lat_max = lat.min(), lat.max()
    lon_min, lon_max = lon.min(), lon.max()

    lat_pad = max((lat_max - lat_min) * 0.1, 0.005)
    lon_pad = max((lon_max - lon_min) * 0.1, 0.005)

    map_extent = [
        lon_min - lon_pad,
        lon_max + lon_pad,
        lat_min - lat_pad,
        lat_max + lat_pad,
    ]

    ax.set_extent(map_extent, crs=data_crs)

    # ------------------------------------------------------------
    # Add OSM background
    # ------------------------------------------------------------
    ax.add_image(tile, zoom)

    # ------------------------------------------------------------
    # Scatter points
    # Important: x = longitude, y = latitude
    # ------------------------------------------------------------
    ax.scatter(
        lon,
        lat,
        s=point_size,
        marker="o",
        label="Points",
        transform=data_crs,
        zorder=5,
    )

    ax.legend()

    # ------------------------------------------------------------
    # Show lon/lat axis labels
    # ------------------------------------------------------------
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    lon_ticks = np.linspace(map_extent[0], map_extent[1], 5)
    lat_ticks = np.linspace(map_extent[2], map_extent[3], 5)

    ax.set_xticks(lon_ticks, crs=data_crs)
    ax.set_yticks(lat_ticks, crs=data_crs)

    ax.xaxis.set_major_formatter(LongitudeFormatter(number_format=".3f"))
    ax.yaxis.set_major_formatter(LatitudeFormatter(number_format=".3f"))

    plt.tight_layout()
    plt.savefig(savefig_fname, dpi=300)
    plt.close(fig)

    print(f"plot_map: {savefig_fname} SAVED!")
    return


def get_closest_airport(latlong: List[Tuple[float, float]]):
    distance_to_icao = {k: None for k in AIRPORTS_ICAO.keys()}
    for k, v in AIRPORTS_ICAO.items():
        for _latlong in latlong:
            d = get_haversine_dist_km(v, _latlong)
            if distance_to_icao[k] is None:
                distance_to_icao[k] = d
            distance_to_icao[k] = min(d, distance_to_icao[k])

    airport_icao = min(distance_to_icao, key=distance_to_icao.get)
    if distance_to_icao[airport_icao] >= 5.0:
        # possible exceed the airport range
        distance_to_icao_sorted = dict(
            sorted(distance_to_icao.items(), key=lambda item: item[1]))
        print(f"{distance_to_icao_sorted = }")
        return None
    return airport_icao


def ext_flights(to_folder: str, k: int = 10, alt: int = 500):
    intervals_json_fname = f'{to_folder}/flights/_intervals.json'
    intervals = load_json(intervals_json_fname)

    new_intervals = []
    for interval in tqdm(intervals):
        _, _fname = interval['fname'].split('-')
        fname = f"{to_folder}/flights/parsed/{_fname}.csv"

        df = pd.read_csv(fname)

        dfs = [df.head(k), df.tail(k)]
        airports = [None, None]

        for i, _df in enumerate(dfs):
            mask = _df['geoaltitude'].le(alt)
            if mask.any():
                _latlong = _df.loc[mask, ['latitude', 'longitude']]
                latlong = _latlong.dropna().itertuples(index=False, name=None)

                airports[i] = get_closest_airport(list(latlong))
                if airports[i] is None:
                    print(f"{interval = }")
                    print()

        new_interval = {
            'fname': _fname,
            "icao24": interval['icao24'],
            "callsign": interval['callsign'],
            "departure": airports[0],
            "arrival": airports[1],
            "start": interval['start'],
            "stop": interval['stop'],
            "inbox": interval['inbox'],
            "outbox": interval['outbox'],
        }
        new_intervals.append(new_interval)

    intervals_json_fname = f'{to_folder}/flights/intervals.json'
    dump_json(new_intervals, intervals_json_fname)
    return
