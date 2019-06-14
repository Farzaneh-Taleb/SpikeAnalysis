"""
@author Farzaneh.Tlb
6/15/19 12:19 AM
Implementation of .... (Fill this line)
"""
import utility_functions as utility
from scipy import signal
import numpy as np
ut = utility.Utility_Functions()
import matplotlib.pyplot as plt
# print("s" , ut.condLFP_data.shape)
# print("s" , ut.LFP_data.shape)

for i in range(1,9):
    trials1 = ut.LFP_data[ut.condLFP_data[:,0]==i]
    trials2 = ut.LFP_data[ut.condLFP_data[:,0]==i+8]
    # print(trials1.shape)
    # trials2 = ut.LFP_data[:, (ut.condLFP_data == i+8).squeeze()]
    print(trials1.shape)
    print(trials2.shape)
    trials=list(trials1) + list(trials2)
    trials = np.array(trials)
    freqs, psd = signal.welch(trials[0,2700:3200])

    # plt.figure(figsize=(5, 4)  )
    plt.subplot(2,4,i)
    plt.semilogx(freqs, psd)
    plt.title('PSD: power spectral density for angel ' + str(i) + "\n in time [2700,3200]")
    plt.xlabel('Frequency')
    plt.ylabel('Power')
    plt.tight_layout()
plt.subplots_adjust(left=0.02, wspace=0.5, bottom=0.06, hspace=0.5)
plt.show()


np.random.seed(0)

time_step = .01
time_vec = np.arange(0, 70, time_step)

# A signal with a small frequency chirp
sig = np.sin(0.5 * np.pi * time_vec * (1 + .1 * time_vec))
print(sig)