from typing import Dict, List
from copy import deepcopy

import numpy as np

from core.const import (
    M_TO_NM,
    FT_TO_NM,
    IN_FEATURES,
    OUT_FEATURES,
)
from core.config import SampleConfig
from core.storage.module import DataStorage
from core.storage.utils import get_callsigns_state, get_callsigns_spec


class OpenScope_DataStorage(DataStorage):

    def __init__(self, s_cfg: SampleConfig, assign_rwy: str = None):
        super().__init__(s_cfg.icao)

        self.s_cfg = s_cfg
        self.assign_rwy = assign_rwy

        self.in_callsigns = set()
        self.out_callsigns = set()
        return

    def append(self, _state: List[Dict]):
        c_info_dict: Dict[str, Dict]
        c_info_dict = get_callsigns_state(_state, self.airport_info)

        c_spec_dict: Dict[str, Dict] = {}
        try:
            # NOTE support the rwy info
            c_spec_dict = get_callsigns_spec(
                _state,
                self.airport_info,
                assign_rwy=self.assign_rwy,
            )
        except:
            pass

        _out_callsigns = set(self.storage.keys()) - set(c_info_dict.keys())
        self.out_callsigns.update(_out_callsigns)

        for c, v in c_info_dict.items():
            if c not in self.storage.keys():
                # new callsign
                self.storage[c] = {}
                self.storage[c]['time'] = [1]
                for k1, v1 in v.items():
                    self.storage[c][k1] = [v1]

                _spec = c_spec_dict.get(c)
                if _spec is not None:
                    for k2, v2 in _spec.items():
                        self.storage[c][k2] = v2
                    _rwy = _spec['rwy_ori']
                    self.use_rwy_order[_rwy].append({'id': c})
            else:
                if c in self.out_callsigns:
                    # prevent adding callsign if had out of radar coverage
                    continue

                self.storage[c]['time'].append(self.storage[c]['time'][-1] + 1)
                for k1, v1 in v.items():
                    self.storage[c][k1].append(v1)
        return

    # --- #

    def get_new_callsigns(self):
        callsigns = []
        for c in self.storage.keys():
            if c not in self.in_callsigns:
                callsigns.append(c)
                self.in_callsigns.add(c)
        return callsigns

    def get_callsigns(self):
        callsigns = []
        for c in self.storage.keys():
            if c in self.out_callsigns:
                # not controllable
                continue
            if len(self.storage[c]['time']) <= self.s_cfg.idx_step:
                # not enough data to sample
                continue
            callsigns.append(c)
        return callsigns

    def get_state(self, c: str):
        _s = self.storage[c]

        # from fn. get_callsigns_spec()
        key_list = [
            'model_name',
            'model_ceiling',
            'model_speed_max',
            'model_speed_min',
            'model_speed_cruise',
            'model_speed_landing',
            'model_icao_ori',
            'model_icao_vec',
            'rwy_ori',
            'rwy_vec',
        ]

        curr_s = {}
        for k, v in _s.items():
            _v = v

            if k not in key_list:
                _v = _v[-1]

            curr_s[k] = _v
        return curr_s

    # --- #

    def _is_valid(self, idx: int | None, callsign: str):
        if idx is None:
            return False
        assert idx < 0
        valid = callsign != "PAD"
        if valid:
            t = len(self.storage[callsign]['time'])
            valid = t + idx >= 0
        return valid

    def _get_tgt_rwy_info(self, callsign: str, callsign_list: List[str]):
        s = self.storage[callsign]
        rwy = s['rwy_ori']

        ldg_seq = 0
        for _land in self.use_rwy_order[rwy]:
            _c = _land['id']
            if _c == callsign:
                break
            elif _c in callsign_list:
                ldg_seq += 1
        assert ldg_seq != -1

        rwy_vec = s['rwy_vec']
        is_ifr = True
        return rwy_vec, float(ldg_seq), is_ifr

    # --- #

    def _sample_multiple(
        self,
        idx: int | None,
        feature_keys: List[str],
        callsign_list: List[str],
    ):
        _pad = [0] * len(feature_keys)

        features, mask = [], []
        for c in callsign_list:
            valid = self._is_valid(idx, c)
            if valid:
                # valid
                s = self.storage[c]
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
        idx: int | None,
        callsign_list: List[str],
    ):
        feature_args = [('x', M_TO_NM), ('y', M_TO_NM), ('altitude', FT_TO_NM)]
        _pad = [0] * len(feature_args)

        features, mask = [], []
        for c in callsign_list:
            valid = self._is_valid(idx, c)
            if valid:
                # valid
                s = self.storage[c]
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
        idx: int | None,
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
            valid = self._is_valid(idx, c)
            if valid:
                # valid
                s = self.storage[c]
                rwy_vec, ldg_seq, is_ifr = self._get_tgt_rwy_info(
                    c,
                    callsign_list,
                )

                # max set to 1 hr = 3600 sec.
                _time = min(self.storage[c]['time'][idx], 3600)
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

    def sample_multiple(self, cs: List[str]):
        curr_time = -1
        empty_ret = 0, (None, None, None, None, None)

        #

        if len(cs) == 0:
            return empty_ret
        elif len(cs) > self.s_cfg.max_num_aircraft:
            raise ValueError

        # NOTE: must be in the same order
        cs_list = cs[:self.s_cfg.max_num_aircraft]
        # cs_list = sorted(list(cs))[:self.s_cfg.max_num_aircraft]
        cs_len = len(cs_list)
        pad_len = self.s_cfg.max_num_aircraft - cs_len
        if pad_len > 0:
            _pad = ["PAD"] * pad_len
            cs_list += _pad

        # --- past --- #

        past, past_mask = [], []
        for i in reversed(range(0, self.s_cfg.past_len)):
            _past, _past_mask = self._sample_multiple(
                curr_time - (self.s_cfg.idx_step * i),
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
            self.s_cfg.max_num_aircraft,
        )
        assert np.all(np_info_mask == np_past_mask[-1])

        # --- future --- #

        future, future_mask = [], []
        for i in range(0, self.s_cfg.future_len):
            _curr_time = curr_time if i == 0 else None
            _future, _future_mask = self._sample_multiple(
                _curr_time,
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

    def sampler_multi(self, cs: List[str]):
        _, ret = self.sample_multiple(cs)
        _, _xyz, _i, _p, _f = ret

        if _xyz is None or _i is None or _p is None or _f is None:
            return None

        xyz, _ = _xyz
        i, _ = _i
        p, pm = _p
        f, fm = _f

        xyz_list = [xyz]
        i_dict: Dict[str, List] = {}
        for k, v in i.items():
            i_dict[k] = [v]

        p_list, pm_list = [p], [pm]
        f_list, fm_list = [f], [fm]

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
        return (np_xyz, np_i, np_p, np_pm, np_f, np_fm)
