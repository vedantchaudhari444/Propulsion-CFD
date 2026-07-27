import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.interpolate import PchipInterpolator

# ==========================================================
# FILE PATHS
# ==========================================================

su2_file = r"C:\Users\VEDANT\Desktop\bottomwall.csv"
ansys_file = r"C:\Users\VEDANT\Desktop\ansys.xlsx"
exp_file = r"C:\Users\VEDANT\Desktop\experimental.xlsx"

# ==========================================================
# CONSTANTS
# ==========================================================

P0 = 135775.0
Patm = 101325.0

x_throat = 0.228
H = 0.048

# ==========================================================
# SU2
# ==========================================================

su2 = pd.read_csv(su2_file)

if "Points:0" in su2.columns:
    xcol = "Points:0"
elif "Points_0" in su2.columns:
    xcol = "Points_0"
else:
    raise ValueError("No x-coordinate column found.")

su2_mean = (
    su2
    .groupby(xcol, as_index=False)["Pressure"]
    .mean()
)

su2_mean["xH"] = (su2_mean[xcol]-x_throat)/H
su2_mean["Pr"] = su2_mean["Pressure"]/P0

su2_mean = su2_mean[su2_mean["xH"]>=-0.5]

# ==========================================================
# ANSYS
# ==========================================================

ansys = pd.read_excel(ansys_file, header=None)

x_ansys = pd.to_numeric(ansys.iloc[:,0], errors="coerce")
Pg = pd.to_numeric(ansys.iloc[:,1], errors="coerce")

Pabs = Pg + Patm

ansys_plot = pd.DataFrame()

ansys_plot["xH"] = (x_ansys-x_throat)/H
ansys_plot["Pr"] = Pabs/P0

ansys_plot = ansys_plot.dropna()
ansys_plot = ansys_plot[ansys_plot["xH"]>=-0.5]

# ==========================================================
# EXPERIMENT
# ==========================================================

exp = pd.read_excel(exp_file)

exp_x = exp.iloc[:,0]
exp_p = exp.iloc[:,1]

# ==========================================================
# SAVE NORMALIZED DATA
# ==========================================================

su2_mean.to_excel(
    r"C:\Users\VEDANT\Desktop\SU2_Normalized.xlsx",
    index=False
)

ansys_plot.to_excel(
    r"C:\Users\VEDANT\Desktop\ANSYS_Normalized.xlsx",
    index=False
)

# ==========================================================
# LIMIT CFD DATA TO EXPERIMENT RANGE
# ==========================================================

x_end = exp_x.max()

su2_mean = su2_mean[su2_mean["xH"] <= x_end]
ansys_plot = ansys_plot[ansys_plot["xH"] <= x_end]

# ==========================================================
# SMOOTH CURVES (PCHIP)
# ==========================================================

su2_mean = (
    su2_mean
    .groupby("xH", as_index=False)["Pr"]
    .mean()
    .sort_values("xH")
)

ansys_plot = (
    ansys_plot
    .groupby("xH", as_index=False)["Pr"]
    .mean()
    .sort_values("xH")
)

x_su2 = su2_mean["xH"].to_numpy()
y_su2 = su2_mean["Pr"].to_numpy()

x_ans = ansys_plot["xH"].to_numpy()
y_ans = ansys_plot["Pr"].to_numpy()

xs_su2 = np.linspace(x_su2.min(), x_su2.max(), 1200)
xs_ans = np.linspace(x_ans.min(), x_ans.max(), 1200)

ys_su2 = PchipInterpolator(x_su2, y_su2)(xs_su2)
ys_ans = PchipInterpolator(x_ans, y_ans)(xs_ans)

# ==========================================================
# PLOT
# ==========================================================

plt.figure(figsize=(13,7))

plt.plot(
    xs_su2,
    ys_su2,
    color="blue",
    linewidth=3.2,
    label="SU2 (Time Mean)"
)

plt.plot(
    xs_ans,
    ys_ans,
    color="red",
    linewidth=3.2,
    label="ANSYS (Time Mean)"
)

plt.scatter(
    exp_x,
    exp_p,
    s=95,
    color="black",
    edgecolors="white",
    linewidth=1.2,
    zorder=20,
    label="Chen Experiment"
)

# ==========================================================
# LABELS
# ==========================================================

plt.xlabel(r"$x/H$", fontsize=22)
plt.ylabel(r"$P/P_0$", fontsize=22)
plt.title("Bottom Wall Mean Pressure Distribution", fontsize=24)

# ==========================================================
# LIMITS
# ==========================================================

xmin = min(xs_su2.min(), xs_ans.min(), exp_x.min())
xmax = max(xs_su2.max(), xs_ans.max(), exp_x.max())

ymin = min(ys_su2.min(), ys_ans.min(), exp_p.min())
ymax = max(ys_su2.max(), ys_ans.max(), exp_p.max())

plt.xlim(xmin-0.1, x_end+0.1)
plt.ylim(ymin-0.015, ymax+0.02)

# ==========================================================
# GRID
# ==========================================================

ax = plt.gca()

ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(0.25))

ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.yaxis.set_minor_locator(MultipleLocator(0.01))

plt.grid(
    which="major",
    color="gray",
    linewidth=1.2,
    alpha=0.70
)

plt.grid(
    which="minor",
    color="gray",
    linestyle="--",
    linewidth=0.6,
    alpha=0.50
)

# ==========================================================
# AXES
# ==========================================================

for spine in ax.spines.values():
    spine.set_linewidth(1.8)

ax.tick_params(
    axis="both",
    which="major",
    direction="in",
    length=8,
    width=1.5,
    labelsize=15
)

ax.tick_params(
    axis="both",
    which="minor",
    direction="in",
    length=4,
    width=1.0
)

# ==========================================================
# LEGEND
# ==========================================================

plt.legend(
    fontsize=16,
    frameon=True,
    facecolor="white",
    edgecolor="black"
)

plt.tight_layout()

plt.savefig(
    r"C:\Users\VEDANT\Desktop\Comparison_SU2_ANSYS_Experiment.png",
    dpi=600,
    bbox_inches="tight"
)

plt.show()