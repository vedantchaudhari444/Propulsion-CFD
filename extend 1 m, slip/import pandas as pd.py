import pandas as pd
import numpy as np
from scipy.spatial import cKDTree

# =========================================================
# FILES
# =========================================================

top_wall_file = r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\topwall_surface.csv"

bot_wall_file = r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\botwall_surface.csv"

flow_file = r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\flow.csv"

# =========================================================
# LOAD FILES
# =========================================================

top_wall = pd.read_csv(top_wall_file)
bot_wall = pd.read_csv(bot_wall_file)
flow = pd.read_csv(flow_file)

# =========================================================
# COLUMN NAMES
# CHANGE IF NEEDED
# =========================================================

wall_x = 'x'
wall_y = 'y'

flow_x = 'Points_0'
flow_y = 'Points_1'

# =========================================================
# CREATE KD TREE FROM FLOW FIELD
# =========================================================

flow_points = np.column_stack((
    flow[flow_x],
    flow[flow_y]
))

tree = cKDTree(flow_points)

# =========================================================
# FUNCTION TO EXTRACT NEAREST VALUES
# =========================================================

def extract_wall_data(wall_df):

    wall_points = np.column_stack((
        wall_df[wall_x],
        wall_df[wall_y]
    ))

    # nearest point search
    dist, idx = tree.query(wall_points)

    # get matching flow values
    matched = flow.iloc[idx].reset_index(drop=True)

    # combine
    result = pd.concat([
        wall_df.reset_index(drop=True),
        matched
    ], axis=1)

    return result

# =========================================================
# EXTRACT
# =========================================================

top_data = extract_wall_data(top_wall)
bot_data = extract_wall_data(bot_wall)

# =========================================================
# SAVE
# =========================================================

top_output = r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\topwall_values.csv"

bot_output = r"C:\Users\VEDANT\Desktop\ramjet\extend 1 m, slip\botwall_values.csv"

top_data.to_csv(top_output, index=False)
bot_data.to_csv(bot_output, index=False)

# =========================================================
# DONE
# =========================================================

print("DONE")
print("Created:")
print(top_output)
print(bot_output)