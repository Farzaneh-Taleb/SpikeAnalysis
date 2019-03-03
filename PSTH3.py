import numpy as np
import utility_functions as utility
import matplotlib.pyplot as plt
import seaborn as sns

"""
@author Farzaneh.Tlb
3/4/19 12:00 AM
Implementation of .... (Fill this line)
"""
ut = utility.Utility_Functions()
# hist_neurons = np.zeros(shape=[25, 16, 3500])
# hist_trials  = np.zeros(shape=[25,16])

# for n in range(ut.number_of_neurons):
#     fig, axs = plt.subplots(1, 2, sharex='col', sharey='row',figsize=(20, 10) , )
#
#     for c in range(ut.conditions):
#         trials = ut.get_trial_by_condition(n, c + 1)
#         trial_numbers, times = ut.get_indecis_of_spikes(trials)


for n in range(0,ut.number_of_neurons):
    for c in range(0,ut.conditions):
        print("n" , n , "c" , c)
        trials = ut.get_trial_by_condition(n, c + 1)

        spikes = np.nonzero(trials)
        times = spikes[1]

        print(times.shape)

        ni, bins, patches = plt.hist(x=times, bins='fd', color='#0504aa',
                                    alpha=0.7, rwidth=0.85)
    plt.show()