""" test: parcelona.kelvin_radius """

from particula import u

from parcelona.util.kelvin_radius import kelvin_radius, h2o_kelvin_radius


def test_kelvin_radius():
    """ test: parcelona.kelvin_radius """
    assert kelvin_radius(
        surface_tension=0.072,
        molecular_weight=18.015,
        density=1000,
        temperature=300
    ).u == u.m


def test_h2o_kelvin_radius():
    """ test: parcelona.h2o_kelvin_radius """
    assert h2o_kelvin_radius(300).u == u.m
    assert h2o_kelvin_radius(200).u == u.m
