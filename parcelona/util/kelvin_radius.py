""" parcelona.kelvin_radius """

from particula import u
from particula.util.input_handling import in_temperature, in_density, in_molecular_weight
from particula.util.input_handling import in_handling
from particula.constants import GAS_CONSTANT


def kelvin_radius(surface_tension, molecular_weight, density, temperature):
    """ Kelvin radius (Neil's definition)
    """

    temperature = in_temperature(temperature).to_base_units()
    molecular_weight = in_molecular_weight(molecular_weight)
    density = in_density(density)
    surface_tension = in_handling(surface_tension, u.N/u.m)

    return 2 * surface_tension * molecular_weight / (
        GAS_CONSTANT * temperature * density
    )


def h2o_kelvin_radius(temperature):
    """ Kelvin radius for H2O """

    temperature = in_temperature(temperature)

    return kelvin_radius(
        surface_tension=0.072,
        molecular_weight=18.015,
        density=1000,
        temperature=temperature
    ) * (temperature >= 0.0) + kelvin_radius(
        surface_tension=0.058,
        molecular_weight=18.015,
        density=917,
        temperature=temperature
    ) * (temperature < 0.0)
