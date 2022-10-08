""" test: parcelona.util.water_vapor_pressure """

from particula import u
from parcelona.util.wvp import buck_wvp


def test_buck_wvp():
    """ test: buck_wvp """

    temperature = (300 * u.K).to("degC")

    assert buck_wvp(temperature).u == u.hPa
    assert buck_wvp(temperature.to_base_units()).u == u.hPa
