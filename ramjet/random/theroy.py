import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.optimize import fsolve

# =========================================================
# CREATE RESULTS FOLDER
# =========================================================

results_folder = r"C:\Users\VEDANT\Desktop\ramjet\results-new"

os.makedirs(results_folder, exist_ok=True)

# =========================================================
# FILE PATHS
# =========================================================

# ---------------- NO SLIP ----------------

ns_top_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-no-slip-0.4\topwall_values.csv"

ns_bot_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-no-slip-0.4\botwall_values.csv"

# ---------------- SLIP ----------------

s_top_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-slip-0.4\topwall_values.csv"

s_bot_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-slip-0.4\botwall_values.csv"

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
# TARGET THROAT MACH
# =========================================================

M_throat = 0.4

# =========================================================
# CFD PARAMETERS
# =========================================================

datasets = [ns_top, ns_bot, s_top, s_bot]

for df in datasets:

    # Pressure ratio
    df['P_ratio'] = df['Pressure'] / P0

    # Temperature ratio
    df['T_ratio'] = df['Temperature'] / T0

    # Density ratio
    df['rho_ratio'] = (
        df['Density']
        /
        df['Density'].iloc[0]
    )

    # Velocity magnitude
    df['Velocity_Mag'] = np.sqrt(
        (df['Momentum_x'] / df['Density'])**2
        +
        (df['Momentum_y'] / df['Density'])**2
    )

# =========================================================
# THEORETICAL GEOMETRY
# =========================================================

x_theory = np.linspace(0, 2, 500)

h = np.zeros_like(x_theory)

for i, x in enumerate(x_theory):

    if x <= 1.0:

        h[i] = (
            0.36*x**3
            - 0.54*x**2
            + 0.36
        )

    else:

        h[i] = 0.18

# =========================================================
# AREA-MACH RELATION
# =========================================================

def area_mach(M):

    term1 = 1 / M

    term2 = (
        (2/(gamma+1))
        *
        (1 + ((gamma-1)/2)*M**2)
    )

    exponent = (
        (gamma+1)
        /
        (2*(gamma-1))
    )

    return (
        term1
        *
        term2**exponent
    )

# =========================================================
# COMPUTE EFFECTIVE A*
# =========================================================

A_ratio_throat = area_mach(M_throat)

A_star = 0.18 / A_ratio_throat

# =========================================================
# COMPUTE AREA RATIO
# =========================================================

A_ratio = h / A_star

# =========================================================
# SOLVE MACH NUMBER
# =========================================================

def solve_mach(M, A_Astar):

    term1 = 1 / M

    term2 = (
        (2/(gamma+1))
        *
        (1 + ((gamma-1)/2)*M**2)
    )

    exponent = (
        (gamma+1)
        /
        (2*(gamma-1))
    )

    return (
        term1
        *
        term2**exponent
        - A_Astar
    )

Mach_theory = np.zeros_like(x_theory)

for i, A in enumerate(A_ratio):

    Mach_theory[i] = fsolve(
        solve_mach,
        0.2,
        args=(A)
    )[0]

# =========================================================
# THEORETICAL ISENTROPIC RELATIONS
# =========================================================

P_ratio_theory = (
    1 +
    ((gamma-1)/2)
    *
    Mach_theory**2
)**(-gamma/(gamma-1))

T_ratio_theory = (
    1 +
    ((gamma-1)/2)
    *
    Mach_theory**2
)**(-1)

rho_ratio_theory = (
    1 +
    ((gamma-1)/2)
    *
    Mach_theory**2
)**(-1/(gamma-1))

# =========================================================
# THEORETICAL VELOCITY
# =========================================================

T_theory = T_ratio_theory * T0

a_theory = np.sqrt(
    gamma
    *
    R
    *
    T_theory
)

Velocity_theory = Mach_theory * a_theory

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

    # =====================================================
    # THEORETICAL
    # =====================================================

    plt.plot(
        x_theory,
        theory_y,
        linewidth=4,
        color='black',
        label='Theoretical'
    )

    # =====================================================
    # NO SLIP
    # =====================================================

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

    # =====================================================
    # SLIP
    # =====================================================

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

    # =====================================================
    # LABELS
    # =====================================================

    plt.xlabel('Length (m)', fontsize=18)

    plt.ylabel(ylabel, fontsize=18)

    plt.title(title, fontsize=18)

    style_plot()

    # =====================================================
    # SAVE FIGURE
    # =====================================================

    plt.savefig(
        os.path.join(results_folder, filename),
        dpi=600
    )

# =========================================================
# 1. MACH NUMBER
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
# 2. PRESSURE RATIO
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
# 3. TEMPERATURE RATIO
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
# 4. DENSITY RATIO
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
# 5. VELOCITY MAGNITUDE
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

print(f"Target throat Mach = {M_throat}")

print(f"Effective A* = {A_star:.6f}")

print(f"A_throat/A* = {A_ratio_throat:.6f}")

print("Results saved in:")
print(results_folder)

print("===================================")