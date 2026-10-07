import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import os

# =========================================================
# CREATE RESULTS FOLDER
# =========================================================

results_folder = r"C:\Users\VEDANT\Desktop\ramjet\results"

os.makedirs(results_folder, exist_ok=True)

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

M_throat = 0.95

# =========================================================
# GEOMETRY
# =========================================================

x = np.linspace(0, 2, 500)

h = np.zeros_like(x)

for i, xi in enumerate(x):

    if xi <= 1.0:

        h[i] = (
            0.36*xi**3
            - 0.54*xi**2
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

Mach = np.zeros_like(x)

for i, A in enumerate(A_ratio):

    Mach[i] = fsolve(
        solve_mach,
        0.2,
        args=(A)
    )[0]

# =========================================================
# ISENTROPIC RELATIONS
# =========================================================

P_ratio = (
    1 +
    ((gamma-1)/2)
    *
    Mach**2
)**(-gamma/(gamma-1))

T_ratio = (
    1 +
    ((gamma-1)/2)
    *
    Mach**2
)**(-1)

rho_ratio = (
    1 +
    ((gamma-1)/2)
    *
    Mach**2
)**(-1/(gamma-1))

# =========================================================
# VELOCITY
# =========================================================

T = T_ratio * T0

a = np.sqrt(gamma * R * T)

Velocity = Mach * a

# =========================================================
# COMMON STYLE
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

    plt.tight_layout()

# =========================================================
# 1. MACH NUMBER
# =========================================================

plt.figure(figsize=(9,6))

plt.plot(
    x,
    Mach,
    linewidth=4,
    color='black'
)

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('Mach Number', fontsize=18)
plt.title('Theoretical Mach Number vs Length', fontsize=18)

style_plot()

plt.savefig(
    os.path.join(results_folder, 'Theory_Mach.png'),
    dpi=600
)

# =========================================================
# 2. PRESSURE RATIO
# =========================================================

plt.figure(figsize=(9,6))

plt.plot(
    x,
    P_ratio,
    linewidth=4,
    color='blue'
)

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('P / P₀', fontsize=18)
plt.title('Theoretical Pressure Ratio vs Length', fontsize=18)

style_plot()

plt.savefig(
    os.path.join(results_folder, 'Theory_PressureRatio.png'),
    dpi=600
)

# =========================================================
# 3. TEMPERATURE RATIO
# =========================================================

plt.figure(figsize=(9,6))

plt.plot(
    x,
    T_ratio,
    linewidth=4,
    color='red'
)

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('T / T₀', fontsize=18)
plt.title('Theoretical Temperature Ratio vs Length', fontsize=18)

style_plot()

plt.savefig(
    os.path.join(results_folder, 'Theory_TemperatureRatio.png'),
    dpi=600
)

# =========================================================
# 4. DENSITY RATIO
# =========================================================

plt.figure(figsize=(9,6))

plt.plot(
    x,
    rho_ratio,
    linewidth=4,
    color='green'
)

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('ρ / ρ₀', fontsize=18)
plt.title('Theoretical Density Ratio vs Length', fontsize=18)

style_plot()

plt.savefig(
    os.path.join(results_folder, 'Theory_DensityRatio.png'),
    dpi=600
)

# =========================================================
# 5. VELOCITY
# =========================================================

plt.figure(figsize=(9,6))

plt.plot(
    x,
    Velocity,
    linewidth=4,
    color='purple'
)

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('Velocity Magnitude (m/s)', fontsize=18)
plt.title('Theoretical Velocity vs Length', fontsize=18)

style_plot()

plt.savefig(
    os.path.join(results_folder, 'Theory_Velocity.png'),
    dpi=600
)

# =========================================================
# SHOW ALL
# =========================================================

plt.show()

# =========================================================
# IMPORTANT VALUES
# =========================================================

print("\n===================================")

print(f"Target throat Mach = {M_throat}")

print(f"Effective A* = {A_star:.6f}")

print(f"Physical throat area = 0.18")

print(f"A_throat/A* = {A_ratio_throat:.6f}")

print("===================================")