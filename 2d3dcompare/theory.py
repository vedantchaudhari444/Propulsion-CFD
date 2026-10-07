"""
===========================================================
theory.py

Computes theoretical isentropic flow properties
for the converging duct.

Author : Vedant Chaudhari
===========================================================
"""

import numpy as np
from scipy.optimize import fsolve

from config import *

# ==========================================================
# DUCT GEOMETRY
# ==========================================================

def duct_height(x):
    """
    Returns duct height (m)
    """

    x = np.asarray(x)

    return np.where(
        x <= CONVERGING_LENGTH,
        0.36*x**3 - 0.54*x**2 + 0.36,
        THROAT_HEIGHT
    )


# ==========================================================
# CROSS-SECTIONAL AREA
# ==========================================================

def duct_area(x):
    """
    Cross-sectional area (m²)
    """

    return duct_height(x) * DUCT_THICKNESS


# ==========================================================
# ISENTROPIC AREA-MACH RELATION
# ==========================================================

def area_ratio(M):

    term1 = 1.0 / M

    term2 = (
        (2.0 / (GAMMA + 1.0))
        *
        (1.0 + ((GAMMA - 1.0) / 2.0) * M**2)
    )

    exponent = (
        (GAMMA + 1.0)
        /
        (2.0 * (GAMMA - 1.0))
    )

    return term1 * term2**exponent


# ==========================================================
# OUTLET MACH NUMBER
# ==========================================================

def outlet_mach():

    pressure_ratio = P_OUTLET / P0

    def equation(M):

        return (
            (1.0 + ((GAMMA - 1.0)/2.0)*M**2)
            **
            (-GAMMA/(GAMMA-1.0))
            -
            pressure_ratio
        )

    M = fsolve(equation,0.9)[0]

    return float(M)


# ==========================================================
# EFFECTIVE SONIC AREA
# ==========================================================

def sonic_area():

    M_exit = outlet_mach()

    throat_area = THROAT_HEIGHT * DUCT_THICKNESS

    Astar = throat_area / area_ratio(M_exit)

    return Astar


# ==========================================================
# MACH DISTRIBUTION
# ==========================================================

def mach_distribution():

    x = np.linspace(
        0,
        TOTAL_LENGTH,
        NUMBER_OF_THEORY_POINTS
    )

    area = duct_area(x)

    Astar = sonic_area()

    ratio = area / Astar

    Mach = np.zeros_like(x)

    guess = 0.2

    for i in range(len(x)):

        def equation(M):

            return area_ratio(M) - ratio[i]

        Mach[i] = fsolve(
            equation,
            guess
        )[0]

        guess = Mach[i]

    return x, Mach


# ==========================================================
# COMPLETE THEORY
# ==========================================================

def theoretical_solution():

    x, Mach = mach_distribution()

    PressureRatio = (
        1.0
        +
        ((GAMMA-1.0)/2.0)
        *
        Mach**2
    ) ** (-GAMMA/(GAMMA-1.0))

    TemperatureRatio = (
        1.0
        +
        ((GAMMA-1.0)/2.0)
        *
        Mach**2
    ) ** (-1.0)

    DensityRatio = (
        1.0
        +
        ((GAMMA-1.0)/2.0)
        *
        Mach**2
    ) ** (-1.0/(GAMMA-1.0))

    Pressure = PressureRatio * P0

    Temperature = TemperatureRatio * T0

    Density = DensityRatio * RHO0

    SpeedOfSound = np.sqrt(
        GAMMA
        *
        R
        *
        Temperature
    )

    Velocity = Mach * SpeedOfSound

    return {

        "Length": x,

        "Mach": Mach,

        "Pressure": Pressure,

        "Temperature": Temperature,

        "Density": Density,

        "Velocity": Velocity,

        "Pressure_Ratio": PressureRatio,

        "Temperature_Ratio": TemperatureRatio,

        "Density_Ratio": DensityRatio

    }


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    theory = theoretical_solution()

    print()

    print("--------------------------------")

    print("Outlet Mach Number")

    print(outlet_mach())

    print()

    print("Effective Sonic Area")

    print(sonic_area())

    print()

    print("First Five Mach Values")

    print(theory["Mach"][:5])