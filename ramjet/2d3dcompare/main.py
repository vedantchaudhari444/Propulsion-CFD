"""
===========================================================
main.py

2D vs 3D CFD Comparison

Run only this file.

Author : Vedant Chaudhari
===========================================================
"""

import pandas as pd

from reader import load_all
from theory import theoretical_solution
from theory import outlet_mach
from theory import sonic_area

from plotting import plot_centreline
from plotting import plot_topwall

from config import *

# ==========================================================
# LOAD CFD DATA
# ==========================================================

print("\n----------------------------------------")
print("Reading CFD files...")
print("----------------------------------------")

data = load_all()

centre2d = data["CentreLine_2D"]
centre3d = data["CentreLine_3D"]

top2d = data["TopWall_2D"]
top3d = data["TopWall_3D"]

print("Done.\n")

# ==========================================================
# THEORY
# ==========================================================

print("----------------------------------------")
print("Calculating theoretical solution...")
print("----------------------------------------")

theory = theoretical_solution()

print("Done.\n")

# ==========================================================
# PLOTS
# ==========================================================

print("----------------------------------------")
print("Generating Centre Line plots...")
print("----------------------------------------")

plot_centreline(

    centre2d,

    centre3d,

    theory

)

print("Done.\n")

print("----------------------------------------")
print("Generating Top Wall plots...")
print("----------------------------------------")

plot_topwall(

    top2d,

    top3d,

    theory

)

print("Done.\n")

# ==========================================================
# SAVE CFD DATA
# ==========================================================

print("----------------------------------------")
print("Saving processed data...")
print("----------------------------------------")

centre2d.to_csv(

    PROCESSED_DATA +
    r"\CentreLine_2D.csv",

    index=False

)

centre3d.to_csv(

    PROCESSED_DATA +
    r"\CentreLine_3D.csv",

    index=False

)

top2d.to_csv(

    PROCESSED_DATA +
    r"\TopWall_2D.csv",

    index=False

)

top3d.to_csv(

    PROCESSED_DATA +
    r"\TopWall_3D.csv",

    index=False

)

pd.DataFrame(theory).to_csv(

    PROCESSED_DATA +
    r"\Theory.csv",

    index=False

)

print("Done.\n")

# ==========================================================
# SUMMARY
# ==========================================================

print("=======================================================")
print("              CFD COMPARISON COMPLETED")
print("=======================================================\n")

print(f"Outlet Mach Number        : {outlet_mach():.6f}")

print(f"Effective Sonic Area A*   : {sonic_area():.6f} m²")

print(f"Theoretical Points        : {len(theory['Length'])}")

print("\nResults saved in:\n")

print(CENTRELINE_RESULTS)

print(TOPWALL_RESULTS)

print(PROCESSED_DATA)

print("\n=======================================================")