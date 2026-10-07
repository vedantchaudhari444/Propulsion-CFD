import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =========================================================
# FILE PATHS
# =========================================================

top_file = r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\topwall_values.csv"

bot_file = r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\botwall_values.csv"

# =========================================================
# LOAD DATA
# =========================================================

top = pd.read_csv(top_file)
bot = pd.read_csv(bot_file)

# =========================================================
# SORT DATA
# =========================================================

top = top.sort_values(by='x')
bot = bot.sort_values(by='x')

# =========================================================
# REFERENCE VALUES
# =========================================================

P0 = 200000.0      # 2 bar in Pa
T0 = 354.0         # Kelvin

# =========================================================
# COMPUTE PARAMETERS
# =========================================================

top['P_ratio'] = top['Pressure'] / P0
bot['P_ratio'] = bot['Pressure'] / P0

top['T_ratio'] = top['Temperature'] / T0
bot['T_ratio'] = bot['Temperature'] / T0

# =========================================================
# VELOCITY MAGNITUDE
# =========================================================

top['Velocity_Mag'] = np.sqrt(
    (top['Momentum_x'] / top['Density'])**2 +
    (top['Momentum_y'] / top['Density'])**2
)

bot['Velocity_Mag'] = np.sqrt(
    (bot['Momentum_x'] / bot['Density'])**2 +
    (bot['Momentum_y'] / bot['Density'])**2
)

# =========================================================
# COMMON PLOT STYLE FUNCTION
# =========================================================

def style_plot():

    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    plt.grid(
        True,
        which='major',
        linestyle='-',
        linewidth=1.5,
        alpha=0.9
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

    plt.legend(fontsize=14, frameon=False)

    plt.tight_layout()

# =========================================================
# 1. MACH NUMBER VS LENGTH
# =========================================================

plt.figure(figsize=(8,6))

plt.plot(top['x'], top['Mach'],
         linewidth=3,
         color='blue',
         label='Top Wall')

plt.plot(bot['x'], bot['Mach'],
         linewidth=3,
         linestyle='--',
         color='red',
         label='Bottom Wall')

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('Mach Number', fontsize=18)

style_plot()

plt.savefig(
    r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\Mach_vs_Length.png",
    dpi=600
)

# =========================================================
# 2. PRESSURE RATIO VS LENGTH
# =========================================================

plt.figure(figsize=(8,6))

plt.plot(top['x'], top['P_ratio'],
         linewidth=3,
         color='blue',
         label='Top Wall')

plt.plot(bot['x'], bot['P_ratio'],
         linewidth=3,
         linestyle='--',
         color='red',
         label='Bottom Wall')

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('P / P₀', fontsize=18)

style_plot()

plt.savefig(
    r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\PressureRatio_vs_Length.png",
    dpi=600
)

# =========================================================
# 3. TEMPERATURE RATIO VS LENGTH
# =========================================================

plt.figure(figsize=(8,6))

plt.plot(top['x'], top['T_ratio'],
         linewidth=3,
         color='blue',
         label='Top Wall')

plt.plot(bot['x'], bot['T_ratio'],
         linewidth=3,
         linestyle='--',
         color='red',
         label='Bottom Wall')

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('T / T₀', fontsize=18)

style_plot()

plt.savefig(
    r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\TemperatureRatio_vs_Length.png",
    dpi=600
)

# =========================================================
# 4. DENSITY VS LENGTH
# =========================================================

plt.figure(figsize=(8,6))

plt.plot(top['x'], top['Density'],
         linewidth=3,
         color='blue',
         label='Top Wall')

plt.plot(bot['x'], bot['Density'],
         linewidth=3,
         linestyle='--',
         color='red',
         label='Bottom Wall')

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('Density (kg/m³)', fontsize=18)

style_plot()

plt.savefig(
    r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\Density_vs_Length.png",
    dpi=600
)

# =========================================================
# 5. VELOCITY MAGNITUDE VS LENGTH
# =========================================================

plt.figure(figsize=(8,6))

plt.plot(top['x'], top['Velocity_Mag'],
         linewidth=3,
         color='blue',
         label='Top Wall')

plt.plot(bot['x'], bot['Velocity_Mag'],
         linewidth=3,
         linestyle='--',
         color='red',
         label='Bottom Wall')

plt.xlabel('Length (m)', fontsize=18)
plt.ylabel('Velocity Magnitude (m/s)', fontsize=18)

style_plot()

plt.savefig(
    r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\Velocity_vs_Length.png",
    dpi=600
)

# =========================================================
# SHOW ALL
# =========================================================

plt.show()