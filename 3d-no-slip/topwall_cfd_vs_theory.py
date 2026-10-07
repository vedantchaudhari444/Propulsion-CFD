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
df["P_ratio"]=df["Pressure"]/P0
df["T_ratio"]=df["Temperature"]/T0
df["rho_ratio"]=df["Density"]/rho0

# theoretical geometry
x=np.linspace(0,2,600)
h=np.where(x<=1,0.36*x**3-0.54*x**2+0.36,0.18)
A=h

pr=Pout/P0
def pm(M):
    return (1+0.2*M*M)**(-gamma/(gamma-1))-pr
M_exit=float(fsolve(pm,0.95)[0])

def area_ratio(M):
    return (1/M)*((2/(gamma+1)*(1+0.2*M*M))**((gamma+1)/(2*(gamma-1))))
Astar=0.18/area_ratio(M_exit)
AR=A/Astar
def eq(M,a):
    return area_ratio(M)-a
Mach=np.zeros_like(x)
g=0.2
for i,a in enumerate(AR):
    Mach[i]=fsolve(eq,g,args=(a,))[0]
    g=min(max(Mach[i],0.02),0.99)
P_ratio=(1+0.2*Mach**2)**(-gamma/(gamma-1))
T_ratio=(1+0.2*Mach**2)**(-1)
rho_ratio=(1+0.2*Mach**2)**(-1/(gamma-1))

Temp=T_ratio*T0
Velocity=Mach*np.sqrt(gamma*R*Temp)

def style():
    plt.grid(True,which='major',lw=1.6)
    plt.minorticks_on()
    plt.grid(True,which='minor',ls='--',lw=0.8)
    ax=plt.gca()
    for s in ax.spines.values():
        s.set_linewidth(2)
    ax.tick_params(width=2,length=7,labelsize=13)
    plt.legend(frameon=False)
    plt.tight_layout()

plots=[
("Pressure_Ratio.png","P_ratio",P_ratio,"P/P0"),
("Temperature_Ratio.png","T_ratio",T_ratio,"T/T0"),
("Density_Ratio.png","rho_ratio",rho_ratio,"ρ/ρ0"),
("Velocity.png","Velocity_Magnitude",Velocity,"Velocity (m/s)")
]

for fname,cfdcol,theory,ylabel in plots:
    plt.figure(figsize=(9,6))
    plt.plot(df["arc_length"],df[cfdcol],lw=3,label="Top Wall CFD (No Slip)")
    plt.plot(x,theory,'k--',lw=3,label="Isentropic Theory")
    plt.xlabel("Length (m)",fontsize=17)
    plt.ylabel(ylabel,fontsize=17)
    style()
    plt.savefig(os.path.join(results,fname),dpi=600)

plt.show()
print("Saved plots to:",results)
