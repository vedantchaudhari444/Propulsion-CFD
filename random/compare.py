import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# =========================================================
# CREATE RESULTS FOLDER
# =========================================================

results_folder = r"C:\Users\VEDANT\Desktop\ramjet\results-new"

os.makedirs(results_folder, exist_ok=True)

# =========================================================
# FILE PATHS
# =========================================================

# -------- NO SLIP --------

ns_top_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-no-slip-0.4\topwall_values.csv"

ns_bot_file = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-no-slip-0.4\botwall_values.csv"

# -------- SLIP --------

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
# REFERENCE VALUES
# =========================================================

P0 = 200000.0
T0 = 354.0

# =========================================================
# COMPUTE PARAMETERS
# =========================================================

datasets = [ns_top, ns_bot, s_top, s_bot]

for df in datasets:

    df['P_ratio'] = df['Pressure'] / P0

    df['T_ratio'] = df['Temperature'] / T0

    df['Velocity_Mag'] = np.sqrt(
        (df['Momentum_x'] / df['Density'])**2 +
        (df['Momentum_y'] / df['Density'])**2
    )

# =========================================================
# COMMON STYLE FUNCTION
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

    plt.legend(fontsize=12, frameon=False)

    plt.tight_layout()

# =========================================================
# GENERAL PLOT FUNCTION
# =========================================================

def comparison_plot(
    top_ns,
    bot_ns,
    top_s,
    bot_s,
    ylabel,
    title,
    filename
):

    plt.figure(figsize=(9,6))

    # ---------------- NO SLIP ----------------

    plt.plot(
        ns_top['x'],
        top_ns,
        linewidth=3,
        color='blue',
        label='Top Wall (No Slip)'
    )

    plt.plot(
        ns_bot['x'],
        bot_ns,
        linewidth=3,
        linestyle='--',
        color='red',
        label='Centre Line (No Slip)'
    )

    # ---------------- SLIP ----------------

    plt.plot(
        s_top['x'],
        top_s,
        linewidth=3,
        color='green',
        label='Top Wall (Slip)'
    )

    plt.plot(
        s_bot['x'],
        bot_s,
        linewidth=3,
        linestyle='--',
        color='black',
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
# 1. MACH NUMBER
# =========================================================

comparison_plot(
    ns_top['Mach'],
    ns_bot['Mach'],
    s_top['Mach'],
    s_bot['Mach'],
    'Mach Number',
    'Mach Number vs Length',
    'Mach_Comparison.png'
)

# =========================================================
# 2. PRESSURE RATIO
# =========================================================

comparison_plot(
    ns_top['P_ratio'],
    ns_bot['P_ratio'],
    s_top['P_ratio'],
    s_bot['P_ratio'],
    'P / P₀',
    'Pressure Ratio vs Length',
    'PressureRatio_Comparison.png'
)

# =========================================================
# 3. TEMPERATURE RATIO
# =========================================================

comparison_plot(
    ns_top['T_ratio'],
    ns_bot['T_ratio'],
    s_top['T_ratio'],
    s_bot['T_ratio'],
    'T / T₀',
    'Temperature Ratio vs Length',
    'TemperatureRatio_Comparison.png'
)

# =========================================================
# 4. DENSITY
# =========================================================

comparison_plot(
    ns_top['Density'],
    ns_bot['Density'],
    s_top['Density'],
    s_bot['Density'],
    'Density (kg/m³)',
    'Density vs Length',
    'Density_Comparison.png'
)

# =========================================================
# 5. VELOCITY MAGNITUDE
# =========================================================

comparison_plot(
    ns_top['Velocity_Mag'],
    ns_bot['Velocity_Mag'],
    s_top['Velocity_Mag'],
    s_bot['Velocity_Mag'],
    'Velocity Magnitude (m/s)',
    'Velocity Magnitude vs Length',
    'Velocity_Comparison.png'
)

# =========================================================
# SHOW ALL PLOTS
# =========================================================

plt.show()

print("\n===================================")
print("ALL COMPARISON PLOTS CREATED")
print("Saved in:")
print(results_folder)
print("===================================")