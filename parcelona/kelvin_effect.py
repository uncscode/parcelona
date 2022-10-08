"""Kelvin effect.
"""

import numpy as np


def kelvin_vapor_pressure(
    radius: float,
    Psat: float,
    material: str = "water",
    **kwargs
):
    """Kelvin vapor pressure
    """
    kelvin_vapor_pressure = Psat * kelvin_enhancement(radius, material, **kwargs)
    return kelvin_vapor_pressure


def kelvin_enhancement(
    radius: float,
    material: str = "water",
    **kwargs
):
    """Kelvin enhancement
    
        Parameters
        ----------
        radius : float
            Particle radius [m]
        material : str, optional
            Material, by default "water"
            "water" : water
            "ice" : ice
        """

    if material == "water":
        kelvin_radius = water_kelvin_radius(**kwargs)
    elif material == "ice":
        kelvin_radius = ice_kelvin_radius(**kwargs)
    else:
        raise ValueError("Method not implemented")

    enhancement_factor = np.exp(kelvin_radius / radius)

    return enhancement_factor


def kelvin_radius(
    surface_tension: float,
    density: float,
    molecular_weight: float,
    **kwargs
):
    """Kelvin radius 
        Based on Neil's definition
    """
    kelvin_radius = 2 * surface_tension * molecular_weight / (
        GAS_CONSTANT * Temperature_K * density 
    )
    return kelvin_radius


def water_kelvin_radius(
    **kwargs
):
    """Kelvin radius for water
    """
    kelvin_radius = kelvin_radius(
        surface_tension=0.072,
        density=1000,
        molecular_weight=18.015,
        **kwargs
    )
    return kelvin_radius


def ice_kelvin_radius(
    **kwargs
):
    """Kelvin radius for ice
    I don't know if this is a thing
    """
    kelvin_radius = kelvin_radius(
        surface_tension=0.058,
        density=917,
        molecular_weight=18.015,
        **kwargs
    )
    return kelvin_radius