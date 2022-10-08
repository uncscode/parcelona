""" parcelona.util.water_vapor_pressure """

import numpy as np

from particula import u
from particula.util.input_handling import in_temperature


def buck_wvp(temperature):
    """ Buck equation for water vapor pressure
        https://en.wikipedia.org/wiki/Arden_Buck_equation
    """

    temp = in_temperature(temperature).m_as("degC")

    return 6.1115 * np.exp(
        (23.036-temp/333.7)*(temp/(279.82+temp))
    )*u.hPa * (temp < 0.0) + 6.1121 * np.exp(
        (18.678-temp/234.5)*(temp/(257.14+temp))
    )*u.hPa * (temp >= 0.0)
