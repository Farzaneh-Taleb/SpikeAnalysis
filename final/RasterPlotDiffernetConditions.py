import utility_functions as utility
import matplotlib.pyplot as plt
import numpy as np

"""
@author Farzaneh.Tlb
2/27/19 12:49 AM
Implementation of RasterPlot(Fill this line)
"""

ut = utility.Utility_Functions()
trials = 20

array_color = ['green', 'red', 'blue', 'yellow', 'black', 'orange', 'gray', 'red']
for n in range(ut.number_of_neurons):
    fig, axs = plt.subplots(1, 2, sharex='col', sharey='row',figsize=(20, 10))
    for c in range(ut.conditions ):
        trials = ut.get_trial_by_condition(n, c + 1)
        selected_trials = trials[0:20, :]
        trial_index = 1
        axs[c//8].set_xlabel("radius" + str(c//8))
        for trial in selected_trials:
            spikes = np.nonzero(trial)
            axs[c//8].scatter(spikes, np.ones(spikes[0].size) * 10 * ((c%8) + 1) + trial_index / 2, marker='.',  edgecolors=array_color[c%8], s=1  )
            x = 10 * ((c%8) + 1) + trial_index
            trial_index += 1
            # axs[c//8].ax
    for c in range(2):
        for ya in range(1,9):
            axs[c].axhline(10*ya)

    fig.suptitle("neuron" + str(n))
    y_axis = np.arange(10, 90, 10)

    plt.yticks(y_axis, ['angle 1', 'angle 2', 'angle 3', 'angle 4',
                        'angle 5', 'angle 6', 'angle 7', 'angle 8'])

    plt.show()
