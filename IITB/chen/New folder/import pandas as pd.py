import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# FILE PATHS
# ==========================================================

su2_file = r"C:\Users\VEDANT\Desktop\point.csv"
ansys_file = r"C:\Users\VEDANT\Desktop\fft.csv"
exp_file = r"C:\Users\VEDANT\Desktop\experimental.csv"

# ==========================================================
# SU2 SETTINGS
# ==========================================================

time_step = 5e-5          # SU2 TIME_STEP
output_freq = 10          # OUTPUT_WRT_FREQ

dt = time_step * output_freq

# ==========================================================
# SU2 FFT
# ==========================================================

su2 = pd.read_csv(su2_file)

pressure = su2.iloc[:,0].to_numpy(dtype=float)

pressure = pressure - np.mean(pressure)

N = len(pressure)

fft = np.fft.rfft(pressure)

freq = np.fft.rfftfreq(N, dt)

amp = np.abs(fft)

# keep only 0-500 Hz

mask = freq <= 500

freq = freq[mask]
amp = amp[mask]

amp = amp / np.max(amp)

# ignore DC peak

peak_su2 = np.argmax(amp[1:]) + 1

# ==========================================================
# ANSYS FFT
# ==========================================================

ansys = pd.read_csv(ansys_file, header=None)

ansys_freq = ansys.iloc[:,0].astype(float).values
ansys_power = ansys.iloc[:,1].astype(float).values

mask = ansys_freq <= 500

ansys_freq = ansys_freq[mask]
ansys_power = ansys_power[mask]

ansys_power = ansys_power / np.max(ansys_power)

peak_ansys = np.argmax(ansys_power[1:]) + 1

# ==========================================================
# EXPERIMENT
# ==========================================================

exp = pd.read_csv(exp_file, header=None)

exp_freq = exp.iloc[:,0].astype(float).values
exp_amp = exp.iloc[:,1].astype(float).values

mask = exp_freq <= 500

exp_freq = exp_freq[mask]
exp_amp = exp_amp[mask]

exp_amp = exp_amp / np.max(exp_amp)

peak_exp = np.argmax(exp_amp)

# ==========================================================
# PRINT RESULTS
# ==========================================================

print("\n--------------------------------------------")
print("SU2")
print("--------------------------------------------")
print("Samples               :",N)
print("Sampling Frequency    :",1/dt,"Hz")
print("Dominant Frequency    :",freq[peak_su2],"Hz")

print("\n--------------------------------------------")
print("ANSYS")
print("--------------------------------------------")
print("Dominant Frequency    :",ansys_freq[peak_ansys],"Hz")

print("\n--------------------------------------------")
print("EXPERIMENT")
print("--------------------------------------------")
print("Dominant Frequency    :",exp_freq[peak_exp],"Hz")
print("--------------------------------------------")

# ==========================================================
# PLOT
# ==========================================================

plt.figure(figsize=(13,7))

# SU2

plt.plot(freq,
         amp,
         color='blue',
         linewidth=2.5,
         label='SU2')

# ANSYS

plt.plot(ansys_freq,
         ansys_power,
         color='red',
         linewidth=2.2,
         label='ANSYS')

# EXP

plt.plot(exp_freq,
         exp_amp,
         'k--',
         linewidth=2,
         label='Experiment')

# ----------------------------------------------------------
# Peaks
# ----------------------------------------------------------

plt.scatter(freq[peak_su2],
            amp[peak_su2],
            color='blue',
            s=80,
            zorder=5)

plt.scatter(ansys_freq[peak_ansys],
            ansys_power[peak_ansys],
            color='red',
            s=80,
            zorder=5)

plt.scatter(exp_freq[peak_exp],
            exp_amp[peak_exp],
            color='black',
            s=80,
            zorder=5)

# ----------------------------------------------------------
# Labels
# ----------------------------------------------------------

plt.annotate(f"SU2\n{freq[peak_su2]:.1f} Hz",
             (freq[peak_su2],amp[peak_su2]),
             xytext=(25,20),
             textcoords='offset points',
             fontsize=11,
             color='blue',
             arrowprops=dict(arrowstyle='->',color='blue'))

plt.annotate(f"ANSYS\n{ansys_freq[peak_ansys]:.1f} Hz",
             (ansys_freq[peak_ansys],ansys_power[peak_ansys]),
             xytext=(-70,40),
             textcoords='offset points',
             fontsize=11,
             color='red',
             arrowprops=dict(arrowstyle='->',color='red'))

plt.annotate(f"EXP\n{exp_freq[peak_exp]:.1f} Hz",
             (exp_freq[peak_exp],exp_amp[peak_exp]),
             xytext=(25,-45),
             textcoords='offset points',
             fontsize=11,
             color='black',
             arrowprops=dict(arrowstyle='->',color='black'))

# ==========================================================
# Figure
# ==========================================================

plt.xlim(0,500)
plt.ylim(0,1.08)

plt.xlabel("Frequency (Hz)",fontsize=18)
plt.ylabel("Normalized Amplitude",fontsize=18)

plt.title("FFT Comparison : SU2 vs ANSYS vs Chen Experiment",
          fontsize=20)

plt.xticks(np.arange(0,501,25),fontsize=12)
plt.yticks(np.arange(0,1.05,0.1),fontsize=12)

plt.grid(which='major',
         linestyle='--',
         linewidth=0.7,
         alpha=0.6)

plt.grid(which='minor',
         linestyle=':',
         linewidth=0.5,
         alpha=0.4)

plt.minorticks_on()

plt.legend(fontsize=14,
           loc='upper right')

plt.tight_layout()

plt.show()