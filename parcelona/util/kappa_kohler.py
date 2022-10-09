""" parcelona.kappa_kohler """

import numpy as np
from scipy.optimize import fminbound

# from particula import u
# from particula.util.input_handling import in_temperature, in_density
# from particula.util.input_handling import in_handling, in_molecular_weight

from parcelona.util.kelvin_radius import h2o_kelvin_radius


def particle_phase_h2o_activity(
    dry_radius,
    wet_radius,
    kappa_ccn,
    **kwargs
):
    """ kappa equilibrium water activity over a material.

    Parameters:
        dry_radius (float): dry radius of the particle [m]
        wet_radius (float): wet radius of the particle [m]
        kappa_ccn (float): kappa CCN value of the particle [dimensionless]

    Returns:
        float: water activity of the particle [dimensionless]

    Calculates the equilibrium water activity over an aerosol particle with
    specified hygroscopicity bathed in gas at a particular temperature. The
    kappa parameter used is kappa_ccn, which specifies the kappa value at the
    critical supersaturation for cloud condensation nuclei (CCN). The kappa
    value changes with water activity for non-ideal mixtures. This more general
    kappa is call kappa_HGF, and is derived from water activity models. The
    kappa_HGF value at the CCN critical supersaturation (or activation point)
    is kappa_ccn value.

    References:
    We used the kappa definition presented by:
    Petters, M. D.,; Kreidenweis, S. M. (2007). A single parameter
    representation of hygroscopic growth and cloud condensation nucleus
    activity Atmospheric Chemistry and Physics, 7(8), 1961-1971.
    https://doi.org/10.5194/acp-7-1961-2007

    For more information on kappa_ccn and kappa_HGF, see Figure 9 in:
    Gorkowski, K., Preston, T. C., &#38; Zuend, A. (2019).
    Relative-humidity-dependent organic aerosol thermodynamics via an efficient
    reduced-complexity model. Atmospheric Chemistry and Physics, June, 1-37.
    https://doi.org/10.5194/acp-2019-495


    """
    return 1/(1 + kappa_ccn * (dry_radius/wet_radius)**3)


def particle_effective_activity(bulk_activity, kelvin_radius, wet_radius):
    """ effective water activity over a particle, known as saturation ratio.

    Parameters:
        bulk_activity (float): water activity of the bulk phase [dimensionless]
        kelvin_radius (float): kelvin radius of the particle [m]
        wet_radius (float): wet radius of the particle [m]

    Returns:
        float: effective water activity of the particle [dimensionless]

    Calculates the effective water activity of a particle or saturation ratio.
    This accounts for Kelvin effects, or the curved surface of the particle.

    References:
    We used the definition of effective water activity presented by:
    Petters, M. D.,; Kreidenweis, S. M. (2007). A single parameter
    representation of hygroscopic growth and cloud condensation nucleus
    activity, Atmospheric Chemistry and Physics, 7(8), 1961-1971.
    https://doi.org/10.5194/acp-7-1961-2007

    """
    return bulk_activity * np.exp(kelvin_radius/wet_radius)


def particle_h2o_activation_radius(
    temperature,
    dry_radius,
    kappa_ccn,
    **kwargs
):
    """ activation radius of a particle.

    Parameters:
        temperature (float): temperature of the bulk phase [K]
        kappa_ccn (float): kappa CCN value of the particle [dimensionless]
        dry_radius (float): dry radius of the particle [m]

    Returns:
        float: activation radius of the particle [m]

    Calculates the activation radius of a particle, which is the radius at
    which the max saturation ratio occurs (on the Kohler curve). This is the
    radius at which the the particle becomes activated as a cloud condensation
    nuclei (CCN). If a particle grows beyond this size, then it is said to
    "activate", and will continue to freely grow even if the environmental
    saturation ratio decreases. If the satruation ratio is below 1 (<100% RH),
    then the activated particle will start to evaporate. If the particle
    evaporates below the activation radius, then it will need to be reactivated


    TODO: look at pyrcel's taylor expansion for the activation radius
    test: 50 nm particle, kappa = 0.1, has a crit sat ratio of ~1.003
    """
    def neg_activity(wet_radius):  # negative of the activity
        return -1.0 * particle_effective_activity(
            bulk_activity=particle_phase_h2o_activity(
                dry_radius,
                wet_radius,
                kappa_ccn
            ),
            kelvin_radius=h2o_kelvin_radius(temperature=temperature).magnitude,
            wet_radius=wet_radius
        )

    out = fminbound(
        neg_activity, dry_radius, dry_radius * 1e4, xtol=1e-10,
        full_output=True, disp=0
    )
    radius_critical, saturation_critical = out[:2]
    saturation_critical *= -1.0  # multiply by -1 to undo negative of activity

    return radius_critical, saturation_critical
