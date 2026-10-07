import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ============================================================
# USER INPUT
# ============================================================

folder = r"C:\Users\VEDANT\Desktop\ramjet\3d-no-slip"

csv_file = os.path.join(folder, "botwall.csv")

results_folder = os.path.join(folder, "results")

os.makedirs(results_folder, exist_ok=True)

# ============================================================
# TOTAL CONDITIONS
# ============================================================

P0 = 200000.0          # Pa
T0 = 354.0             # K
R = 287.0

rho0 = P0/(R*T0)

# ============================================================
# LOAD DATA
# ============================================================

df = pd.read_csv(csv_file)

print(df.columns)

# ============================================================
# SORT ALONG LINE
# ============================================================

df = df.sort_values(by="arc_length")

# ============================================================
# CALCULATE RATIOS
# ============================================================

df["Pressure_Ratio"] = df["Pressure"]/P0

df["Temperature_Ratio"] = df["Temperature"]/T0

df["Density_Ratio"] = df["Density"]/rho0

# ============================================================
# COMMON STYLE
# ============================================================

def style_plot():

    plt.grid(True, which='major',
             linewidth=1.8,
             alpha=0.9)

    plt.minorticks_on()

    plt.grid(True, which='minor',
             linestyle='--',
             linewidth=0.8,
             alpha=0.8)

    ax = plt.gca()

    for spine in ax.spines.values():
        spine.set_linewidth(2)

    ax.tick_params(axis='both',
                   which='major',
                   width=2,
                   length=8,
                   labelsize=14)

    ax.tick_params(axis='both',
                   which='minor',
                   width=1.5,
                   length=5)

    plt.tight_layout()

# ============================================================
# GENERIC PLOT FUNCTION
# ============================================================

def make_plot(x,
              y,
              xlabel,
              ylabel,
              title,
              filename,
              color):

    plt.figure(figsize=(9,6))

    plt.plot(x,
             y,
             linewidth=3,
             color=color)

    plt.xlabel(xlabel,
               fontsize=18)

    plt.ylabel(ylabel,
               fontsize=18)

    plt.title(title,
              fontsize=18)

    style_plot()

    plt.savefig(
        os.path.join(results_folder, filename),
        dpi=600
    )

# ============================================================
# MACH
# ============================================================

make_plot(df["arc_length"],
          df["Mach"],
          "Length (m)",
          "Mach Number",
          "Centreline Mach Number",
          "Mach.png",
          "blue")

# ============================================================
# PRESSURE RATIO
# ============================================================

make_plot(df["arc_length"],
          df["Pressure_Ratio"],
          "Length (m)",
          "P/P₀",
          "Centreline Pressure Ratio",
          "PressureRatio.png",
          "red")

# ============================================================
# TEMPERATURE RATIO
# ============================================================

make_plot(df["arc_length"],
          df["Temperature_Ratio"],
          "Length (m)",
          "T/T₀",
          "Centreline Temperature Ratio",
          "TemperatureRatio.png",
          "green")

# ============================================================
# DENSITY RATIO
# ============================================================

make_plot(df["arc_length"],
          df["Density_Ratio"],
          "Length (m)",
          "ρ/ρ₀",
          "Centreline Density Ratio",
          "DensityRatio.png",
          "purple")

# ============================================================
# VELOCITY
# ============================================================

make_plot(df["arc_length"],
          df["Velocity_Magnitude"],
          "Length (m)",
          "Velocity Magnitude (m/s)",
          "Centreline Velocity",
          "Velocity.png",
          "black")

# ============================================================
# SAVE CSV
# ============================================================

output_csv = os.path.join(
    results_folder,
    "Processed_Centreline_Data.csv"
)

df.to_csv(output_csv,
          index=False)

print("\n====================================")
print("Plots generated successfully")
print("Results folder:")
print(results_folder)
print("====================================")

plt.show()