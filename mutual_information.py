import utility_functions as utility
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

"""
@author Farzaneh.Tlb
2/26/19 11:18 AM
Implementation of Mutual Information 
"""
ut = utility.Utility_Functions()

ent_r_s = np.zeros(shape=[8, ])
p_s = np.zeros(shape=[8, ])




def calculate_MI(start_time, end_time):
    MI = np.zeros(shape=[25, ])
    for n in range(ut.number_of_neurons):
        for c in range(ut.conditions - 8):
            trials1 = ut.get_trial_by_condition(n, c + 1)
            trials2 = ut.get_trial_by_condition(n,c+9)
            all_trials = np.concatenate((trials1,trials2))
            print("tr" , all_trials.shape)
            number_of_trials_per_c = all_trials.shape[0]
            data_to_histogram = ut.get_indecis_of_spikes(all_trials[:, start_time:end_time])
            hist, bins = np.histogram(data_to_histogram, bins='fd', density=True)
            print(np.sum(hist[0]))
            ent_r_s[c] = -(hist[0] * np.log(np.abs(hist[0]))).sum()
            p_s[c] = number_of_trials_per_c / ut.number_of_all_trials

        x2 = np.multiply(ent_r_s, p_s)
        x2 = np.sum(x2)
        trials_by_neuron = ut.get_neuron(n)
        data_to_histogram = ut.get_indecis_of_spikes(trials_by_neuron[:, start_time:end_time])
        hist = np.histogram(data_to_histogram, bins='fd', density=True)
        ent_r = -(hist[0] * np.log(np.abs(hist[0]))).sum()
        MI[n] = ent_r - x2

    return MI




MI1 = calculate_MI(1000, 1501)
MI2 = calculate_MI(2700, 3201)

fig, axs = plt.subplots(1, 3,figsize=(20, 10))

axs[0].hist(MI1, bins='fd' ,alpha=0.5  )
axs[0].hist(MI2, bins='fd' , alpha=0.5 )
# plt.show()

axs[1].bar(np.arange(1, 26), MI1 , alpha=0.5 ,   )
axs[1].bar(np.arange(1, 26), MI2 , alpha=0.5 , )

# plt.show()

axs[2].scatter(MI1.flatten(), MI2.flatten())
# plt.scatter(MI2.flatten())
plt.show()

print(stats.ttest_ind(MI1, MI2))

# p_r =
# p_r_s =
# p_s_r =
