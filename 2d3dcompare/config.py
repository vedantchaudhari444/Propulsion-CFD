"""
===========================================================
CFD 2D vs 3D Comparison
Configuration File

Author : Vedant Chaudhari
===========================================================
"""

import os

# ==========================================================
# PROJECT DIRECTORY
# ==========================================================

PROJECT_FOLDER = r"C:\Users\VEDANT\Desktop\ramjet\2d3dcompare"

# ==========================================================
# INPUT FILES
# ==========================================================

TOPWALL_2D = os.path.join(PROJECT_FOLDER, "topwall_2d.csv")
TOPWALL_3D = os.path.join(PROJECT_FOLDER, "topwall_3d.csv")

CENTRELINE_2D = os.path.join(PROJECT_FOLDER, "botwall_2d.csv")
CENTRELINE_3D = os.path.join(PROJECT_FOLDER, "botwall_3d.csv")

# ==========================================================
# OUTPUT DIRECTORY
# ==========================================================

RESULTS_FOLDER = os.path.join(PROJECT_FOLDER, "Results")

CENTRELINE_RESULTS = os.path.join(RESULTS_FOLDER, "CentreLine")
TOPWALL_RESULTS = os.path.join(RESULTS_FOLDER, "TopWall")
PROCESSED_DATA = os.path.join(RESULTS_FOLDER, "ProcessedData")

# ==========================================================
# CREATE OUTPUT FOLDERS
# ==========================================================

os.makedirs(CENTRELINE_RESULTS, exist_ok=True)
os.makedirs(TOPWALL_RESULTS, exist_ok=True)
os.makedirs(PROCESSED_DATA, exist_ok=True)

# ==========================================================
# FLOW PROPERTIES
# ==========================================================

GAMMA = 1.4

R = 287.0

# ==========================================================
# TOTAL CONDITIONS
# ==========================================================

P0 = 200000.0          # Pa

T0 = 354.0             # Kelvin

# ==========================================================
# OUTLET STATIC PRESSURE
# ==========================================================

P_OUTLET = 111800.0

# ==========================================================
# STAGNATION DENSITY
# ==========================================================

RHO0 = P0 / (R * T0)

# ==========================================================
# GEOMETRY
# ==========================================================

INLET_HEIGHT = 0.36

THROAT_HEIGHT = 0.18

DUCT_THICKNESS = 0.36

CONVERGING_LENGTH = 1.0

TOTAL_LENGTH = 2.0

# ==========================================================
# THEORY SETTINGS
# ==========================================================

NUMBER_OF_THEORY_POINTS = 600

# ==========================================================
# PLOT SETTINGS
# ==========================================================

FIGURE_SIZE = (9, 6)

FIGURE_DPI = 600

LINEWIDTH = 3

FONT_SIZE = 16

TITLE_SIZE = 18

TICK_SIZE = 13

# ==========================================================
# CFD LINE COLORS
# ==========================================================

COLOR_2D = "blue"

COLOR_3D = "red"

COLOR_THEORY = "black"

THEORY_LINESTYLE = "--"