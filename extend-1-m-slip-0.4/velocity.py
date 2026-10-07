import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# USER INPUTS
# =====================================================

file_path = r"C:\Users\VEDANT\Desktop\ramjet\extend-1-m-slip-0.4\flow.csv"

x_profile = 1.0

variable = 'Velocity_Magnitude'

# Examples:
#
# 'Velocity_Magnitude'
# 'Mach'
# 'Pressure'
# 'Temperature'
# 'Density'

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv(file_path)

# =====================================================
# FIND CLOSEST X LOCATION IN MESH
# =====================================================

x_all = df['Points_0'].values

x_actual = x_all[
    np.argmin(
        np.abs(x_all - x_profile)
    )
]

print(f'\nRequested x = {x_profile:.6f}')
print(f'Actual mesh x = {x_actual:.6f}')

# =====================================================
# AUTOMATIC TOLERANCE
# =====================================================

unique_x = np.sort(
    df['Points_0'].unique()
)

dx = np.min(np.diff(unique_x))

tol = dx * 0.5

# =====================================================
# EXTRACT VERTICAL PROFILE
# =====================================================

profile = df[
    np.abs(
        df['Points_0'] - x_actual
    ) < tol
].copy()

# =====================================================
# SORT FROM BOTTOM WALL TO TOP WALL
# =====================================================

profile = profile.sort_values(
    by='Points_1'
)

# =====================================================
# SAVE PROFILE
# =====================================================

csv_name = (
    f"profile_x_{x_profile:.3f}.csv"
)

profile.to_csv(
    csv_name,
    index=False
)

# =====================================================
# PLOT
# =====================================================

plt.figure(figsize=(8,6))

plt.plot(
    profile[variable],
    profile['Points_1'],
    linewidth=3
)

plt.xlabel(
    variable,
    fontsize=16
)

plt.ylabel(
    'y (m)',
    fontsize=16
)

plt.title(
    f'{variable} Profile at x = {x_actual:.4f} m',
    fontsize=16
)

plt.grid(
    True,
    which='major',
    linewidth=1.5
)

plt.minorticks_on()

plt.grid(
    True,
    which='minor',
    linestyle='--'
)

plt.tight_layout()

png_name = (
    f"{variable}_profile_x_{x_profile:.3f}.png"
)

plt.savefig(
    png_name,
    dpi=600
)

plt.show()

# =====================================================
# INFORMATION
# =====================================================

print('\n==============================')
print('Profile extracted successfully')
print('Points found:', len(profile))
print('Bottom wall y =', profile['Points_1'].min())
print('Top wall y =', profile['Points_1'].max())
print('Saved CSV :', csv_name)
print('Saved PNG :', png_name)
print('==============================')