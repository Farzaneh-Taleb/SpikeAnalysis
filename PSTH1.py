import utility_functions as utility
import numpy as np
import matplotlib.pyplot as plt
"""
@author Farzaneh.Tlb
2/24/19 7:52 PM
Implementation of Histogram in correct form(Fill this line)
"""

ut = utility.Utility_Functions()
neurons_array  = ut.get_nurons_array()
hist_neurons = np.zeros(shape=[25, 16, 3500])
hist_trials  = np.zeros(shape=[25,16])

for n in range(0,ut.number_of_neurons):
    for c in range(0,ut.conditions):
        summation , number_of_trials =ut.getTrialsSummationByCondition(n, c+ 1)
        hist_neurons[n,c ] = summation
        hist_trials[n,c ] = number_of_trials

# plt.xlim(0,3500)
# plt.plot(hist_neurons[2,0] , hist_neurons[2,1],hist_neurons[2,3])

# for c in range(0,ut.conditions):


a = np.add.reduceat(hist_neurons[4,1], np.arange(0, len(hist_neurons[4,1]  ), 50))
b = np.add.reduceat(hist_neurons[4,1], np.arange(0, len(hist_neurons[4,1]), 50))
print("a" , a.shape)
plt.plot(a)
plt.show()



