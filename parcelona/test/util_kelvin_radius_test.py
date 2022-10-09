""" test: parcelona.kelvin_radius """

import pytest

from particula import u

from parcelona.util.kelvin_radius import kelvin_radius, h2o_kelvin_radius


def test_kelvin_radius():
    """ test: parcelona.kelvin_radius """
    assert kelvin_radius(
        surface_tension=0.072 * u.N/u.m,
        molecular_weight=0.01815 * u.kg/u.mol,
        density=1000 * u.kg/u.m**3,
        temperature=300
    ).u == u.m


def test_h2o_kelvin_radius():
    """ test: parcelona.h2o_kelvin_radius """
    assert h2o_kelvin_radius(300).u == u.m
    assert h2o_kelvin_radius(200).u == u.m
    assert (
        h2o_kelvin_radius(273.15).to(u.nm).magnitude ==
        pytest.approx(1.0, rel=0.2)
    )
