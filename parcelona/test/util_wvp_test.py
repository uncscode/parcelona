""" test: parcelona.util.water_vapor_pressure """

from particula import u
from parcelona.util.wvp import buck_wvp


def test_buck_wvp():
    """ test: buck_wvp """

    temperature1 = (300 * u.K).to("degC")
    temperature2 = (350 * u.K).to("degC")
    assert buck_wvp(temperature1).u == u.hPa
    assert buck_wvp(temperature1.to_base_units()).u == u.hPa
    assert buck_wvp(temperature1) < buck_wvp(temperature2)
