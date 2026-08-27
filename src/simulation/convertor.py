from typing import Dict, List
from copy import deepcopy
from math import ceil

import numpy as np

from core.const import NM_TO_KM, OUT_FEATURES
from core.utils import get_idx
from core.storage import OpenScope_DataStorage
from core.storage.utils import load_airport_info
from core.fms import (
    get_shift_degrees,
    np_get_latlong,
    get_haversine_dist_km,
    get_Rhumb_lines_bearing,
    get_glideslope_altitude_from_dist,
    get_n_IAS,
)
from simulation.ils import ILS


class GlideControl():

    def __init__(
        self,
        icao: str,
        ds: OpenScope_DataStorage,
        #
        take_idx: int,
        use_mode: str = 'median',
    ):
        self.ds = ds
        self.take_idx = take_idx

        self.np_fn = None
        if use_mode == 'mean':
            self.np_fn = np.mean
        elif use_mode == 'median':
            self.np_fn = np.median
        else:
            raise NotImplementedError

        #

        self.ils = ILS(icao)

        _info = load_airport_info(icao, get_raw=True)
        self.airport_msa = _info['RAW']['MSA']
        self.magnetic_north = _info['magnetic_north']
        self.ref_pos = _info['position']
        self.runways_dict = _info['runways_dict']

        self.x_idx = get_idx(OUT_FEATURES, 'x')
        self.y_idx = get_idx(OUT_FEATURES, 'y')
        self.alt_idx = get_idx(OUT_FEATURES, 'altitude')

        self.msa = max(self.airport_msa, self.ils.min_gs_alt)

        # km per 20 sec. -> km per sec. -> nm per sec. -> knot
        self.sp_r = (1. / 20) / NM_TO_KM * 3600
        return

    def valid_action(self, s: Dict[str, float], action: List[float | None]):
        altitude, heading, speed = action

        # --- altitude --- #

        if altitude is not None:
            _ceiling = float(s['model_ceiling'])

            # make altitude in range [MSA, _ceiling]
            altitude = max(self.msa, min(altitude, _ceiling))
            altitude = ceil(altitude / 100)  # to FL

            altitude = int(altitude)

        # --- heading --- #

        if heading is not None:
            heading = ceil(get_shift_degrees(heading, do_shift=True))
            heading = int(heading)

        # --- speed --- #

        if speed is not None:
            _cruise = float(s['model_speed_cruise'])
            _landing = float(s['model_speed_landing'])
            _altitude = float(s['altitude'])

            # make speed in range [_landing, _cruise]
            speed = max(_landing, min(speed, _cruise))

            if _altitude < 10000:
                # ref. openscope-6.28.0 make speed in range [..., 250]
                # 1. _calculateLegalSpeed() & overrideTarget() in ./src/assets/scripts/client/aircraft/AircraftModel.js
                # 2. AIRPORT_CONSTANTS.MAX_SPEED_BELOW_10K_FEET = 250 in ./src/assets/scripts/client/constants/aircraftConstants.js
                speed = min(speed, 250)

            speed = int(speed)

        return altitude, heading, speed

    def _get_altitude(self, s: Dict[str, float], t_fp: np.ndarray):
        altitude = t_fp[self.alt_idx]
        return altitude

    def _get_heading(self, fa: np.ndarray, t_fp: np.ndarray):
        a_xy = (fa[self.x_idx], fa[self.y_idx])
        _from = np_get_latlong(*a_xy, self.ref_pos)
        t_xy = (t_fp[self.x_idx], t_fp[self.y_idx])
        _to = np_get_latlong(*t_xy, self.ref_pos)

        heading = get_Rhumb_lines_bearing(
            _from,
            _to,
            magnetic_north=self.magnetic_north,
        )
        return heading

    def _get_speed(
        self,
        s: Dict[str, float],
        p_fp: np.ndarray,
        n_fp: np.ndarray,
    ):
        p_xy = (p_fp[self.x_idx], p_fp[self.y_idx])
        _from = np_get_latlong(*p_xy, self.ref_pos)
        n_xy = (n_fp[self.x_idx], n_fp[self.y_idx])
        _to = np_get_latlong(*n_xy, self.ref_pos)

        # dist. in km -> speed in knot
        n_gs = get_haversine_dist_km(_from, _to) * self.sp_r

        n_ias = get_n_IAS(
            n_gs,
            s['flightPathVector'],
            s['windVector'],
            s['trueAirspeedIncreaseFactor'],
        )
        return n_ias

    def get_raw_action(
        self,
        s: Dict[str, float],
        fa: np.ndarray,
        pred: np.ndarray,
    ):
        """
        :param fa: shape = (?)
        :type fa: np.ndarray
        :param pred: shape = (B, T, ?)
        :type pred: np.ndarray
        """
        # prev, target, next
        p_fp = self.np_fn(pred[:, self.take_idx - 1, :], axis=0)
        t_fp = self.np_fn(pred[:, self.take_idx, :], axis=0)
        n_fp = self.np_fn(pred[:, self.take_idx + 1, :], axis=0)

        altitude = self._get_altitude(s, t_fp)
        heading = self._get_heading(fa, t_fp)
        speed = self._get_speed(s, p_fp, n_fp)

        return self.valid_action(s, (altitude, heading, speed))

    def get_raw_best_action(self, s: Dict[str, float], dist_km, dest_latlong):
        curr_latlong = (s['latitude'], s['longitude'])

        altitude = get_glideslope_altitude_from_dist(dist_km) - 100
        heading = get_Rhumb_lines_bearing(
            curr_latlong,
            dest_latlong,
            magnetic_north=self.magnetic_north,
        )

        return self.valid_action(s, (altitude, heading, None))

    def get_action(
        self,
        #
        c: str,
        c_info: Dict[str, str | float | List | Dict],
        #
        s: Dict[str, float],
        c_fa: np.ndarray,
        fp: np.ndarray,
        #
        can_ctl: bool,
    ):
        """
        openscope command
        """

        tgt_rwy = c_info['rwy_ori']
        altitude, heading, speed = self.get_raw_action(s, c_fa, fp)

        #

        can_ils = c_info['can_ils']
        if can_ils:
            send = False
            action = f"{c}"
            ils_info = None

            # have not done ils yet
            if not c_info['done_ils']:

                # # check on OpenScope side again
                # if s['openscope_can_ils']:

                #     py_can_ils, _pos, _str = self.ils.can_ils(s, tgt_rwy)
                #     ils_info = (py_can_ils, f"{c} {_str}")

                #     # check on Python side again
                #     if py_can_ils:
                #         # c_info['ils_info_2'] = (_pos, _str)
                #         pass

                send = True
                action += f" i {tgt_rwy}"

                c_info['done_ils'] = True
                c_info['state_2'] = deepcopy(s)

            ##

            if s['on_course']:
                pass
            else:  # not on course
                c_info['not_on_course'] += 1

            if s['on_glidepath']:
                pass
            else:  # not on glidepath
                c_info['not_on_glidepath'] += 1

            _can_legal_speed = self.can_legal_speed(s, tgt_rwy)
            if _can_legal_speed:
                send = True
                action += f" sp {speed}"

            if send:
                return action, ils_info

        #

        if not can_ils and can_ctl:
            action = f"{c} a {altitude} h {heading:03d} sp {speed}"
            ils_info = None

            # check on OpenScope side
            if s['openscope_can_ils']:

                py_can_ils, _pos, _str = self.ils.can_ils(
                    s,
                    tgt_rwy,
                    strict_mode=True,
                )
                ils_info = (py_can_ils, f"{c} {_str}")

                # check on Python side
                if py_can_ils:
                    dist_km, dest_latlong = self.ils.try_intercept(s, tgt_rwy)
                    _alt, _h, _ = self.get_raw_best_action(
                        s, dist_km, dest_latlong)

                    # 1. ori. action
                    # action += f" i {tgt_rwy}"

                    # 2. reset action
                    # action = f"{c} i {tgt_rwy}"

                    # 3. tgt on a best point to intercept
                    # action = f"{c} a {_alt} h {_h:03d} i {tgt_rwy}"

                    # 4. tgt on a best point to intercept, but give the clearance later
                    action = f"{c} a {_alt} h {_h:03d} sp {speed}"

                    ####

                    c_info['can_ils'] = True
                    c_info['not_on_course'] = 0
                    c_info['not_on_glidepath'] = 0
                    c_info['try_intercept'] = (dist_km, dest_latlong)

                    c_info['ils_info_1'] = (_pos, _str)
                    c_info['state_1'] = deepcopy(s)

                    raw_action = ((altitude, heading, speed), (_alt, _h))
                    c_info['raw_action_1'] = raw_action
                    c_info['action_1'] = action

            return action, ils_info

        return None, None

    def can_legal_speed(self, s: Dict[str, float], tgt_rwy: str):
        """
        NOTE:
        ref. fn. _calculateTargetedSpeedDuringLanding() in openscope-6.28.0/src/assets/scripts/client/aircraft/AircraftModel.js
            openscope will compute target speed during landing when dist. is in the range [stableApproachDistance, AIRPORT_CONSTANTS.FINAL_APPROACH_FIX_DISTANCE_NM]
            therefore, we may ctl. the speed before AIRPORT_CONSTANTS.FINAL_APPROACH_FIX_DISTANCE_NM = 5
        """
        c_latlong = (s['latitude'], s['longitude'])

        t_latlong = self.runways_dict[tgt_rwy]['this']

        #

        _d = get_haversine_dist_km(c_latlong, t_latlong)
        return _d > self.ils.min_dist_km
