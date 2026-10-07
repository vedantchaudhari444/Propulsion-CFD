"""
===========================================================
reader.py

Reads both 2D and 3D SU2 CSV files automatically.

Author : Vedant Chaudhari
===========================================================
"""

import pandas as pd
import numpy as np

from config import *

# ==========================================================
# INTERNAL FUNCTIONS
# ==========================================================

def _compute_2d_properties(df):
    """
    Compute missing flow properties for 2D CSV files.
    """

    # ------------------------------------------------------
    # Pressure
    # ------------------------------------------------------

    if "Pressure" not in df.columns:

        kinetic = (
            df["Momentum_x"]**2 +
            df["Momentum_y"]**2
        ) / df["Density"]

        df["Pressure"] = (
            GAMMA - 1.0
        ) * (
            df["Energy"] - 0.5 * kinetic
        )

    # ------------------------------------------------------
    # Temperature
    # ------------------------------------------------------

    if "Temperature" not in df.columns:

        df["Temperature"] = (
            df["Pressure"] /
            (df["Density"] * R)
        )

    # ------------------------------------------------------
    # Velocity
    # ------------------------------------------------------

    if "Velocity_Magnitude" not in df.columns:

        u = df["Momentum_x"] / df["Density"]

        v = df["Momentum_y"] / df["Density"]

        df["Velocity_Magnitude"] = np.sqrt(
            u**2 + v**2
        )

    # ------------------------------------------------------
    # Mach
    # ------------------------------------------------------

    if "Mach" not in df.columns:

        a = np.sqrt(
            GAMMA *
            R *
            df["Temperature"]
        )

        df["Mach"] = (
            df["Velocity_Magnitude"] / a
        )

    return df


# ==========================================================
# COMMON RATIOS
# ==========================================================

def _compute_ratios(df):

    df["Pressure_Ratio"] = (
        df["Pressure"] / P0
    )

    df["Temperature_Ratio"] = (
        df["Temperature"] / T0
    )

    df["Density_Ratio"] = (
        df["Density"] / RHO0
    )

    return df


# ==========================================================
# PUBLIC FUNCTION
# ==========================================================

def load_csv(file_path):
    """
    Automatically reads either

    2D CSV

    OR

    3D CSV

    Returns a clean dataframe ready for plotting.
    """

    df = pd.read_csv(file_path)

    # ------------------------------------------------------
    # Detect file type
    # ------------------------------------------------------

    if "arc_length" in df.columns:

        print("Detected : 3D CSV")

        df = df.sort_values(
            by="arc_length"
        )

        df["Length"] = df["arc_length"]

    else:

        print("Detected : 2D CSV")

        df = df.sort_values(
            by="x"
        )

        df["Length"] = df["x"]

        df = _compute_2d_properties(df)

    # ------------------------------------------------------
    # Ratios
    # ------------------------------------------------------

    df = _compute_ratios(df)

    # ------------------------------------------------------
    # Reset index
    # ------------------------------------------------------

    df.reset_index(
        drop=True,
        inplace=True
    )

    return df


# ==========================================================
# LOAD ALL FILES
# ==========================================================

def load_all():

    data = {}

    data["TopWall_2D"] = load_csv(
        TOPWALL_2D
    )

    data["TopWall_3D"] = load_csv(
        TOPWALL_3D
    )

    data["CentreLine_2D"] = load_csv(
        CENTRELINE_2D
    )

    data["CentreLine_3D"] = load_csv(
        CENTRELINE_3D
    )

    return data


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    data = load_all()

    print()

    for key in data:

        print("--------------------------------")

        print(key)

        print(data[key].head())

        print()