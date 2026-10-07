import pandas as pd
import numpy as np

input_csv = r"C:\Users\VEDANT\Desktop\ramjet\3d-no-slip\surface.csv"
output_csv = r"C:\Users\VEDANT\Desktop\ramjet\3d-no-slip\topwall_values.csv"

mid_z = 0.18
tol_z = 1e-4
tol_y = 1e-4

df = pd.read_csv(input_csv)
df = df[np.abs(df["Points_2"]-mid_z)<tol_z].copy()

def y_top(x):
    return 0.36*x**3-0.54*x**2+0.36 if x<=1.0 else 0.18

df["y_wall"]=df["Points_0"].map(y_top)

top=df[np.abs(df["Points_1"]-df["y_wall"])<tol_y].copy()
for t in [5e-4,1e-3]:
    if len(top)>=20: break
    top=df[np.abs(df["Points_1"]-df["y_wall"])<t].copy()

top=top.sort_values("Points_0")
dx=np.diff(top["Points_0"])
dy=np.diff(top["Points_1"])
arc=np.concatenate(([0.0],np.cumsum(np.sqrt(dx**2+dy**2))))
top.insert(0,"arc_length",arc)
top=top.drop(columns=["y_wall"])
top.to_csv(output_csv,index=False)
print(f"Extracted {len(top)} points")
print(output_csv)
