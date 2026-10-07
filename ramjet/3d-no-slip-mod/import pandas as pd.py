import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# Read files
# ==========================
of = pd.read_csv("Axial_p2000_noz_3d_0.4_0.7s.csv")
su2 = pd.read_csv("centerline.csv")

# ==========================
# Downsample OpenFOAM (faster plotting)
# ==========================
step = max(1, len(of)//3000)      # keep about 3000 points
of = of.iloc[::step].reset_index(drop=True)

# ==========================
# Constants
# ==========================
P0 = 200000.0
T0 = 300.0
rho0 = 2.32288
gamma = 1.4

# ==========================
# OpenFOAM
# ==========================
x_of = of["arc_length"]
mach_of = of["Ma"]

p_of = of["p_average"]
pt_of = of["P0"]

pp0_of = p_of / pt_of
tt0_of = of["T_average"] / of["T0"]
rr0_of = of["rho"] / of["rho0"]
vel_of = of["U_average:0"]

# ==========================
# SU2
# ==========================
x_su2 = su2["arc_length"]

mach_su2 = su2["Mach"]
p_su2 = su2["Pressure"]

# Total pressure from static pressure and Mach
pt_su2 = p_su2 * (1 + 0.2*mach_su2**2)**3.5

pp0_su2 = p_su2 / pt_su2
tt0_su2 = su2["Temperature"] / T0
rr0_su2 = su2["Density"] / rho0
vel_su2 = su2["Velocity_Magnitude"]

# ==========================
# Plot function
# ==========================
def plot_compare(x1,y1,x2,y2,ylabel,title,filename):

    plt.figure(figsize=(8,5))

    plt.plot(x1,y1,
             lw=2,
             label='OpenFOAM')

    plt.plot(x2,y2,
             '--',
             lw=2,
             label='SU2')

    plt.xlabel("Axial Distance (m)")
    plt.ylabel(ylabel)
    plt.title(title)

    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.savefig(filename,dpi=300)
    plt.close()

# ==========================
# Generate plots
# ==========================

plot_compare(
    x_of,mach_of,
    x_su2,mach_su2,
    "Mach Number",
    "Mach Number Comparison",
    "Mach_Comparison.png"
)

plot_compare(
    x_of,pp0_of,
    x_su2,pp0_su2,
    "P/P₀",
    "Pressure Ratio Comparison",
    "PressureRatio_Comparison.png"
)

plot_compare(
    x_of,tt0_of,
    x_su2,tt0_su2,
    "T/T₀",
    "Temperature Ratio Comparison",
    "TemperatureRatio_Comparison.png"
)

plot_compare(
    x_of,rr0_of,
    x_su2,rr0_su2,
    "ρ/ρ₀",
    "Density Ratio Comparison",
    "DensityRatio_Comparison.png"
)

plot_compare(
    x_of,vel_of,
    x_su2,vel_su2,
    "Velocity (m/s)",
    "Velocity Comparison",
    "Velocity_Comparison.png"
)

# ==========================
# Total Pressure Comparison
# ==========================

plot_compare(
    x_of,pt_of,
    x_su2,pt_su2,
    "Total Pressure (Pa)",
    "Total Pressure Comparison",
    "TotalPressure_Comparison.png"
)

print("All plots generated successfully.")