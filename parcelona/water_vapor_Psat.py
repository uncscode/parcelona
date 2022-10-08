"""Calculate water vapor pressure Psat
"""

import numpy as np

"""TO DO: 
Add the pressure units and pint converter
Add an auto method to select the best method based on T
"""


def water_Psat(
    T: float,
    method: str = "Buck",
    ice: bool = False,
    **kwargs
):
    """ Returns water vapor pressure Psat

    Parameters
    ----------
    T : float
        Temperature [K]
    method : str, optional
        Method to calculate Psat, by default "Buck"
        "Buck" : Buck (1981)
        "GoffGratch" : Goff-Gratch (1946)
        "Antoine" : Antoine (1888)
    ice : bool, optional
    """

    if method == "Buck":
        return Buck(T, **kwargs)
    elif method == "GoffGratch":
        return GoffGratch(T, **kwargs)
    elif method == "Antoine":
        return Antoine(T, **kwargs)
    elif ice:
        return GeffGratch_ice(T, **kwargs)
    else:
        raise ValueError("Method not implemented")


def Buck(T, **kwargs):
    """ Buck (1981) equation
        return kPa
    """
    Tc = T - 273.15
    Psat = 0.61121 * np.exp((18.678 - Tc / 234.5) * (Tc / (257.14 + Tc)))
    return Psat


def GoffGratch(T, **kwargs):
    """ Goff-Gratch (1946) equation
        return hPa
    """
    T_boil = 373.15  # boiling point of water K
    Psat = 10 ** (
        -7.90298 * (T_boil/T - 1) +
        5.02808 * np.log10(T_boil/T) -
        1.3816e-7 * (10 ** (11.344 * (1 - T_boil/T)) - 1) +
        8.1328e-3 * (10 ** (-3.49149 * (T_boil/T - 1)) - 1) +
        np.log10(1013.246)
        )
    return Psat


def GeffGratch_ice(T, **kwargs):
    """ Goff-Gratch (1946) equation for ice
        return hPa
    """
    T_ice = 273.16  # triple point of water K

    Psat = 10 ** (
        -9.09718 * (T_ice/T - 1) -
        3.56654 * np.log10(T_ice/T) +
        0.876793 * (1 - T/T_ice) +
        np.log10(6.1071)
        )
    return Psat


def Antoine(T, **kwargs):
    """ Antoine (1888) equation
        return mmHg
    """
    Tc = T - 273.15
    Psat = 10 ** (8.07131 - 1730.63 / (233.426 + Tc)) # 1 to 99 C
    return Psat
