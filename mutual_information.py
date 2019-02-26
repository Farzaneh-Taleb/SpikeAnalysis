import utility_functions as utility
import numpy as np
import matplotlib.pyplot as plt
"""
@author Farzaneh.Tlb
2/26/19 11:18 AM
Implementation of Mutual Information 
"""
ut = utility.Utility_Functions()

ent_r_s = np.zeros(shape=[8,])
p_s = np.zeros(shape=[8,])
# selected_neuron = 0


def calculate_MI(start_time , end_time):
    MI = np.zeros(shape=[25, 8])
    for n in range(ut.number_of_neurons):
        for c in range(ut.conditions-8):
            trials = ut.get_trial_by_condition(n, c+1)
            number_of_trials = trials.shape[0]
            data_to_histogram = ut.get_indecis_of_spikes(trials[:,start_time:end_time])
            hist = np.histogram(data_to_histogram, bins='fd', density=True)
            ent_r_s[c] = -(hist[0]*np.log(np.abs(hist[0]))).sum()
            p_s[c] = number_of_trials /  ut.number_of_all_trials

        x2 = np.multiply(ent_r_s, p_s)
        trials_by_neuron = ut.get_neuron(n)
        data_to_histogram = ut.get_indecis_of_spikes(trials_by_neuron[:, start_time:end_time])
        hist = np.histogram(data_to_histogram, bins='fd', density=True)
        ent_r = -(hist[0] * np.log(np.abs(hist[0]))).sum()
        MI[n] = ent_r - x2
        print(MI[n])
    return MI
MI1  =calculate_MI(1000,1501)
MI2 = calculate_MI(2700,3201)

plt.hist(MI1.flatten(), bins='fd')
plt.hist(MI2.flatten() , bins = 'fd')
plt.show()


# p_r =
# p_r_s =
# p_s_r =



