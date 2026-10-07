import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import os

folder=r"C:\Users\VEDANT\Desktop\ramjet\3d-no-slip"
csv_file=os.path.join(folder,"topwall_values.csv")
results=os.path.join(folder,"results_topwall")
os.makedirs(results,exist_ok=True)

P0=200000.0
T0=354.0
gamma=1.4
R=287.0
rho0=P0/(R*T0)
Pout=111800.0

df=pd.read_csv(csv_file).sort_values("arc_length")
x=df["Points_0"].to_numpy()

df["P_ratio"]=df["Pressure"]/P0
df["T_ratio"]=df["Temperature"]/T0
df["rho_ratio"]=df["Density"]/rho0

def h(xx):
    return np.where(xx<=1.0,0.36*xx**3-0.54*xx**2+0.36,0.18)

def area_ratio(M):
    return (1/M)*((2/(gamma+1)*(1+0.2*M*M))**((gamma+1)/(2*(gamma-1))))

def peq(M):
    return (1+0.2*M*M)**(-gamma/(gamma-1))-(Pout/P0)

M_end=float(fsolve(peq,0.95)[0])
Astar=0.18/area_ratio(M_end)
Ar=h(x)/Astar

def eq(M,A):
    return area_ratio(M)-A

M=np.zeros_like(x)
g=0.3
for i,A in enumerate(Ar):
    M[i]=fsolve(eq,g,args=(A,))[0]
    g=min(max(M[i],0.02),0.98)

P_ratio=(1+0.2*M**2)**(-gamma/(gamma-1))
T_ratio=(1+0.2*M**2)**(-1)
rho_ratio=(1+0.2*M**2)**(-1/(gamma-1))
V=M*np.sqrt(gamma*R*T_ratio*T0)

plots=[
("P_ratio",P_ratio,"P/P0","Pressure Ratio"),
("T_ratio",T_ratio,"T/T0","Temperature Ratio"),
("rho_ratio",rho_ratio,"ρ/ρ0","Density Ratio"),
("Velocity_Magnitude",V,"Velocity (m/s)","Velocity")
]

for cfd,theory,ylabel,title in plots:
    plt.figure(figsize=(9,6))
    plt.plot(df["arc_length"],df[cfd],lw=3,label="3D CFD")
    plt.plot(df["arc_length"],theory,lw=3,label="Theory")
    plt.xlabel("Arc Length (m)",fontsize=16)
    plt.ylabel(ylabel,fontsize=16)
    plt.title(title+" - Top Wall",fontsize=16)
    plt.grid(True,which="major",lw=1.5)
    plt.minorticks_on()
    plt.grid(True,which="minor",ls="--",lw=0.8)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(results,title.replace(" ","_")+".png"),dpi=600)

plt.show()
print("Saved plots to:",results)
