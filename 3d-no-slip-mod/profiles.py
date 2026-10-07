import pandas as pd
import matplotlib.pyplot as plt
import os

# =====================================================
# DIRECTORY
# =====================================================

folder = r"C:\Users\VEDANT\Desktop\ramjet\3d-no-slip-mod"

results = os.path.join(folder, "results_profiles")

os.makedirs(results, exist_ok=True)

# =====================================================
# TOTAL CONDITIONS
# =====================================================

P0 = 200000.0
T0 = 300.0
R = 287.0

rho0 = P0 / (R * T0)

# =====================================================
# FILES TO LOAD
# =====================================================

files = {
    "1.0 m"  : "1m.csv",
    "1.25 m" : "1.25m.csv",
    "1.5 m"  : "1.5m.csv",
    "1.75 m" : "1.75m.csv",
    "2.0 m"  : "2m.csv",
    "Exit "  : "2.0411m.csv",
}

# =====================================================
# LOAD DATA
# =====================================================

data = {}

for label, fname in files.items():

    path = os.path.join(folder, fname)

    df = pd.read_csv(path)

    df = df.sort_values("Points_1")

    # compute total (stagnation) pressure from static pressure and Mach
    # pt_su2 = p_su2 * (1 + 0.2*mach_su2**2)**3.5 where p_su2 is the "Pressure" column
    df["pt_su2"] = df["Pressure"] * (1 + 0.2 * df["Mach"] ** 2) ** 3.5

    # pressure ratio using computed total pressure instead of raw static pressure
    df["P_ratio"] = df["pt_su2"] / P0

    df["T_ratio"] = df["Temperature"] / T0

    df["rho_ratio"] = df["Density"] / rho0

    data[label] = df

# =====================================================
# PLOT STYLE
# =====================================================

def style():

    plt.grid(
        True,
        which='major',
        linewidth=1.8,
        alpha=0.95
    )

    plt.minorticks_on()

    plt.grid(
        True,
        which='minor',
        linestyle='--',
        linewidth=1.0,
        alpha=0.8
    )

    ax = plt.gca()

    for spine in ax.spines.values():
        spine.set_linewidth(2)

    ax.tick_params(
        axis='both',
        which='major',
        width=2,
        length=8
    )

    ax.tick_params(
        axis='both',
        which='minor',
        width=1.5,
        length=5
    )

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)


# =====================================================
# GENERIC PLOTTER
# =====================================================

def make_plot(column, xlabel, title, filename):

    plt.figure(figsize=(9,7))

    for label, df in data.items():

        plt.plot(
            df[column],
            df["Points_1"],
            linewidth=3,
            label=label
        )

    plt.xlabel(
        xlabel,
        fontsize=18
    )

    plt.ylabel(
        "y (m)",
        fontsize=18
    )

    plt.title(
        title,
        fontsize=18
    )

    style()

    # place legend uniformly outside the plot to avoid overlapping lines
    plt.legend(fontsize=10, loc='upper left', bbox_to_anchor=(1.02, 1))
    plt.tight_layout(rect=[0, 0, 0.85, 1])

    plt.savefig(
        os.path.join(results, filename),
        dpi=600,
        bbox_inches='tight'
    )

# =====================================================
# MACH
# =====================================================

make_plot(
    "Mach",
    "Mach Number",
    "Mach Number Profiles",
    "Mach_Profiles.png"
)

# =====================================================
# PRESSURE RATIO
# =====================================================

make_plot(
    "P_ratio",
    "P/P₀",
    "Pressure Ratio Profiles",
    "PressureRatio_Profiles.png"
)

# =====================================================
# TEMPERATURE RATIO
# =====================================================

make_plot(
    "T_ratio",
    "T/T₀",
    "Temperature Ratio Profiles",
    "TemperatureRatio_Profiles.png"
)

# =====================================================
# DENSITY RATIO
# =====================================================

make_plot(
    "rho_ratio",
    "ρ/ρ₀",
    "Density Ratio Profiles",
    "DensityRatio_Profiles.png"
)

# =====================================================
# VELOCITY
# =====================================================

make_plot(
    "Velocity_Magnitude",
    "Velocity Magnitude (m/s)",
    "Velocity Profiles",
    "VelocityProfiles.png"
)

print("\nProfiles saved in:")
print(results)