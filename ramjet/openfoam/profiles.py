import pandas as pd
import matplotlib.pyplot as plt
import os

# =====================================================
# DIRECTORY
# =====================================================

folder = r"C:\Users\VEDANT\Desktop\ramjet\openfoam"
su2_folder = r"C:\Users\VEDANT\Desktop\ramjet\3d-no-slip-mod"

results = os.path.join(folder, "results_profiles")
os.makedirs(results, exist_ok=True)

# =====================================================
# TOTAL CONDITIONS
# =====================================================

P0 = 200000.0       # Inlet total pressure (Pa)
T0 = 300.0          # Inlet total temperature (K)
R = 287.0           # Gas constant (J/kg-K)

rho0 = P0 / (R * T0)

# =====================================================
# FILES TO LOAD
# =====================================================

files = {
    "1.0 m": {"openfoam": "1m.csv", "su2": "1m.csv"},
    "1.25 m": {"openfoam": "1.25m.csv", "su2": "1.25m.csv"},
    "1.5 m": {"openfoam": "1.5m.csv", "su2": "1.5m.csv"},
    "1.75 m": {"openfoam": "1.75.csv", "su2": "1.75m.csv"},
    "2.0 m": {"openfoam": "2m.csv", "su2": "2m.csv"},
    "Exit": {"openfoam": "2.0411m.csv", "su2": "2.0411m.csv"},
}

# =====================================================
# POSSIBLE COLUMN NAMES
# =====================================================

column_candidates = {
    "y": ["Points_1", "y", "Y", "CoordinateY"],
    "Mach": ["Ma_average", "Mach", "Mach_Number"],
    "Pressure": ["p_average", "Pressure", "StaticPressure"],
    "Temperature": ["T_average", "Temperature", "StaticTemperature"],
    "Density": ["rho_average", "Density", "Rho"],
    "Velocity": [
        "U_average_Magnitude",
        "Velocity_Magnitude",
        "Velocity",
        "VelocityMagnitude",
    ],
}

# =====================================================
# FIND COLUMNS
# =====================================================

def resolve_columns(raw, path):

    available = {
        str(column).strip().lower(): column
        for column in raw.columns
    }

    resolved = {}
    missing = []

    for quantity, candidates in column_candidates.items():

        match = next(
            (
                available[candidate.lower()]
                for candidate in candidates
                if candidate.lower() in available
            ),
            None,
        )

        if match is None:
            missing.append(
                f"{quantity} ({', '.join(candidates)})"
            )
        else:
            resolved[quantity] = match

    if missing:

        available_names = ", ".join(
            str(column) for column in raw.columns
        )

        raise ValueError(
            f"Missing required columns in {path}: "
            f"{', '.join(missing)}. "
            f"Available columns: {available_names}"
        )

    return resolved


# =====================================================
# LOAD DATA
# =====================================================

data = {
    "openfoam": {},
    "su2": {}
}

for label, fname in files.items():

    for solver, solver_folder in (
        ("openfoam", folder),
        ("su2", su2_folder)
    ):

        path = os.path.join(
            solver_folder,
            fname[solver]
        )

        raw = pd.read_csv(path)

        source_columns = resolve_columns(
            raw,
            path
        )

        # Sort according to y-coordinate
        raw = raw.sort_values(
            source_columns["y"]
        )

        df = pd.DataFrame({

            "y":
                raw[source_columns["y"]],

            "Mach":
                raw[source_columns["Mach"]],

            "Pressure":
                raw[source_columns["Pressure"]],

            "Temperature":
                raw[source_columns["Temperature"]],

            "Density":
                raw[source_columns["Density"]],

            "Velocity":
                raw[source_columns["Velocity"]],
        })

        # =================================================
        # STATIC PRESSURE RATIO
        #
        # P / P0_inlet
        # =================================================

        df["P_static_ratio"] = (
            df["Pressure"] / P0
        )

        # =================================================
        # TOTAL PRESSURE
        #
        # P0 = P(1 + 0.2 M^2)^3.5
        # =================================================

        df["TotalPressure"] = (
            df["Pressure"]
            *
            (1 + 0.2 * df["Mach"] ** 2) ** 3.5
        )

        # =================================================
        # TOTAL PRESSURE RATIO
        #
        # P0_local / P0_inlet
        # =================================================

        df["P_total_ratio"] = (
            df["TotalPressure"] / P0
        )

        # =================================================
        # TEMPERATURE RATIO
        # =================================================

        df["T_ratio"] = (
            df["Temperature"] / T0
        )

        # =================================================
        # DENSITY RATIO
        # =================================================

        df["rho_ratio"] = (
            df["Density"] / rho0
        )

        data[solver][label] = df


# =====================================================
# PLOT STYLE
# =====================================================

def style():

    plt.grid(
        True,
        which="major",
        linewidth=1.8,
        alpha=0.95
    )

    plt.minorticks_on()

    plt.grid(
        True,
        which="minor",
        linestyle="--",
        linewidth=1.0,
        alpha=0.8
    )

    ax = plt.gca()

    for spine in ax.spines.values():
        spine.set_linewidth(2)

    ax.tick_params(
        axis="both",
        which="major",
        width=2,
        length=8
    )

    ax.tick_params(
        axis="both",
        which="minor",
        width=1.5,
        length=5
    )

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)


# =====================================================
# GENERIC PLOTTER
# =====================================================

def make_plot(
    column,
    xlabel,
    title,
    filename
):

    plt.figure(figsize=(13, 9))

    colors = plt.get_cmap(
        "tab10"
    ).colors

    for index, label in enumerate(files):

        color = colors[
            index % len(colors)
        ]

        openfoam_df = data[
            "openfoam"
        ][label]

        su2_df = data[
            "su2"
        ][label]

        # ---------------------------------------------
        # OpenFOAM
        # Open circles
        # ---------------------------------------------

        plt.plot(
            openfoam_df[column],
            openfoam_df["y"],

            linestyle="None",

            marker="o",

            markersize=4.5,

            markerfacecolor="none",

            markeredgewidth=1.2,

            markevery=max(
                1,
                len(openfoam_df) // 30
            ),

            color=color,

            label=f"{label} OpenFOAM"
        )

        # ---------------------------------------------
        # SU2
        # Continuous line
        # ---------------------------------------------

        plt.plot(
            su2_df[column],
            su2_df["y"],

            linewidth=2,

            linestyle="-",

            color=color,

            label=f"{label} SU2"
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

    plt.legend(
        fontsize=10,
        ncol=2,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.12),
        columnspacing=1.2,
        handlelength=2.5
    )

    plt.tight_layout(
        rect=[0, 0.08, 1, 1]
    )

    plt.savefig(
        os.path.join(
            results,
            filename
        ),
        dpi=600,
        bbox_inches="tight"
    )

    plt.close()


# =====================================================
# 1. MACH NUMBER
# =====================================================

make_plot(
    "Mach",
    "Mach Number",
    "Mach Number Profiles",
    "Mach_Profiles.png"
)


# =====================================================
# 2. STATIC PRESSURE RATIO
# =====================================================

make_plot(
    "P_static_ratio",
    "P/P₀,inlet",
    "Static Pressure Ratio Profiles",
    "StaticPressureRatio_Profiles.png"
)


# =====================================================
# 3. TOTAL PRESSURE RATIO
# =====================================================

make_plot(
    "P_total_ratio",
    "P₀/P₀,inlet",
    "Total Pressure Ratio Profiles",
    "TotalPressureRatio_Profiles.png"
)


# =====================================================
# 4. TEMPERATURE RATIO
# =====================================================

make_plot(
    "T_ratio",
    "T/T₀",
    "Temperature Ratio Profiles",
    "TemperatureRatio_Profiles.png"
)


# =====================================================
# 5. DENSITY RATIO
# =====================================================

make_plot(
    "rho_ratio",
    "ρ/ρ₀",
    "Density Ratio Profiles",
    "DensityRatio_Profiles.png"
)


# =====================================================
# 6. VELOCITY
# =====================================================

make_plot(
    "Velocity",
    "Velocity Magnitude (m/s)",
    "Velocity Profiles",
    "VelocityProfiles.png"
)


# =====================================================
# FINISHED
# =====================================================

print("\nAll profiles generated successfully.")
print("Results saved in:")
print(results)