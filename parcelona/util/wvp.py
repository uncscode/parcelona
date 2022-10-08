""" parcelona.util.water_vapor_pressure """

import math

from particula import u
from particula.util.input_handling import in_temperature


def buck_wvp(temperature):
    """ Buck equation for water vapor pressure
        https://en.wikipedia.org/wiki/Arden_Buck_equation
    """

    temp = in_temperature(temperature).m_as("degC")

    if temp >= 0.0:
        return 6.1121 * math.exp(
            (18.678-temp/234.5)*(temp/(257.14+temp))
        )*u.hPa

    return 6.1115 * math.exp(
        (23.036-temp/333.7)*(temp/(279.82+temp))
    )*u.hPa
