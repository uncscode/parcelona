""" test: parcelona.util.wvpsat """

from particula import u

from parcelona.util.wvpsat import buck_wvpsat, real_wvpsat


def test_buck_wvp():
    """ test: buck_wvp """

    temperature1 = (300 * u.K).to("degC")
    temperature2 = (350 * u.K).to("degC")

    assert buck_wvpsat(temperature1).u == u.hPa
    assert buck_wvpsat(temperature1.to_base_units()).u == u.hPa
    assert buck_wvpsat(temperature1) < buck_wvpsat(temperature2)


def test_real_wvp():
    """ test: real_wvp """

    temperature1 = (300 * u.K).to("degC")
    temperature2 = (350 * u.K).to("degC")

    assert real_wvpsat(temperature1, radius=1e-6).u == u.hPa
    assert real_wvpsat(temperature1.to_base_units(), radius=1e-6).u == u.hPa
    assert real_wvpsat(
        temperature1, radius=1e-6) < real_wvpsat(temperature2, radius=1e-6)
