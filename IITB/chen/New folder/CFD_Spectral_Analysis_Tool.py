import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import welch, find_peaks

su2_file=r"C:\Users\VEDANT\Desktop\point.csv"
ansys_file=r"C:\Users\VEDANT\Desktop\pre.csv"
exp_file=r"C:\Users\VEDANT\Desktop\experimental.csv"

REMOVE_FIRST=0.30
FMAX=500

su2=pd.read_csv(su2_file)
p_su2=su2.iloc[:,0].astype(float).values
su2_index=np.arange(len(p_su2))
t_su2=su2_index * 5e-4
k=int(len(p_su2)*REMOVE_FIRST)
p_su2=p_su2[k:]-np.mean(p_su2[k:])
t_su2=t_su2[k:]
fs_su2=1/np.mean(np.diff(t_su2))

ans=pd.read_csv(ansys_file)
t_ans=ans.iloc[:,0].astype(float).values
p_ans=ans.iloc[:,1].astype(float).values
k=int(len(p_ans)*REMOVE_FIRST)
p_ans=p_ans[k:]-np.mean(p_ans[k:])
t_ans=t_ans[k:]
fs_ans=1/np.mean(np.diff(t_ans))

exp=pd.read_csv(exp_file)
f_exp=exp.iloc[:,0].astype(float).values
a_exp=exp.iloc[:,1].astype(float).values
a_exp=a_exp/np.max(a_exp)

def get_psd(sig,fs):
    n=min(256,len(sig))
    f,P=welch(sig,fs=fs,window="hann",nperseg=n,noverlap=n//2,scaling="density")
    m=f<=FMAX
    f,P=f[m],P[m]
    P=P/np.max(P)
    return f,P

f1,p1=get_psd(p_su2,fs_su2)
f2,p2=get_psd(p_ans,fs_ans)

def dominant(f,p):
    pk,_=find_peaks(p,height=0.1)
    if len(pk)==0:
        return np.argmax(p[1:])+1
    return pk[np.argmax(p[pk])]

i1=dominant(f1,p1)
i2=dominant(f2,p2)
i3=np.argmax(a_exp)

def label_peak(ax, x, y, value, dx, dy, ha='left', va='bottom'):
    ax.annotate(
        f"{value:.1f} Hz",
        (x, y),
        xytext=(dx, dy),
        textcoords="offset points",
        ha=ha,
        va=va,
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="0.6", alpha=0.85),
        clip_on=True,
    )

plt.figure(figsize=(12,6))
ax=plt.gca()
plt.plot(f1,p1,label="SU2",lw=2)
plt.plot(f2,p2,label="ANSYS",lw=2)
plt.plot(f_exp,a_exp,'k--',label="Experimental",lw=2)

plt.scatter(f1[i1],p1[i1])
plt.scatter(f2[i2],p2[i2])
plt.scatter(f_exp[i3],a_exp[i3])

label_peak(ax, f1[i1], p1[i1], f1[i1], 8, 10, 'left', 'bottom')
label_peak(ax, f2[i2], p2[i2], f2[i2], -8, 10, 'right', 'bottom')
label_peak(ax, f_exp[i3], a_exp[i3], f_exp[i3], 8, -10, 'left', 'top')

plt.xlim(0,500)
plt.ylim(0,1.05)
plt.grid(True,ls='--')
plt.xlabel("Frequency (Hz)")
plt.ylabel("Normalized PSD")
plt.legend()
plt.tight_layout()
plt.savefig("FFT_Comparison.png",dpi=300)

pd.DataFrame({
"Case":["SU2","ANSYS","Experimental"],
"Peak Frequency (Hz)":[f1[i1],f2[i2],f_exp[i3]]
}).to_csv("Peak_Summary.csv",index=False)

print("SU2 Peak:",f1[i1])
print("ANSYS Peak:",f2[i2])
print("Experimental Peak:",f_exp[i3])
