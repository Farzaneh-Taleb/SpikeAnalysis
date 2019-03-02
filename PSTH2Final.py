import numpy
import utility_functions as utility
import matplotlib.pyplot as plt
import seaborn as sns

"""
@author Farzaneh.Tlb
2/26/19 12:10 AM
Implementation of another betttter PSTH [hip hip hoOoOoOoOray] 
"""
ut = utility.Utility_Functions()

for n in range(ut.number_of_neurons):
    fig, axs = plt.subplots(1, 2, sharex='col', sharey='row')

    for c in range(ut.conditions):
        print((c + 1) % 4)
        trials = ut.get_trial_by_condition(n, c + 1)
        trial_numbers, times = ut.get_indecis_of_spikes(trials)

        sns.distplot(times, bins='fd', norm_hist=True, hist=False, ax=axs[c // 8], label="condition" + str(c + 1))

    plt.xlabel("neuron" + str(n))
    plt.show()


