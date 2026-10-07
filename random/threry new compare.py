import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.optimize import fsolve

# =========================================================
# CREATE RESULTS FOLDER
# =========================================================

results_folder = r"C:\Users\VEDANT\Desktop\ramjet\results-0.6"

os.makedirs(results_folder, exist_ok=True)

# =========================================================
# FILE PATHS
# =========================================================

# ---------------- NO SLIP ----------------

ns_top_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-no-slip-0.6\topwall_values.csv"

ns_bot_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-no-slip-0.6\botwall_values.csv"

# ---------------- SLIP ----------------

s_top_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-slip-0.6\topwall_values.csv"

s_bot_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-slip-0.6\botwall_values.csv"

# =========================================================
# LOAD DATA
# =========================================================

ns_top = pd.read_csv(ns_top_file)
ns_bot = pd.read_csv(ns_bot_file)

s_top = pd.read_csv(s_top_file)
s_bot = pd.read_csv(s_bot_file)

# =========================================================
# SORT DATA
# =========================================================

ns_top = ns_top.sort_values(by='x')
ns_bot = ns_bot.sort_values(by='x')

s_top = s_top.sort_values(by='x')
s_bot = s_bot.sort_values(by='x')

# =========================================================
# CONSTANTS
# =========================================================

gamma = 1.4
R = 287.0

P0 = 200000.0
T0 = 354.0

# =========================================================
# TARGET THROAT MACH NUMBER
# =========================================================

M_throat = 0.6

# =========================================================
# THEORETICAL GEOMETRY
# =========================================================

x_theory = np.linspace(0, 2, 600)

h = np.zeros_like(x_theory)

for i, x in enumerate(x_theory):

    # Converging section

    if x <= 1.0:

        h[i] = (
            0.36*x**3
            - 0.54*x**2
            + 0.36
        )

    # Constant area section

    else:

        h[i] = 0.18

# =========================================================
# AREA-MACH RELATION
# =========================================================

def area_ratio_from_mach(M):

    term1 = 1.0 / M

    term2 = (
        (2.0 / (gamma + 1.0))
        *
        (1.0 + ((gamma - 1.0) / 2.0) * M**2)
    )

    exponent = (
        (gamma + 1.0)
        /
        (2.0 * (gamma - 1.0))
    )

    return term1 * (term2 ** exponent)

# =========================================================
# EFFECTIVE SONIC AREA
# =========================================================

A_ratio_throat = area_ratio_from_mach(M_throat)

# Physical throat area
A_throat = 0.18

# Effective sonic area
A_star = A_throat / A_ratio_throat

# =========================================================
# AREA RATIO ALONG DUCT
# =========================================================

A_ratio = h / A_star

# =========================================================
# SOLVE MACH NUMBER
# =========================================================

def mach_equation(M, target_A_ratio):

    return (
        area_ratio_from_mach(M)
        -
        target_A_ratio
    )

Mach_theory = np.zeros_like(x_theory)

for i, A in enumerate(A_ratio):

    # Strongly enforce subsonic branch

    Mach_theory[i] = fsolve(
        mach_equation,
        0.05,
        args=(A)
    )[0]

# =========================================================
# ISENTROPIC RELATIONS
# =========================================================

# Pressure ratio

P_ratio_theory = (
    1.0 +
    ((gamma - 1.0) / 2.0)
    *
    Mach_theory**2
) ** (-gamma / (gamma - 1.0))

# Temperature ratio

T_ratio_theory = (
    1.0 +
    ((gamma - 1.0) / 2.0)
    *
    Mach_theory**2
) ** (-1.0)

# Density ratio

rho_ratio_theory = (
    1.0 +
    ((gamma - 1.0) / 2.0)
    *
    Mach_theory**2
) ** (-1.0 / (gamma - 1.0))

# =========================================================
# STATIC VALUES
# =========================================================

Pressure_theory = P_ratio_theory * P0

Temperature_theory = T_ratio_theory * T0

# =========================================================
# SPEED OF SOUND
# =========================================================

a_theory = np.sqrt(
    gamma
    *
    R
    *
    Temperature_theory
)

# =========================================================
# VELOCITY
# =========================================================

Velocity_theory = Mach_theory * a_theory

# =========================================================
# CFD PARAMETERS
# =========================================================

# Stagnation density

rho0 = P0 / (R * T0)

datasets = [ns_top, ns_bot, s_top, s_bot]

for df in datasets:

    # Pressure ratio
    df['P_ratio'] = df['Pressure'] / P0

    # Temperature ratio
    df['T_ratio'] = df['Temperature'] / T0

    # Correct density ratio
    df['rho_ratio'] = (
        df['Density']
        /
        rho0
    )

    # Velocity magnitude
    df['Velocity_Mag'] = np.sqrt(
        (df['Momentum_x'] / df['Density'])**2
        +
        (df['Momentum_y'] / df['Density'])**2
    )
# =========================================================
# COMMON PLOT STYLE
# =========================================================

def style_plot():

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.grid(
        True,
        which='major',
        linestyle='-',
        linewidth=1.8,
        alpha=0.95
    )

    plt.minorticks_on()

    plt.grid(
        True,
        which='minor',
        linestyle='--',
        linewidth=1.0,
        alpha=0.85
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

    plt.legend(fontsize=11, frameon=False)

    plt.tight_layout()

# =========================================================
# GENERAL COMPARISON FUNCTION
# =========================================================

def comparison_plot(
    theory_y,
    ns_top_y,
    ns_bot_y,
    s_top_y,
    s_bot_y,
    ylabel,
    title,
    filename
):

    plt.figure(figsize=(10,6))

    # ---------------- THEORY ----------------

    plt.plot(
        x_theory,
        theory_y,
        linewidth=4,
        color='black',
        label='Theoretical'
    )

    # ---------------- NO SLIP ----------------

    plt.plot(
        ns_top['x'],
        ns_top_y,
        linewidth=3,
        color='blue',
        label='Top Wall (No Slip)'
    )

    plt.plot(
        ns_bot['x'],
        ns_bot_y,
        linewidth=3,
        linestyle='--',
        color='red',
        label='Centre Line (No Slip)'
    )

    # ---------------- SLIP ----------------

    plt.plot(
        s_top['x'],
        s_top_y,
        linewidth=3,
        color='green',
        label='Top Wall (Slip)'
    )

    plt.plot(
        s_bot['x'],
        s_bot_y,
        linewidth=3,
        linestyle='--',
        color='purple',
        label='Centre Line (Slip)'
    )

    plt.xlabel('Length (m)', fontsize=18)

    plt.ylabel(ylabel, fontsize=18)

    plt.title(title, fontsize=18)

    style_plot()

    plt.savefig(
        os.path.join(results_folder, filename),
        dpi=600
    )

# =========================================================
# MACH NUMBER
# =========================================================

comparison_plot(
    Mach_theory,
    ns_top['Mach'],
    ns_bot['Mach'],
    s_top['Mach'],
    s_bot['Mach'],
    'Mach Number',
    'Mach Number Comparison',
    'Mach_Comparison.png'
)

# =========================================================
# PRESSURE RATIO
# =========================================================

comparison_plot(
    P_ratio_theory,
    ns_top['P_ratio'],
    ns_bot['P_ratio'],
    s_top['P_ratio'],
    s_bot['P_ratio'],
    'P / P₀',
    'Pressure Ratio Comparison',
    'PressureRatio_Comparison.png'
)

# =========================================================
# TEMPERATURE RATIO
# =========================================================

comparison_plot(
    T_ratio_theory,
    ns_top['T_ratio'],
    ns_bot['T_ratio'],
    s_top['T_ratio'],
    s_bot['T_ratio'],
    'T / T₀',
    'Temperature Ratio Comparison',
    'TemperatureRatio_Comparison.png'
)

# =========================================================
# DENSITY RATIO
# =========================================================

comparison_plot(
    rho_ratio_theory,
    ns_top['rho_ratio'],
    ns_bot['rho_ratio'],
    s_top['rho_ratio'],
    s_bot['rho_ratio'],
    'ρ / ρ₀',
    'Density Ratio Comparison',
    'DensityRatio_Comparison.png'
)

# =========================================================
# VELOCITY
# =========================================================

comparison_plot(
    Velocity_theory,
    ns_top['Velocity_Mag'],
    ns_bot['Velocity_Mag'],
    s_top['Velocity_Mag'],
    s_bot['Velocity_Mag'],
    'Velocity Magnitude (m/s)',
    'Velocity Comparison',
    'Velocity_Comparison.png'
)

# =========================================================
# SHOW ALL
# =========================================================

plt.show()

# =========================================================
# IMPORTANT OUTPUTS
# =========================================================

print("\n===================================")

print(f"Target throat Mach number = {M_throat}")

print(f"A_throat/A* = {A_ratio_throat:.6f}")

print(f"Effective sonic area A* = {A_star:.6f}")

print(f"Theoretical outlet pressure = {P_ratio_theory[-1]*P0:.2f} Pa")

print("Results saved in:")
print(results_folder)

print("===================================")