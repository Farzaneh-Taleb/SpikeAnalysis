# from mat4py import loadmat
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import utility_functions as utility


"""
@author Farzaneh.Tlb
Implementation of RasterPlot
"""
ut = utility.Utility_Functions()

neurons_array =  ut.get_nurons_array()


nueron_numbers = [1,3,5]

# selected_trials =neurons_array[0,0:10]
selected_trials = ut.get_trial_by_condition(3,1)
selected_trials = selected_trials[0:20 , : ]

it = np.nditer(selected_trials ,flags =['multi_index'] , op_flags =['writeonly'])
for x in it :
    it[0] = it[0] * (it.multi_index[0] + 1)
    it.iternext()


def numpy_fillna(data):
    lens = np.array([len(i) for i in data])
    mask = np.arange(lens.max()) < lens[:,None]
    out = np.zeros(mask.shape)
    out[mask] = np.concatenate(data)
    return out





ready_to_plot_indices = []

k= 1
j=i=0
max = 0
for trial in selected_trials:
    ready_to_plot_indices.append(np.nonzero(trial)[0])

numpy_fillna(ready_to_plot_indices)


plt.eventplot(ready_to_plot_indices , orientation='horizontal' , linelengths=0.2)
lineoffsets1 = np.arange(0,3500,1)

plt.show()

