from multiprocessing import Pool
from datetime import datetime
from pathlib import Path
import json

from tqdm import tqdm
import numpy as np
import pandas as pd

# lat min, lat max, long min, long max
AIRSPACE = (34.15, 36.75, 138.85, 141.9)

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


# --- #


def load_flightlist(flightlist_fname: str):
    df = pd.read_csv(flightlist_fname)

    k = ['icao24', 'callsign', 'firstseen', 'lastseen', 'departure', 'arrival']
    flights = [{_k: d[_k] for _k in k} for _, d in df.iterrows()]
    return flights


def get_flight_valid_time(fname: str, t_thres: int = 5):
    feat_keys = [
        'timestamp',
        'last_position',
        'latitude',
        'longitude',
        'groundspeed',
        'geoaltitude',
    ]

    lat1, lat2, long1, long2 = AIRSPACE
    t_c = -1
    t_in, t_out = -1, -1

    valid_now = False

    in_count = 0
    out_count = 0

    #

    df = pd.read_csv(fname)
    df = df.sort_values("timestamp")

    for i, r in df.iterrows():
        try:
            if r[feat_keys].isna().sum() != 0:
                continue

            t_c = datetime.fromisoformat(r['timestamp']).timestamp()
            lat, long = r['latitude'], r['longitude']

            if lat1 <= lat and lat <= lat2 and long1 <= long and long <= long2:
                # in airspace
                valid_now = True
                in_count += 1
                out_count = 0
                if t_in == -1 and in_count >= t_thres:
                    t_in = int(t_c) - t_thres + 1

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
            print(f"{i = } {r = }")
            print(f"{e = }")
            print()
            return None, False

    if t_out == -1:
        t_out = int(t_c)

    if t_in >= t_out:
        return None, False
    _res = (t_in, t_out)
    return _res, True


def is_flight_valid(fname: str, t_in: int, t_out: int, t_thres: float = 1.):
    feat_keys = [
        'timestamp',
        'last_position',
        'latitude',
        'longitude',
        'groundspeed',
        'geoaltitude',
    ]

    lat1, lat2, long1, long2 = AIRSPACE
    t_pp = -1

    valid_now = False

    isna_count = 0
    out_count = 0

    error_count = 0
    invalid_count = 0

    #

    df = pd.read_csv(fname)
    df = df.sort_values("timestamp")

    for i, r in df.iterrows():
        try:
            if r[feat_keys].isna().sum() != 0:
                if valid_now:
                    isna_count += 1
                continue

            t_c = datetime.fromisoformat(r['timestamp']).timestamp()
            t_p = datetime.fromtimestamp(r['last_position']).timestamp()
            if not (t_in <= int(t_c) and int(t_c) <= t_out):
                if valid_now:
                    break
                continue

            valid_now = True
            lat, long = r['latitude'], r['longitude']

            if not (lat1 <= lat and lat <= lat2 and long1 <= long
                    and long <= long2):
                if valid_now:
                    out_count += 1

            if t_pp != -1 and t_pp == t_p and t_c - t_p <= t_thres:
                error_count += 1
            t_pp = t_p

            if t_c - t_p > t_thres:
                invalid_count += 1

        except Exception as e:
            print(f"{i = } {r = }")
            print(f"{e = }")
            print()
            return None, False

    _res = (isna_count, out_count, error_count, invalid_count)
    return _res, True


def valid_flights(
    folder: str,
    #
    lerp_thres: int = 10,
    out_thres: int = 0,
    invalid_thres: float = 0.1,
):
    flightlist_fname = f"{folder}/flightlist.csv"
    flightlist = load_flightlist(flightlist_fname)

    flights_folder = f"{folder}/flights"
    csv_folder = f"{flights_folder}/csv"
    parsed_folder = f"{flights_folder}/parsed"
    mkdir(parsed_folder, can_exists=True)

    intervals_json_fname = f'{flights_folder}/intervals.json'
    full_fname = Path(intervals_json_fname)
    if full_fname.is_file():
        return

    #

    # c = 100

    good_departure, total_departure = 0, 0
    good_arrival, total_arrival = 0, 0

    valid_flights_list = []
    intervals = []
    for f in tqdm(flightlist):
        try:
            icao24 = f['icao24']
            callsign = f['callsign']
            departure = f['departure']
            arrival = f['arrival']
            start = datetime.fromisoformat(f['firstseen'])
            stop = datetime.fromisoformat(f['lastseen'])
            _start = int(start.timestamp())
            _stop = int(stop.timestamp())

            if not isinstance(departure, str):
                departure = None
            if not isinstance(arrival, str):
                arrival = None
        except Exception as e:
            print(f"{f = }")
            print(f"{e = }")
            print()
            continue

        fname = f'{icao24}_{_start}_{_stop}'
        parsed_fname = f'{parsed_folder}/{fname}.csv'
        csv_fname = f'{csv_folder}/{fname}.csv'

        full_fname = Path(parsed_fname)
        if full_fname.is_file():
            continue

        ts, is_valid = get_flight_valid_time(csv_fname)
        if not is_valid:
            print("FAIL | get_flight_valid_time")
            continue
        t_in, t_out = ts
        count = t_out - t_in

        res, is_valid = is_flight_valid(csv_fname, t_in, t_out)
        if not is_valid:
            print("FAIL | is_flight_valid")
            continue
        isna_count, out_count, error_count, invalid_count = res
        bad_points = isna_count + error_count

        invalid_rate = invalid_count / count if count > 0 else 1

        print(
            f"{fname} | " +
            f"{isna_count:05d}, {out_count:05d}, {error_count:05d} | " +
            f"{invalid_count:05d}, {count:05d} {invalid_rate:.2f} | " +
            f"{departure} {arrival}  ",
            end="",
        )

        is_good = bad_points <= lerp_thres and out_count <= out_thres and invalid_rate <= invalid_thres
        if is_good:
            # c -= 1

            valid_flights_list.append(fname)
            intervals.append({
                #
                'fname': fname,
                #
                'icao24': icao24,
                'callsign': callsign,
                'departure': departure,
                'arrival': arrival,
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

        if departure == "RJTT":
            total_departure += 1
            if is_good:
                good_departure += 1
        if arrival == "RJTT":
            total_arrival += 1
            if is_good:
                good_arrival += 1

        dr = good_departure / total_departure if total_departure > 0 else -1
        ar = good_arrival / total_arrival if total_arrival > 0 else -1

        print(f"{total_departure:05d} {dr:.3f} {total_arrival:05d} {ar:.3f}  ")

        # if c <= 0:
        #     break

    #

    valid_flights_fname = f"{folder}/valid_flights.json"
    dump_json(valid_flights_list, valid_flights_fname)
    dump_json(intervals, intervals_json_fname)
    return


# --- #


def parse_flight(fname: str, t_in: int, t_out: int, t_thres: int, _fname: str):
    feat_keys = [
        'latitude',
        'longitude',
        'altitude',
        'geoaltitude',
        'groundspeed',
        'track',  # heading
        'vertical_rate',
    ]

    df = pd.read_csv(fname)
    df = df.sort_values('timestamp')

    df['unix_1'] = df['timestamp'].apply(
        lambda x: datetime.fromisoformat(x).timestamp() if pd.notna(x) else 0)
    df['unix_2'] = df['last_position'].apply(
        lambda x: datetime.fromtimestamp(x).timestamp() if pd.notna(x) else 0)

    df = df[(t_in <= df['unix_1']) & (df['unix_1'] <= t_out)]
    df['invalid_1'] = (df['unix_1'] - df['unix_2'] > t_thres)
    df['invalid_2'] = df['unix_2'].shift(1) == df['unix_2']

    cond = df['invalid_1'] | df['invalid_2'] | df[feat_keys].isna().any(axis=1)

    df.loc[cond, feat_keys] = np.nan
    # df = df[feat_keys].interpolate()
    df[feat_keys] = df[feat_keys].interpolate(limit_area='inside')
    df = df[['timestamp'] + feat_keys]

    # NOTE this is dangerous move
    df = df.dropna(subset=feat_keys)

    df.to_csv(_fname, index=False)
    print(f"parse_flight: {_fname} SAVED!")
    return


def process_file(args):
    return parse_flight(*args)


def parse_flights(folder: str, t_thres: float = 1., processes: int = 24):
    flights_folder = f"{folder}/flights"
    csv_folder = f"{flights_folder}/csv"
    parsed_folder = f"{flights_folder}/parsed"

    intervals_json_fname = f'{flights_folder}/intervals.json'
    intervals = load_json(intervals_json_fname)

    #

    args_list = []
    for interval in tqdm(intervals):
        csv_fname = f"{csv_folder}/{interval['fname']}.csv"
        parsed_csv_fname = f"{parsed_folder}/{interval['fname']}.csv"

        t_in, t_out = interval['inbox'], interval['outbox']
        _args = (csv_fname, t_in, t_out, t_thres, parsed_csv_fname)
        args_list.append(_args)

    if processes == 0:
        for _args in args_list:
            process_file(_args)
    else:
        with Pool(processes) as pool:
            pool.map(process_file, args_list)
    return
