# NOTE OpenScope v6.28.0 workflow
"""
1. ils in the command for one specific aircraft

2. call runIls() then will run aircraft.pilot.conductInstrumentApproach()
    2.a. will set datum & course in mcp to var. below
        const datum = runwayModel.positionModel;
        const course = runwayModel.angle;
    2.b. set the descentAngle (aka. glideslopeGradient)
    2.c. cancel holding pattern & set arrival runway
    2.d. give the approach clearance

3. will check all constraints below
    3.a. above the min Glideslope Intercept Altitude
        3.a.i. get from runwayModel.getMinimumGlideslopeInterceptAltitude()
            compute the alt. that 5 nm (~ 9.26 km) away with 3 degrees of glideslope gradient + the base alt. (the airport or the runway)

    3.b. _interceptCourse() need to return True
        3.b.i. _interceptCourse() is mcp setter, therefore will always return True

    3.c. _interceptGlidepath() need to return True

4. then the mcp will got attr below
    4.a. MCP_MODE_NAME.ALTITUDE -> MCP_MODE.ALTITUDE.APPROACH
        4.a.i. `return this._calculateTargetedAltitudeToInterceptGlidepath();`

    4.b. MCP_MODE_NAME.HEADING -> MCP_MODE.HEADING.VOR_LOC then will do subroutines below
        4.b.i. `this.targetGroundTrack = this._calculateTargetedHeadingToInterceptCourse();`

5. in _calculateTargetedAltitudeToInterceptGlidepath()
    check this.isEstablishedOnCourse()
            if  true, then everything else is not relevant
        but if false, will not descend on the glideslope

    5.a. in this.isEstablishedOnCourse() will do
        `return runwayModel.isOnApproachCourse(this) && runwayModel.isOnCorrectApproachGroundTrack(this.groundTrack);`

        5.a.i. isOnApproachCourse() return true if the lateral distance from course is less than 500 ft.
            PERFORMANCE.MAXIMUM_DISTANCE_CONSIDERED_ESTABLISHED_ON_APPROACH_COURSE_NM: 0.0822894, // appx. 500 feet

        5.a.ii. isOnCorrectApproachGroundTrack() return true if angle diff. is less than 5 degrees
            PERFORMANCE.MAXIMUM_ANGLE_CONSIDERED_ESTABLISHED_ON_APPROACH_COURSE: 0.0872665, // appx. 5 degrees

6. in _calculateTargetedHeadingToInterceptCourse()
    if shouldAttemptIntercept or inTheWindow then will do intercept

    6.a. shouldAttemptIntercept: which means the distance between the center line and the heading diff are small enough to intercept
    6.b. inTheWindow: which means angle away from localizer with in +- 1.5 degrees

7. isAboveGlidepath() will only be called when aircraft is set _onApproach() and will only effect on the game score
    MAXIMUM_ALTITUDE_DIFFERENCE_CONSIDERED_ESTABLISHED_ON_GLIDEPATH
"""

from typing import Dict
import math

from core.const import NM_TO_KM
from core.storage.utils import load_airport_info
from core.fms import (
    get_radians,
    get_dest_point,
    get_haversine_dist_km,
    get_Rhumb_lines_bearing,
    angle_offset,
    get_glideslope_altitude_from_dist,
)


class ILS():

    def __init__(
        self,
        icao: str,
        #
        min_dist_nm: float = 5,
        max_dist_nm: float = 25,
        #
        # legal ils
        max_legal_angle_diff: float = 10,
        loc_angle_tolerance: float = 1.5,
        alt_extra_tolerance: float = 50,
        #
        max_intercept_angle: float = 30,
    ):
        """
        Args:
            min_dist_nm: the ils max distance (in nm)
                ref. openscope-6.28.0
                0.a. PERFORMANCE.STABLE_APPROACH_TIME_SECONDS = 60 (sec.) in ./src/assets/scripts/client/constants/aircraftConstants.js
                0.b. AIRPORT_CONSTANTS.FINAL_APPROACH_FIX_DISTANCE_NM = 5 (nm) in ./src/assets/scripts/client/constants/airportConstants.js
                1. _calculateTargetedSpeedDuringLanding() in ./src/assets/scripts/client/aircraft/AircraftModel.js
                    stableApproachDistance <= 160 (knots) * NM_TO_KM / 3600 * 60 = 5 (km)

            max_dist_nm: the ils max distance (in nm)


            max_legal_angle_diff: the max ils horizontal angle range (in degree)
            loc_angle_tolerance: the ils horizontal angle tolerance (in degree)
            alt_extra_tolerance: the ils vertical altitude tolerance (in ft.) (50, 100, 200)
        """

        self.min_dist_nm = min_dist_nm
        self.max_dist_nm = max_dist_nm

        self.min_dist_km = self.min_dist_nm * NM_TO_KM
        self.max_dist_km = self.max_dist_nm * NM_TO_KM

        #

        self.max_legal_angle_diff = max_legal_angle_diff
        self.loc_angle_tolerance = loc_angle_tolerance
        self.alt_extra_tolerance = alt_extra_tolerance

        self.max_intercept_angle = max_intercept_angle

        #

        self.dist_threshold = 0.5  # start turn early, to avoid overshoots from tailwind
        self.turn_rate = 3  # 3 degrees per sec.

        #

        _info = load_airport_info(icao, get_raw=True)
        self.airport_msa = _info['RAW']['MSA']
        self.airport_position = _info['RAW']['position']
        self.magnetic_north = _info['magnetic_north']
        self.runways_dict = _info['runways_dict']

        self.min_gs_alt = get_glideslope_altitude_from_dist(self.min_dist_km)

        # knot -> nm per sec. -> km per sec.
        self.sp_r = (1. / 3600) * NM_TO_KM
        return

    def can_ils(
        self,
        s: Dict[str, float],
        tgt_rwy: str,
        strict_mode: bool = False,
    ):
        # ref. openscope-6.28.0/src/assets/scripts/client/aircraft/AircraftModel.js fn. _calculateTargetedHeadingToInterceptCourse()
        """
        if match all constraints below can have legal ils
            1. shouldAttemptIntercept
            2. inTheWindow
        """
        # rwy_bearing is magnetic heading
        tgt_h = self.runways_dict[tgt_rwy]['rwy_bearing']
        tgt_latlong = self.runways_dict[tgt_rwy]['this']

        #

        curr_latlong = (s['latitude'], s['longitude'])
        curr_alt = s['altitude']

        curr_t = s['magneticTrack']
        curr_h = s['magneticHeading']
        curr_ias = s['indicatedAirspeed']

        #

        _d = get_haversine_dist_km(curr_latlong, tgt_latlong)
        _b = get_Rhumb_lines_bearing(
            curr_latlong,
            tgt_latlong,
            magnetic_north=self.magnetic_north,
        )
        _pos = (_d, _b, (tgt_h, tgt_latlong))

        _angle_away_from_loc = angle_offset(tgt_h, _b)
        angle_away_from_loc = abs(_angle_away_from_loc)
        angle_away_from_loc_rad = get_radians(angle_away_from_loc)

        #

        # ILS signal max range
        if _d > self.max_dist_km:
            return False, _pos, 'outside ils range'

        if curr_alt < self.airport_msa:
            return False, _pos, 'below the min. assignable alt.'
        if curr_alt < self.min_gs_alt:
            return False, _pos, 'below the min. glideslope alt.'

        # must below glideslope alt. from curr. dist.
        glideslope_alt = get_glideslope_altitude_from_dist(_d)
        if curr_alt > (glideslope_alt - self.alt_extra_tolerance):
            return False, _pos, 'above the glideslope'

        # early break check (must within the window of ±max_legal_angle_diff away from runway heading)
        if angle_away_from_loc > self.max_legal_angle_diff:
            return False, _pos, 'should not attempt intercept (angle)'

        # --- #

        if strict_mode:
            _heading_away_from_loc = angle_offset(tgt_h, curr_t)
            heading_away_from_loc = abs(_heading_away_from_loc)

            if heading_away_from_loc > self.max_intercept_angle:
                return False, _pos, 'should not attempt intercept (heading)'

            if _angle_away_from_loc * _heading_away_from_loc <= 0:
                return False, _pos, 'should not attempt intercept (same side)'

        # --- #

        in_the_window = angle_away_from_loc < self.loc_angle_tolerance
        if in_the_window:
            return True, _pos, 'in the window'

        #

        h_diff = angle_offset(tgt_h, curr_h)
        h_diff_rad = 2 * math.pi * (h_diff / 360.)

        turn_time_in_hr = abs(h_diff) / self.turn_rate * (1. / 3600.)
        turning_radius_nm = curr_ias * turn_time_in_hr
        dist_covered_during_turn_nm = turning_radius_nm * abs(h_diff_rad)

        _dist = dist_covered_during_turn_nm + self.dist_threshold

        _r = math.sin(angle_away_from_loc_rad) / math.sin(h_diff_rad)
        dist_to_loc = _d / NM_TO_KM * _r
        should_attempt_intercept = (0 < dist_to_loc) and (dist_to_loc <= _dist)

        if should_attempt_intercept:
            return True, _pos, 'should attempt intercept'
        return False, _pos, 'other'

    # --- #

    def try_intercept(
        self,
        s: Dict[str, float],
        tgt_rwy: str,
        intercept_time: float = 60.,
    ):
        """
        use after passing can ils check

        :param intercept_time: t in sec (30, 60, 90)
        """
        # rwy_bearing is magnetic heading
        tgt_h = self.runways_dict[tgt_rwy]['rwy_bearing']
        tgt_h2 = self.runways_dict[tgt_rwy]['rwy_bearing_2']
        tgt_latlong = self.runways_dict[tgt_rwy]['this']

        #

        curr_latlong = (s['latitude'], s['longitude'])

        # knot -> km per sec. -> km
        intercept_dist_km = self.sp_r * s['speed'] * intercept_time

        #

        _d = get_haversine_dist_km(curr_latlong, tgt_latlong)
        _b = get_Rhumb_lines_bearing(
            curr_latlong,
            tgt_latlong,
            magnetic_north=self.magnetic_north,
        )

        angle_away_from_loc = abs(angle_offset(tgt_h, _b))
        angle_away_from_loc_rad = get_radians(angle_away_from_loc)

        # force to intercept
        new_to_rwy_dist_km = self.min_dist_km
        if angle_away_from_loc <= self.max_legal_angle_diff:
            to_rwy_dist_km = _d * math.cos(angle_away_from_loc_rad)
            to_rwy_dist_km = min(abs(to_rwy_dist_km), _d)
            _new_to_rwy_dist_km = to_rwy_dist_km - intercept_dist_km

            new_to_rwy_dist_km = max(0, _new_to_rwy_dist_km)
            # new_to_rwy_dist_km = max(self.min_dist_km, _new_to_rwy_dist_km)

        # true heading
        true_tgt_h2 = tgt_h2 + self.magnetic_north

        dest_latlong = get_dest_point(
            tgt_latlong,
            true_tgt_h2,
            new_to_rwy_dist_km,
        )
        return new_to_rwy_dist_km, dest_latlong
