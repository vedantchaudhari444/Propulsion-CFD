import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ============================================================
# USER SETTINGS
# ============================================================

INPUT_FILE = "slice.csv"
OUTPUT_FOLDER = "topwall_results"

P0_INLET = 200000.0       # Pa
T0_INLET = 300.0          # K
R = 287.0                 # J/kg-K
GAMMA = 1.4

# Number of axial locations used to identify Topwall
N_X_BINS = 500

# ============================================================
# CREATE OUTPUT FOLDER
# ============================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ============================================================
# READ CSV
# ============================================================

df = pd.read_csv(INPUT_FILE)

# Remove spaces from column names
df.columns = [str(c).strip() for c in df.columns]

print("\nAvailable columns:")
print(df.columns.tolist())

# ============================================================
# AUTOMATIC COLUMN DETECTION
# ============================================================

def find_column(candidates):
    lower_cols = {c.lower(): c for c in df.columns}

    for name in candidates:
        if name.lower() in lower_cols:
            return lower_cols[name.lower()]

    return None


X_col = find_column([
    "Points:0", "Points_0", "x", "X", "CoordinateX"
])

Y_col = find_column([
    "Points:1", "Points_1", "y", "Y", "CoordinateY"
])

Z_col = find_column([
    "Points:2", "Points_2", "z", "Z", "CoordinateZ"
])

Mach_col = find_column([
    "Mach", "Mach_Number", "Ma", "Ma_average"
])

Pressure_col = find_column([
    "Pressure", "StaticPressure", "p", "p_average"
])

Temperature_col = find_column([
    "Temperature", "StaticTemperature", "T", "T_average"
])

Density_col = find_column([
    "Density", "rho", "rho_average", "Rho"
])

Velocity_col = find_column([
    "Velocity_Magnitude",
    "VelocityMagnitude",
    "Velocity",
    "U_Magnitude",
    "U_average_Magnitude"
])

Yplus_col = find_column([
    "y_plus",
    "YPlus",
    "Y_plus",
    "WallYPlus",
    "yplus"
])

# ============================================================
# CHECK REQUIRED COLUMNS
# ============================================================

required = {
    "X": X_col,
    "Y": Y_col,
    "Mach": Mach_col,
    "Pressure": Pressure_col,
    "Temperature": Temperature_col,
    "Density": Density_col,
    "Velocity": Velocity_col,
    "Y+": Yplus_col
}

missing = [name for name, col in required.items() if col is None]

if missing:
    raise ValueError(
        "\nMissing columns: " + ", ".join(missing) +
        "\nCheck the column names printed above."
    )

# ============================================================
# KEEP REQUIRED DATA
# ============================================================

data = pd.DataFrame({
    "x": pd.to_numeric(df[X_col], errors="coerce"),
    "y": pd.to_numeric(df[Y_col], errors="coerce"),
    "Mach": pd.to_numeric(df[Mach_col], errors="coerce"),
    "Pressure": pd.to_numeric(df[Pressure_col], errors="coerce"),
    "Temperature": pd.to_numeric(df[Temperature_col], errors="coerce"),
    "Density": pd.to_numeric(df[Density_col], errors="coerce"),
    "Velocity": pd.to_numeric(df[Velocity_col], errors="coerce"),
    "y_plus": pd.to_numeric(df[Yplus_col], errors="coerce")
})

# Remove invalid coordinates
data = data.dropna(subset=["x", "y"])

# ============================================================
# IDENTIFY TOPWALL
# ============================================================
#
# For each axial x-location:
# choose the point with the maximum y-coordinate.
#
# This follows the curved Topwall.
# ============================================================

x_min = data["x"].min()
x_max = data["x"].max()

dx = (x_max - x_min) / (N_X_BINS - 1)

data["x_bin"] = np.round(
    (data["x"] - x_min) / dx
) * dx + x_min

# Find highest-y point in every x bin
topwall_indices = data.groupby(
    "x_bin"
)["y"].idxmax()

topwall = data.loc[
    topwall_indices
].copy()

topwall = topwall.sort_values(
    "x"
).reset_index(drop=True)

topwall.drop(
    columns=["x_bin"],
    inplace=True
)

# ============================================================
# CALCULATE TOTAL PRESSURE
# ============================================================

topwall["TotalPressure"] = (
    topwall["Pressure"]
    *
    (1 + 0.2 * topwall["Mach"]**2)**3.5
)

# ============================================================
# CALCULATE NORMALIZED QUANTITIES
# ============================================================

rho0 = P0_INLET / (R * T0_INLET)

topwall["P_static_ratio"] = (
    topwall["Pressure"] / P0_INLET
)

topwall["P_total_ratio"] = (
    topwall["TotalPressure"] / P0_INLET
)

topwall["T_ratio"] = (
    topwall["Temperature"] / T0_INLET
)

topwall["rho_ratio"] = (
    topwall["Density"] / rho0
)

# ============================================================
# SAVE TOPWALL DATA
# ============================================================

output_csv = os.path.join(
    OUTPUT_FOLDER,
    "Topwall_Extracted_Data.csv"
)

topwall.to_csv(
    output_csv,
    index=False
)

# ============================================================
# PLOT FUNCTION
# ============================================================

def make_plot(
    ydata,
    ylabel,
    title,
    filename
):

    plt.figure(figsize=(10, 6))

    plt.plot(
        topwall["x"],
        ydata,
        linewidth=2
    )

    plt.xlabel(
        "Axial Distance, x (m)",
        fontsize=14
    )

    plt.ylabel(
        ylabel,
        fontsize=14
    )

    plt.title(
        title,
        fontsize=15
    )

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            OUTPUT_FOLDER,
            filename
        ),
        dpi=300
    )

    plt.close()

# ============================================================
# 1. Y+
# ============================================================

make_plot(
    topwall["y_plus"],
    r"$y^+$",
    r"$y^+$ Distribution Along Topwall",
    "Topwall_yplus.png"
)

# ============================================================
# 2. MACH NUMBER
# ============================================================

make_plot(
    topwall["Mach"],
    "Mach Number",
    "Mach Number Along Topwall",
    "Topwall_Mach.png"
)

# ============================================================
# 3. STATIC PRESSURE
# ============================================================

make_plot(
    topwall["Pressure"] / 1000.0,
    "Static Pressure (kPa)",
    "Static Pressure Along Topwall",
    "Topwall_StaticPressure.png"
)

# ============================================================
# 4. STATIC PRESSURE RATIO
# ============================================================

make_plot(
    topwall["P_static_ratio"],
    r"$P/P_{0,inlet}$",
    "Static Pressure Ratio Along Topwall",
    "Topwall_StaticPressureRatio.png"
)

# ============================================================
# 5. TOTAL PRESSURE
# ============================================================

make_plot(
    topwall["TotalPressure"] / 1000.0,
    "Total Pressure (kPa)",
    "Total Pressure Along Topwall",
    "Topwall_TotalPressure.png"
)

# ============================================================
# 6. TOTAL PRESSURE RATIO
# ============================================================

make_plot(
    topwall["P_total_ratio"],
    r"$P_0/P_{0,inlet}$",
    "Total Pressure Ratio Along Topwall",
    "Topwall_TotalPressureRatio.png"
)

# ============================================================
# 7. STATIC TEMPERATURE
# ============================================================

make_plot(
    topwall["Temperature"],
    "Static Temperature (K)",
    "Static Temperature Along Topwall",
    "Topwall_Temperature.png"
)

# ============================================================
# 8. TEMPERATURE RATIO
# ============================================================

make_plot(
    topwall["T_ratio"],
    r"$T/T_0$",
    "Temperature Ratio Along Topwall",
    "Topwall_TemperatureRatio.png"
)

# ============================================================
# 9. DENSITY
# ============================================================

make_plot(
    topwall["Density"],
    r"Density (kg/m$^3$)",
    "Density Along Topwall",
    "Topwall_Density.png"
)

# ============================================================
# 10. DENSITY RATIO
# ============================================================

make_plot(
    topwall["rho_ratio"],
    r"$\rho/\rho_0$",
    "Density Ratio Along Topwall",
    "Topwall_DensityRatio.png"
)

# ============================================================
# 11. VELOCITY
# ============================================================

make_plot(
    topwall["Velocity"],
    "Velocity Magnitude (m/s)",
    "Velocity Along Topwall",
    "Topwall_Velocity.png"
)

# ============================================================
# DONE
# ============================================================

print("\n==========================================")
print("Topwall extraction completed.")
print("==========================================")

print("\nNumber of Topwall points:", len(topwall))

print("\nTopwall x-range:")
print(topwall["x"].min(), "to", topwall["x"].max(), "m")

print("\nMaximum y+:")
print(topwall["y_plus"].max())

print("\nMinimum y+:")
print(topwall["y_plus"].min())

print("\nAverage y+:")
print(topwall["y_plus"].mean())

print("\nResults saved in:")
print(OUTPUT_FOLDER)