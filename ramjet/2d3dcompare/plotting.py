"""
===========================================================
plotting.py

Publication Quality Plotting Module

Author : Vedant Chaudhari
===========================================================
"""

import os
import matplotlib.pyplot as plt

from config import *

# ==========================================================
# COMMON STYLE
# ==========================================================

def apply_style():

    ax = plt.gca()

    # Major Grid
    plt.grid(
        True,
        which='major',
        linestyle='-',
        linewidth=1.8,
        alpha=0.95
    )

    # Minor Grid
    plt.minorticks_on()

    plt.grid(
        True,
        which='minor',
        linestyle='--',
        linewidth=0.8,
        alpha=0.80
    )

    # Axis Thickness
    for spine in ax.spines.values():
        spine.set_linewidth(2)

    # Tick Marks
    ax.tick_params(
        axis='both',
        which='major',
        width=2,
        length=8,
        labelsize=TICK_SIZE
    )

    ax.tick_params(
        axis='both',
        which='minor',
        width=1.5,
        length=5
    )

    plt.tight_layout()


# ==========================================================
# UNIVERSAL PLOT FUNCTION
# ==========================================================

def comparison_plot(
    df2d,
    df3d,
    theory,
    cfd_column,
    theory_column,
    ylabel,
    title,
    save_folder,
    filename
):

    plt.figure(figsize=FIGURE_SIZE)

    # ------------------------------
    # Theory
    # ------------------------------

    plt.plot(

        theory["Length"],

        theory[theory_column],

        color=COLOR_THEORY,

        linestyle=THEORY_LINESTYLE,

        linewidth=LINEWIDTH,

        label="Theory"

    )

    # ------------------------------
    # 2D CFD
    # ------------------------------

    plt.plot(

        df2d["Length"],

        df2d[cfd_column],

        color=COLOR_2D,

        linewidth=LINEWIDTH,

        label="2D CFD"

    )

    # ------------------------------
    # 3D CFD
    # ------------------------------

    plt.plot(

        df3d["Length"],

        df3d[cfd_column],

        color=COLOR_3D,

        linewidth=LINEWIDTH,

        label="3D CFD"

    )

    # ------------------------------

    plt.xlabel(

        "Length (m)",

        fontsize=FONT_SIZE

    )

    plt.ylabel(

        ylabel,

        fontsize=FONT_SIZE

    )

    plt.title(

        title,

        fontsize=TITLE_SIZE

    )

    plt.legend(

        fontsize=12,

        frameon=False

    )

    apply_style()

    plt.savefig(

        os.path.join(

            save_folder,

            filename

        ),

        dpi=FIGURE_DPI

    )

    plt.close()


# ==========================================================
# CENTRELINE
# ==========================================================

def plot_centreline(df2d, df3d, theory):

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Mach",

        "Mach",

        "Mach Number",

        "Centre Line Mach Number",

        CENTRELINE_RESULTS,

        "Mach.png"

    )

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Pressure_Ratio",

        "Pressure_Ratio",

        "P/P₀",

        "Centre Line Pressure Ratio",

        CENTRELINE_RESULTS,

        "PressureRatio.png"

    )

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Temperature_Ratio",

        "Temperature_Ratio",

        "T/T₀",

        "Centre Line Temperature Ratio",

        CENTRELINE_RESULTS,

        "TemperatureRatio.png"

    )

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Density_Ratio",

        "Density_Ratio",

        "ρ/ρ₀",

        "Centre Line Density Ratio",

        CENTRELINE_RESULTS,

        "DensityRatio.png"

    )

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Velocity_Magnitude",

        "Velocity",

        "Velocity (m/s)",

        "Centre Line Velocity",

        CENTRELINE_RESULTS,

        "Velocity.png"

    )


# ==========================================================
# TOP WALL
# ==========================================================

def plot_topwall(df2d, df3d, theory):

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Mach",

        "Mach",

        "Mach Number",

        "Top Wall Mach Number",

        TOPWALL_RESULTS,

        "Mach.png"

    )

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Pressure_Ratio",

        "Pressure_Ratio",

        "P/P₀",

        "Top Wall Pressure Ratio",

        TOPWALL_RESULTS,

        "PressureRatio.png"

    )

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Temperature_Ratio",

        "Temperature_Ratio",

        "T/T₀",

        "Top Wall Temperature Ratio",

        TOPWALL_RESULTS,

        "TemperatureRatio.png"

    )

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Density_Ratio",

        "Density_Ratio",

        "ρ/ρ₀",

        "Top Wall Density Ratio",

        TOPWALL_RESULTS,

        "DensityRatio.png"

    )

    comparison_plot(

        df2d,

        df3d,

        theory,

        "Velocity_Magnitude",

        "Velocity",

        "Velocity (m/s)",

        "Top Wall Velocity",

        TOPWALL_RESULTS,

        "Velocity.png"

    )


# ==========================================================
# END
# ==========================================================