# CFD vs Theory comparison script
# Update only the folder path if needed.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import os

folder = r"C:\Users\VEDANT\Desktop\ramjet\3d-no-slip"
csv_file = os.path.join(folder,"botwall.csv")
results = os.path.join(folder,"results")
os.makedirs(results, exist_ok=True)

P0 = 200000.0
T0 = 354.0
gamma = 1.4
R = 287.0
rho0 = P0/(R*T0)

df = pd.read_csv(csv_file).sort_values("arc_length")

df["P_ratio"] = df["Pressure"]/P0
df["T_ratio"] = df["Temperature"]/T0
df["rho_ratio"] = df["Density"]/rho0

# -------- Geometry ----------
x = np.linspace(0,2,600)
h = np.where(x<=1.0,
             0.36*x**3-0.54*x**2+0.36,
             0.18)

# -------- Find outlet/throat Mach from outlet pressure -----
Pout = 111800.0
pr = Pout/P0

def fM(M):
    return (1+0.2*M**2)**(-gamma/(gamma-1)) - pr

M_target = float(fsolve(fM,0.95)[0])

def area_ratio(M):
    return (1/M)*((2/(gamma+1)*(1+0.2*M**2))**((gamma+1)/(2*(gamma-1))))

Astar = 0.18/area_ratio(M_target)

Ar = h/Astar

def eq(M,A):
    return area_ratio(M)-A

Mach = np.zeros_like(x)
guess=0.3
for i,A in enumerate(Ar):
    Mach[i]=fsolve(eq,guess,args=(A,))[0]
    guess=min(max(Mach[i],0.01),0.99)

P_ratio=(1+0.2*Mach**2)**(-gamma/(gamma-1))
T_ratio=(1+0.2*Mach**2)**(-1)
rho_ratio=(1+0.2*Mach**2)**(-1/(gamma-1))
Temp=T_ratio*T0
Velocity=Mach*np.sqrt(gamma*R*Temp)

def style():
    plt.grid(True,which="major",lw=1.6)
    plt.minorticks_on()
    plt.grid(True,which="minor",ls="--",lw=0.8)
    ax=plt.gca()
    for s in ax.spines.values():
        s.set_linewidth(2)
    ax.tick_params(width=2,length=7,labelsize=13)
    plt.tight_layout()

plots=[
("Mach","Mach","Mach Number","Mach Comparison"),
("P_ratio","P_ratio","P/P0","Pressure Ratio Comparison"),
("T_ratio","T_ratio","T/T0","Temperature Ratio Comparison"),
("rho_ratio","rho_ratio","ρ/ρ0","Density Ratio Comparison"),
("Velocity_Magnitude","Velocity","Velocity (m/s)","Velocity Comparison")
]

for cfdcol,theocol,ylabel,title in plots:
    plt.figure(figsize=(9,6))
    plt.plot(df["arc_length"],df[cfdcol],lw=3,label="3D CFD")
    plt.plot(x,locals()[theocol],lw=3,label="Theory")
    plt.xlabel("Length (m)",fontsize=16)
    plt.ylabel(ylabel,fontsize=16)
    plt.title(title,fontsize=16)
    plt.legend()
    style()
    plt.savefig(os.path.join(results,title.replace(" ","_")+".png"),dpi=600)

plt.show()
print("Theoretical throat Mach =",M_target)
print("Results saved to:",results)
