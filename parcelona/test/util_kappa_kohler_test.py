""" test: parcelona.util.kappa_kohler """

import pytest
from particula import u
from parcelona.util.kappa_kohler import (
    particle_effective_activity,
    particle_phase_h2o_activity,
    particle_h2o_activation
)
from parcelona.util.kelvin_radius import h2o_kelvin_radius

dry_radius = 50e-9 * u.m
wet_radius = 500e-9 * u.m
kappa_ccn = 0.1 * u.dimensionless
dry_radius_array = [100e-9, 150e-9] * u.m
wet_radius_array = [500e-9, 151e-9] * u.m
kappa_ccn_array = [0.1, 0.01] * u.dimensionless


def test_particle_phase_h2o_activity():
    """ test: parcelona.util.kappa_kohler.particle_phase_h2o_activity """
    bulk_activity = particle_phase_h2o_activity(
        dry_radius,
        wet_radius,
        kappa_ccn
    )
    bulk_activity_array = particle_phase_h2o_activity(
        dry_radius_array,
        wet_radius_array,
        kappa_ccn_array
    )
    assert bulk_activity.u == u.dimensionless
    assert bulk_activity.magnitude == pytest.approx(1, rel=0.1)
    assert bulk_activity_array.u == u.dimensionless
    assert bulk_activity_array[0].magnitude > bulk_activity_array[1].magnitude


def test_particle_effective_activity():
    """ test: parcelona.util.kappa_kohler.particle_effective_activity """
    bulk_activity = particle_phase_h2o_activity(
        dry_radius,
        wet_radius,
        kappa_ccn
    )
    sat_ratio = particle_effective_activity(
        bulk_activity,
        h2o_kelvin_radius(300 * u.K),
        wet_radius)

    bulk_activity_array = particle_phase_h2o_activity(
        dry_radius_array,
        wet_radius_array,
        kappa_ccn_array
    )
    sat_ratio_array = particle_effective_activity(
        bulk_activity_array,
        h2o_kelvin_radius(300 * u.K),
        wet_radius_array)

    assert sat_ratio.u == u.dimensionless
    assert sat_ratio.magnitude == pytest.approx(1, rel=0.01)
    assert sat_ratio_array.u == u.dimensionless
    assert sat_ratio_array[0].magnitude > sat_ratio_array[1].magnitude


def test_particle_h2o_activation():
    """ test: parcelona.util.kappa_kohler.particle_h2o_activation """
    temperature = 293 * u.K

    activation_radius, activation_crit_sat = particle_h2o_activation(
        temperature,
        dry_radius,
        kappa_ccn)

    assert activation_radius.u == u.m
    assert activation_crit_sat.u == u.dimensionless
    assert activation_crit_sat.magnitude == pytest.approx(1.003, rel=0.001)
