import pandas as pd
import matplotlib.pyplot as plt

# Load file
file_path = r"C:\Users\VEDANT\Desktop\Book2.xlsx"
df = pd.read_excel(file_path)

# Data
x_exp = df.iloc[:, 0]
y_exp = df.iloc[:, 1]

x_ansys = df.iloc[:, 2]
y_ansys = df.iloc[:, 3]

x_su2 = df.iloc[:, 4]
y_su2 = df.iloc[:, 5]

# Figure (same size)
plt.figure(figsize=(8,6))

# EXP → line + symbols
plt.plot(x_exp, y_exp, color='black', marker='s',
         linestyle='-', linewidth=2.2, markersize=6,
         label='Experimental')

# ANSYS → line
plt.plot(x_ansys, y_ansys, color='red',
         linewidth=3, label='ANSYS')

# SU2 → line
plt.plot(x_su2, y_su2, color='blue',
         linewidth=3, label='SU2')

# Labels (bigger for paper)
plt.xlabel('x / H_throat', fontsize=18)
plt.ylabel('P / P\u2080', fontsize=18)

# Tick labels
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

# Turn on minor ticks
plt.minorticks_on()

# 🔥 VERY PROMINENT GRID
plt.grid(True, which='major',
         linestyle='-',
         linewidth=1.2,
         alpha=0.9)

plt.grid(True, which='minor',
         linestyle='--',
         linewidth=0.8,
         alpha=0.8)

# Axis border (thick like journal plots)
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_linewidth(2)

# Tick thickness (important for print)
ax.tick_params(axis='both', which='major', width=1.5, length=6)
ax.tick_params(axis='both', which='minor', width=1.0, length=4)

# Legend
plt.legend(fontsize=13, frameon=False)

# Font
plt.rcParams['font.family'] = 'Times New Roman'

plt.tight_layout()

# Save high-quality (VERY IMPORTANT)
plt.savefig("CFD_vs_Exp_strong_grid.png", dpi=600)

plt.show()