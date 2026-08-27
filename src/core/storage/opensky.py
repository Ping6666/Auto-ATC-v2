from typing import Dict, List
from pathlib import Path
from copy import deepcopy
import random

from tqdm import tqdm
import numpy as np

from core.const import (
    M_TO_NM,
    FT_TO_NM,
    HAMPEL_WINDOW_SIZE,
    IN_FEATURES,
    OUT_FEATURES,
    CALLSIGN_ICAO,
    MODEL_ICAO,
)
from core.icao24 import ICAO24_DICT
from core.utils import listdir
from core.storage.utils import (
    split_callsign,
    go_around_split,
    load_intervals,
    load_flight,
)
from core.storage.module import DataStorage
from core.storage.tree import SegmentTree


class Opensky_DataStorage(DataStorage):

    seg_tree: SegmentTree

    def __init__(self, icao: str, only_ifr: bool):
        super().__init__(icao)

        self.split_fn = go_around_split
        self.only_ifr = only_ifr

        self.use_keys = [
            'icao24',
            'callsign',
            'departure',
            'arrival',
            'intention',
            'start',
            'stop',
        ]
        self.tgt_rwy_kwargs = {
            'prev_idx': -5,
            'last_idx': -1,
            'magnetic_north': self.airport_info['magnetic_north'],
        }

        self.no_sample_len = HAMPEL_WINDOW_SIZE // 2
        return

    def load(self, base_folder: str):
        folder = f"{base_folder}/flights/parsed"

        intervals_fname = f"{base_folder}/flights/intervals.json"
        intervals_dict = load_intervals(intervals_fname)

        files = listdir(folder, get_file=True, level=0)
        files = sorted(files)
        # print(f"{len(files) = }")

        #

        t_list = []
        rwy_t_dict = {rwy: [] for rwy in self.airport_info['runways_order']}

        for i, fname in enumerate(tqdm(files)):
            full_fname = Path(f'{folder}/{fname}')
            if not full_fname.is_file():
                continue

            interval = intervals_dict.get(full_fname.stem)
            if interval is None:
                continue

            if interval['departure'] == interval['arrival']:
                continue

            interval['intention'] = 'other'
            if interval['arrival'] == self.airport_info['icao']:
                interval['intention'] = 'arrival'
            elif interval['departure'] == self.airport_info['icao']:
                interval['intention'] = 'departure'

            # --- #
            if interval['intention'] != 'arrival':
                continue
            # --- #

            _icao24 = interval['icao24']
            if _icao24 not in ICAO24_DICT.keys():
                continue

            _type = ICAO24_DICT[_icao24]['ICAOTypeCode']
            if _type not in MODEL_ICAO:
                continue

            c1, _ = split_callsign(interval['callsign'])
            if c1 is None or c1 not in CALLSIGN_ICAO:
                continue

            ##

            f_id = f"{i:05d}_{_icao24}_{interval['callsign']}\n{interval['start']}_{interval['stop']}"

            flight, data_len = load_flight(
                full_fname,
                self.airport_info,
                self.tgt_rwy_kwargs,
                self.split_fn,
                only_ifr=self.only_ifr,
            )
            if flight is None or data_len == 0:
                continue

            for k in self.use_keys:
                flight[k] = interval[k]

            ##

            # NOTE the parsed flight is starting from inbox
            # the start and stop are the all values time range, which may not be parsed time range
            _inbox = interval['inbox']
            flight['inbox'] = _inbox
            flight['outbox'] = _inbox + data_len - 1

            for rwy_idx in range(len(flight['rwy_list'])):
                _idx = flight['rwy_list'][rwy_idx]['idx']
                flight['rwy_list'][rwy_idx]['land_time'] = _inbox + _idx

            flight['model_icao_ori'] = _type
            flight['model_icao_vec'] = MODEL_ICAO.index(_type)

            ##

            if interval['intention'] == 'arrival':
                # set the landing order
                _start = flight['inbox']
                for rwy_info in flight['rwy_list']:
                    _rwy = rwy_info['rwy_ori']
                    _end = rwy_info['land_time']

                    _item = {'id': f_id, 'start': _start, 'end': _end}
                    rwy_t_dict[_rwy].append(_item)

                    _start = _end + 1
            else:
                # not landing
                flight.pop('rwy_list')

            ##

            self.storage[f_id] = flight

            t = {'id': f_id, 'start': flight['inbox'], 'end': flight['outbox']}
            t_list.append(t)

        #

        self.seg_tree = SegmentTree(t_list)
        for rwy, land_list in rwy_t_dict.items():
            self.use_rwy_order[rwy] = sorted(land_list, key=lambda x: x['end'])
            # print(f"{rwy = } {self.use_rwy_order[rwy] = }")
        return

    # --- #

    def _is_valid(self, curr_time: int, callsign: str):
        valid = callsign != "PAD"
        if valid:
            s = self.storage[callsign]
            _in, _out = s['inbox'], s['outbox']

            valid = _in <= curr_time and curr_time <= _out
            # valid = (_in + self.no_sample_len <= curr_time
            #          and curr_time <= _out - self.no_sample_len)
        return valid

    def _get_tgt_rwy_info(self, curr_time: int, callsign: str):
        s = self.storage[callsign]
        idx = curr_time - s['inbox']

        l = len(s['rwy_list'])
        ii = None
        for i in reversed(range(l)):
            _idx = s['rwy_list'][i]['idx']
            if idx < _idx:
                ii = i
                break

        assert ii is not None

        in_range = False
        ldg_seq = 0

        rwy = s['rwy_list'][ii]['rwy_ori']
        for _land in self.use_rwy_order[rwy]:
            if in_range and curr_time > _land['end']:
                ldg_seq = -1
                break

            if _land['start'] <= curr_time and curr_time <= _land['end']:
                in_range = True

                if _land['id'] == callsign:
                    break
                else:
                    ldg_seq += 1

        assert ldg_seq != -1

        rwy_vec = s['rwy_list'][ii]['rwy_vec']
        is_ifr = s['rwy_list'][ii]['is_ifr']

        return rwy_vec, float(ldg_seq), is_ifr

    # --- #

    def _sample_multiple(
        self,
        curr_time: int,
        feature_keys: List[str],
        #
        callsign_list: List[str],
    ):
        _pad = [0] * len(feature_keys)

        features, mask = [], []
        for c in callsign_list:
            valid = self._is_valid(curr_time, c)
            if valid:
                # valid
                s = self.storage[c]
                idx = curr_time - s['inbox']
                _features = []
                for f in feature_keys:
                    _features.append(s[f][idx] if f in s.keys() else 0)
                features.append(_features)
                mask.append(False)

            else:
                # pad
                features.append(deepcopy(_pad))
                mask.append(True)

        # shape: (S, F)
        np_features = np.array(features, dtype=np.float32)
        np_mask = np.array(mask, dtype=bool)
        return np_features, np_mask

    def _sample_multiple_xyz_nm(
        self,
        curr_time: int,
        #
        callsign_list: List[str],
    ):
        feature_args = [('x', M_TO_NM), ('y', M_TO_NM), ('altitude', FT_TO_NM)]
        _pad = [0] * len(feature_args)

        features, mask = [], []
        for c in callsign_list:
            valid = self._is_valid(curr_time, c)
            if valid:
                # valid
                s = self.storage[c]
                idx = curr_time - s['inbox']
                features.append([s[f][idx] * r for f, r in feature_args])
                mask.append(False)

            else:
                # pad
                features.append(deepcopy(_pad))
                mask.append(True)

        # shape: (S, F)
        np_features = np.array(features, dtype=np.float32)
        np_mask = np.array(mask, dtype=bool)
        return np_features, np_mask

    def _sample_multiple_info(
        self,
        curr_time: int,
        #
        callsign_list: List[str],
        max_num_aircraft: int,
    ):
        empty_dict = {
            #
            'time_emb': 0,
            #
            'model_type_emb': 0,
            #
            'rwy_emb': 0,
            #
            'rwy_order_emb': 0,
            #
            'is_ifr_emb': 0,
            #
        }
        info_dict = {k: [] for k in empty_dict.keys()}

        #

        mask = []
        for c in callsign_list:
            valid = self._is_valid(curr_time, c)
            if valid:
                # valid
                s = self.storage[c]
                idx = curr_time - s['inbox'] + 1

                rwy_vec, ldg_seq, is_ifr = self._get_tgt_rwy_info(curr_time, c)

                # max set to 1 hr = 3600 sec.
                _time = min(idx, 3600)
                _ldg_seq = min(ldg_seq, max_num_aircraft)

                _dict = {
                    #
                    'time_emb': _time,
                    #
                    'model_type_emb': s['model_icao_vec'] + 1,
                    #
                    'rwy_emb': rwy_vec + 1,
                    #
                    'rwy_order_emb': _ldg_seq,
                    #
                    'is_ifr_emb': 1 if is_ifr else 2,
                    #
                }

                for k in info_dict.keys():
                    # NOTE: add extra dim.
                    info_dict[k].append([_dict[k]])
                mask.append(False)

            else:
                # pad
                for k in info_dict.keys():
                    # NOTE: add extra dim.
                    info_dict[k].append([empty_dict[k]])
                mask.append(True)

        # shape: (S, F)
        np_info_dict: Dict[str, np.ndarray] = {}
        for k, v in info_dict.items():
            if 'emb' in k:
                np_info_dict[k] = np.array(v, dtype=np.int32)
            else:
                np_info_dict[k] = np.array(v, dtype=np.float32)
        np_mask = np.array(mask, dtype=bool)
        return np_info_dict, np_mask

    def sample_multiple(
        self,
        curr_time: int,
        idx_step: int,
        past_len: int,
        future_len: int,
        max_num_aircraft: int,
    ):
        # both including curr_time
        assert past_len > 1 and future_len > 1
        empty_ret = 0, (None, None, None, None, None)

        #

        cs_p = self.seg_tree.query(curr_time - idx_step)
        cs_c = self.seg_tree.query(curr_time)
        cs_n = self.seg_tree.query(curr_time + idx_step)
        cs = set.intersection(cs_p, cs_c, cs_n)

        if len(cs) == 0:
            return empty_ret
        elif len(cs) > max_num_aircraft:
            raise ValueError

        cs_list = sorted(list(cs))[:max_num_aircraft]
        cs_len = len(cs_list)
        pad_len = max_num_aircraft - cs_len
        if pad_len > 0:
            _pad = ["PAD"] * pad_len
            cs_list += _pad

        # --- past --- #

        past, past_mask = [], []
        for i in reversed(range(0, past_len)):
            _past, _past_mask = self._sample_multiple(
                curr_time - (idx_step * i),
                IN_FEATURES,
                cs_list,
            )
            past.append(_past)
            past_mask.append(_past_mask)

        # (T, S, F)
        np_past = np.array(past)
        np_past_mask = np.array(past_mask)

        # --- xyz nm --- #

        np_xyz, np_xyz_mask = self._sample_multiple_xyz_nm(curr_time, cs_list)
        assert np.all(np_xyz_mask == np_past_mask[-1])

        # --- curr info --- #

        np_info_dict, np_info_mask = self._sample_multiple_info(
            curr_time,
            cs_list,
            max_num_aircraft,
        )
        assert np.all(np_info_mask == np_past_mask[-1])

        # --- future --- #

        future, future_mask = [], []
        for i in range(0, future_len):
            _future, _future_mask = self._sample_multiple(
                curr_time + (idx_step * i),
                OUT_FEATURES,  # NOTE use as stored key
                cs_list,
            )
            future.append(_future)
            future_mask.append(_future_mask)

        # (T, S, F)
        np_future = np.array(future)
        np_future_mask = np.array(future_mask)

        # --- #

        ret = (
            # (S, )
            np.array(deepcopy(cs_list), dtype=object),
            (
                # (S, ?)
                np_xyz,
                # (S, )
                np_xyz_mask,
            ),
            (
                # (S, ?)
                np_info_dict,
                # (S, )
                np_info_mask,
            ),
            (
                # (S, T, ?)
                np_past.transpose((1, 0, 2)),
                # (S, T)
                np_past_mask.transpose((1, 0)),
            ),
            (
                # (S, T, ?)
                np_future.transpose((1, 0, 2)),
                # (S, T)
                np_future_mask.transpose((1, 0)),
            ),
        )
        return cs_len, ret

    # --- #

    def sample_single(
        self,
        curr_time: int,
        idx_step: int,
        past_len: int,
        future_len: int,
        max_num_aircraft: int,
    ):
        """
        Do flatten on the result from sample multiple
        """

        cs_len, ret = self.sample_multiple(
            curr_time,
            idx_step,
            past_len,
            future_len,
            max_num_aircraft,
        )
        np_cs, _xyz, _i, _p, _f = ret

        if _xyz is None or _i is None or _p is None or _f is None:
            return cs_len, (None, None, None, None, None, None)

        xyz, _ = _xyz
        i, im = _i
        p, pm = _p
        f, fm = _f

        ego_c_list, other_cs_list = [], []
        info_dict: Dict[str, List] = {}
        info_mask = []
        other_curr, other_curr_mask = [], []
        past, past_mask = [], []
        future, future_mask = [], []

        empty_idx = np.arange(cs_len, max_num_aircraft)
        for c_idx in range(cs_len):
            ego_c = np_cs[c_idx]
            ego_p = p[c_idx]
            ego_pm = pm[c_idx]
            ego_f = f[c_idx]
            ego_fm = fm[c_idx]

            ego_xyz = xyz[c_idx:c_idx + 1].copy()
            valid_xyz = (xyz - ego_xyz)[:cs_len]
            valid_l2 = np.linalg.norm(valid_xyz, axis=-1)
            valid_idx = np.argsort(valid_l2)

            _valid_idx = np.concatenate((valid_idx, empty_idx))
            other_cs = np_cs[_valid_idx]
            other_i = deepcopy(i)
            for k in other_i.keys():
                v = other_i[k]
                other_i[k] = v[_valid_idx]
            # NOTE: im will not change
            other_im = im.copy()
            other_c = p[_valid_idx][:, -1, :]
            other_cm = pm[_valid_idx][:, -1]

            ##

            ego_c_list.append(ego_c)
            past.append(ego_p)
            past_mask.append(ego_pm)
            future.append(ego_f)
            future_mask.append(ego_fm)

            other_cs_list.append(other_cs)
            if len(info_dict.keys()) == 0:
                info_dict = {k: [] for k in other_i.keys()}
            for k, v in other_i.items():
                info_dict[k].append(v)
            info_mask.append(other_im)
            other_curr.append(other_c)
            other_curr_mask.append(other_cm)

        #

        # shape: (cs_len, S, F)
        np_info_dict: Dict[str, np.ndarray] = {}
        for k, v in info_dict.items():
            if 'emb' in k:
                np_info_dict[k] = np.array(v, dtype=np.int32)
            else:
                np_info_dict[k] = np.array(v, dtype=np.float32)

        ret = (
            # (cs_len, )
            np.array(ego_c_list, dtype=object),
            # (cs_len, S)
            np.array(other_cs_list, dtype=object),
            (
                # (cs_len, S, ?)
                np_info_dict,
                # (cs_len, S, )
                np.array(info_mask, dtype=bool),
            ),
            (
                # (cs_len, S, ?)
                np.array(other_curr, dtype=np.float32),
                # (cs_len, S, )
                np.array(other_curr_mask, dtype=bool),
            ),
            (
                # (cs_len, T, ?)
                np.array(past, dtype=np.float32),
                # (cs_len, T)
                np.array(past_mask, dtype=bool),
            ),
            (
                # (cs_len, T, ?)
                np.array(future, dtype=np.float32),
                # (cs_len, T)
                np.array(future_mask, dtype=bool),
            ),
        )
        return cs_len, ret

    # --- #

    def sampler_single(self, sampling_probability: float, sample_kwargs: Dict):
        i_dict: Dict[str, List] = {}
        im_list = []
        o_list, om_list = [], []
        p_list, pm_list = [], []
        f_list, fm_list = [], []

        cs_lens = []

        #

        _start = self.seg_tree.points[0]
        _end = self.seg_tree.points[-1]

        for idx in tqdm(range(_start, _end)):
            _sp = random.random()
            if _sp > sampling_probability:
                continue

            cs_len, ret = self.sample_single(idx, **sample_kwargs)
            _, _, _i, _o, _p, _f = ret

            if _i is None or _o is None or _p is None or _f is None:
                continue

            i, im = _i
            o, om = _o
            p, pm = _p
            f, fm = _f

            cs_lens.append(cs_len)

            if len(i_dict.keys()) == 0:
                i_dict = {k: [] for k in i.keys()}
            for k, v in i.items():
                i_dict[k].extend(v)
            im_list.extend(im)

            o_list.extend(o)
            om_list.extend(om)

            p_list.extend(p)
            pm_list.extend(pm)
            f_list.extend(f)
            fm_list.extend(fm)

        #

        _fn = np.array
        # _fn = np.vstack

        np_i: Dict[str, np.ndarray] = {}
        for k, v in i_dict.items():
            if 'emb' in k:
                np_i[k] = _fn(v, dtype=np.int32)
            else:
                np_i[k] = _fn(v, dtype=np.float32)
        np_im = _fn(im_list, dtype=np.bool_)
        np_o = _fn(o_list, dtype=np.float32)
        np_om = _fn(om_list, dtype=np.bool_)
        np_p = _fn(p_list, dtype=np.float32)
        np_pm = _fn(pm_list, dtype=np.bool_)
        np_f = _fn(f_list, dtype=np.float32)
        np_fm = _fn(fm_list, dtype=np.bool_)

        #

        for f_idx, f in enumerate(IN_FEATURES):
            if 'd1_' not in f and 'd2_' not in f:
                continue
            n = 1 if 'd1_' in f else 2

            _f_idx = IN_FEATURES.index(f[3:])
            _v = np_p[..., _f_idx]
            np_p[..., n:, f_idx] = np.diff(_v, n=n, axis=-1)

        # (
        #     (B, S, ?),
        #     (B, S, ),
        #     (B, S, ?),
        #     (B, S, ),
        #     (B, T1, ?),
        #     (B, T1),
        #     (B, T2, ?),
        #     (B, T2),
        # )
        return max(cs_lens), (np_i, np_im, np_o, np_om, np_p, np_pm, np_f,
                              np_fm)

    def sampler_multi(self, sampling_probability: float, sample_kwargs: Dict):
        xyz_list = []
        i_dict: Dict[str, List] = {}
        p_list, pm_list = [], []
        f_list, fm_list = [], []

        cs_lens = []

        #

        _start = self.seg_tree.points[0]
        _end = self.seg_tree.points[-1]

        for idx in tqdm(range(_start, _end)):
            _sp = random.random()
            if _sp > sampling_probability:
                continue

            cs_len, ret = self.sample_multiple(idx, **sample_kwargs)
            _, _xyz, _i, _p, _f = ret

            if _xyz is None or _i is None or _p is None or _f is None:
                continue

            xyz, _ = _xyz
            i, _ = _i
            p, pm = _p
            f, fm = _f

            cs_lens.append(cs_len)

            xyz_list.append(xyz)
            if len(i_dict.keys()) == 0:
                i_dict = {k: [] for k in i.keys()}
            for k, v in i.items():
                i_dict[k].append(v)

            p_list.append(p)
            pm_list.append(pm)
            f_list.append(f)
            fm_list.append(fm)

        #

        _fn = np.array
        # _fn = np.vstack

        np_xyz = _fn(xyz_list, dtype=np.float32)
        np_i: Dict[str, np.ndarray] = {}
        for k, v in i_dict.items():
            if 'emb' in k:
                np_i[k] = _fn(v, dtype=np.int32)
            else:
                np_i[k] = _fn(v, dtype=np.float32)
        np_p = _fn(p_list, dtype=np.float32)
        np_pm = _fn(pm_list, dtype=np.bool_)
        np_f = _fn(f_list, dtype=np.float32)
        np_fm = _fn(fm_list, dtype=np.bool_)

        #

        for f_idx, f in enumerate(IN_FEATURES):
            if 'd1_' not in f and 'd2_' not in f:
                continue
            n = 1 if 'd1_' in f else 2

            _f_idx = IN_FEATURES.index(f[3:])
            _v = np_p[..., _f_idx]
            np_p[..., n:, f_idx] = np.diff(_v, n=n, axis=-1)

        # (
        #     (B, S, ?),
        #     (B, S, ?),
        #     (B, S, T1, ?),
        #     (B, S, T1),
        #     (B, S, T2, ?),
        #     (B, S, T2),
        # )
        return max(cs_lens), (np_xyz, np_i, np_p, np_pm, np_f, np_fm)
