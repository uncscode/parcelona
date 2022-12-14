""" parcelona.util.wvpsat """

import numpy as np

from particula import u
from particula.util.input_handling import in_temperature, in_radius

from parcelona.util.kelvin_radius import h2o_kelvin_radius


def buck_wvpsat(temperature):
    """ Buck equation for water vapor pressure
        https://en.wikipedia.org/wiki/Arden_Buck_equation
    """

    temp = in_temperature(temperature).m_as("degC")

    return 6.1115 * np.exp(
        (23.036-temp/333.7)*(temp/(279.82+temp))
    )*u.hPa * (temp < 0.0) + 6.1121 * np.exp(
        (18.678-temp/234.5)*(temp/(257.14+temp))
    )*u.hPa * (temp >= 0.0)


def real_wvpsat(temperature, radius):
    """ wvpsat with kelvin enhancement
        https://en.wikipedia.org/wiki/Kelvin_equation

        Note: I'm not sure yet if we'll use this function or not.
    """

    temperature = in_temperature(temperature)
    radius = in_radius(radius)

    kelvin_radius = h2o_kelvin_radius(temperature)

    calc_wvpsat = buck_wvpsat

    return calc_wvpsat(temperature) * np.exp(kelvin_radius/radius)
