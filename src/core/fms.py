from typing import Tuple
import math

import numpy as np

from core.const import EARTH_R, M_TO_KM, FT_TO_KM

# --- #


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


def get_shift_degrees(value: float | int, do_shift: bool):
    """
    Args:
        value: the angle in degrees
    Return:
        if do_shift then return value in range (0, 360]
        else                                   [0, 360)
    """
    if value is not None:
        value = value % 360
        if do_shift and value == 0:
            value = 360
    return value


def get_degrees(value: float, do_shift: bool):
    """
    Args:
        value: the angle in radians
    Return:
        the angle in degrees
    """
    value = math.degrees(value)
    value = get_shift_degrees(value, do_shift=do_shift)
    return value


# --- #


def np_get_xy(lat: np.ndarray, long: np.ndarray, ref_pos: Tuple[float, float]):
    """
    Return:
        the x, y in EARTH_R unit (meter)
    """
    ref_lat, ref_long = ref_pos[0], ref_pos[1]

    d_lat = np.radians(lat - ref_lat)
    d_lon = np.radians(long - ref_long)

    x = EARTH_R * d_lon * np.cos(np.radians(ref_lat))
    y = EARTH_R * d_lat
    return x, y


def np_get_latlong(x: np.ndarray, y: np.ndarray, ref_pos: Tuple[float, float]):
    """
    :param x: in EARTH_R unit (meter)
    :type x: np.ndarray
    :param y: in EARTH_R unit (meter)
    :type y: np.ndarray
    """
    ref_lat, ref_long = ref_pos[0], ref_pos[1]

    d_lat = y / EARTH_R
    d_lon = x / (EARTH_R * np.cos(np.radians(ref_lat)))

    lat = np.degrees(d_lat) + ref_lat
    long = np.degrees(d_lon) + ref_long

    return lat, long


# --- #


def get_dest_point(
    _from: Tuple[float, float],
    bearing: float,
    distance: float,
    is_radians: bool = False,
):
    """
    compute destination point given distance and bearing from start point

    Args:
        _from: (lat, long)
        bearing: the true heading to dest.
        distance: the dist. from start point to dest. point (in R's unit)
        is_radians: the _from & bearing are representing using radians, else with degree

    Return:
        a tuple of float, with (lat, long) (same unit as _from & bearing using is_radians)

    ref.: https://www.movable-type.co.uk/scripts/latlong.html

        all angles in radians!!!
        where: φ is latitude, λ is longitude,
        θ is the bearing (clockwise from north), δ is the angular distance d/R;
        d being the distance travelled, R the earth's radius

        const φ2 = Math.asin( Math.sin(φ1)*Math.cos(d/R) +
                            Math.cos(φ1)*Math.sin(d/R)*Math.cos(brng) );
        const λ2 = λ1 + Math.atan2(Math.sin(brng)*Math.sin(d/R)*Math.cos(φ1),
                                Math.cos(d/R)-Math.sin(φ1)*Math.sin(φ2));
    """

    if is_radians:
        latitude_1, longitude_1 = _from[0], _from[1]
        bearing = bearing
    else:
        latitude_1, longitude_1 = get_radians(_from[0]), get_radians(_from[1])
        bearing = get_radians(bearing)

    R = EARTH_R * M_TO_KM

    latitude_2 = math.asin((math.sin(latitude_1) * math.cos(distance / R)) +
                           (math.cos(latitude_1) * math.sin(distance / R) *
                            math.cos(bearing)))
    longitude_2 = longitude_1 + math.atan2(
        (math.sin(bearing) * math.sin(distance / R) * math.cos(latitude_1)),
        math.cos(distance / R) - (math.sin(latitude_1) * math.sin(latitude_2)),
    )

    if not is_radians:
        # lat long in degree
        latitude_2 = latitude_2 * 180. / math.pi
        longitude_2 = longitude_2 * 180. / math.pi

    _to = (latitude_2, longitude_2)
    return _to


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


def get_Rhumb_lines_bearing(
    _from: Tuple[float, float],
    _to: Tuple[float, float],
    is_radians: bool = False,
    magnetic_north: float = 0,
):
    """
    compute the heading with the Rhumb lines

    ref.: https://www.movable-type.co.uk/scripts/latlong.html

        all angles in radians!!!
        where: φ is latitude, λ is longitude, Δλ is taking shortest route (<180°), R is the earth's radius, ln is natural log

        const Δψ = Math.log(Math.tan(Math.PI/4+φ2/2)/Math.tan(Math.PI/4+φ1/2));
        // if dLon over 180° take shorter rhumb line across the anti-meridian:
        if (Math.abs(Δλ) > Math.PI) Δλ = Δλ>0 ? -(2*Math.PI-Δλ) : (2*Math.PI+Δλ);
        const brng = Math.atan2(Δλ, Δψ) * 180/Math.PI;
    """
    # NOTE see bearingToPosition() in OpenScope

    if is_radians:
        latitude_1, longitude_1 = _from[0], _from[1]
        latitude_2, longitude_2 = _to[0], _to[1]
    else:
        latitude_1, longitude_1 = get_radians(_from[0]), get_radians(_from[1])
        latitude_2, longitude_2 = get_radians(_to[0]), get_radians(_to[1])

    delta_longitude = longitude_2 - longitude_1

    if (abs(delta_longitude) > math.pi):
        if delta_longitude > 0:
            delta_longitude = -(2. * math.pi - delta_longitude)
        else:
            delta_longitude = (2. * math.pi + delta_longitude)

    delta_psi = math.log(
        math.tan(math.pi / 4. + latitude_2 / 2.) /
        math.tan(math.pi / 4. + latitude_1 / 2.))

    # bearing in degree
    bearing = math.atan2(delta_longitude, delta_psi) * 180. / math.pi

    # NOTE true to magnetic
    bearing = bearing - magnetic_north
    return get_shift_degrees(bearing, do_shift=True)


# --- #


def mod(first_value, second_value):
    """
    Returns the modulo operation ensuring the result is always non-negative.
    """
    return ((first_value % second_value) + second_value) % second_value


def vlen(vector):
    """
    Calculate the length (magnitude) of the vector
    """
    return math.sqrt(vector[0]**2 + vector[1]**2)


def angle_offset(a, b):
    return (a - b + 180) % 360 - 180


def get_glideslope_altitude_from_dist(
    distance: float,
    glideslope_gradient: float = 3.0,
):
    """
    Args:
        distance: the distance away from the glideslope (in km)

    Return:
        glideslope altitude in ft.
    """

    _tan = math.tan(get_radians(glideslope_gradient))
    glideslope_altitude = distance * _tan / FT_TO_KM

    return glideslope_altitude


def get_n_IAS(
    n_gs: float,
    #
    flightPathVector: float,
    windVector: float,
    trueAirspeedIncreaseFactor: float,
):
    """
    ref. see fn. updateGroundSpeedPhysics() in file openscope-6.28.0/src/assets/scripts/client/aircraft/AircraftModel.js
    IAS -> factor -> TAS (and its vector) -> wind -> GS (and its vector)

    NOTE: suppose the ias change does not effect the track (aka. heading)
    """

    # # TAS in vector
    # c_tas_vector = flightThroughAirVector
    # c_tas = vlen(c_tas_vector)

    # GS in vector
    c_gs_vector = flightPathVector
    c_gs = vlen(c_gs_vector)

    # wind vector
    w_vector = windVector

    # TAS increase factor
    tas_factor = 1. + trueAirspeedIncreaseFactor

    #

    _r = n_gs / c_gs
    n_gs_vector = [_r * _gs for _gs in c_gs_vector]

    n_tas_vector = [_gs - _w for _gs, _w in zip(n_gs_vector, w_vector)]

    n_ias_vector = [_tas / tas_factor for _tas in n_tas_vector]
    n_ias = vlen(n_ias_vector)

    # c_ias_vector = [_tas / tas_factor for _tas in c_tas_vector]
    # c_ias = vlen(c_ias_vector)
    return n_ias
