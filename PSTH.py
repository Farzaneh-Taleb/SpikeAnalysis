"""
@author Farzaneh.Tlb
1/30/2019 1:07 AM
Implementation of PSTH
"""
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

Nu = loadmat('../datas/Nu.mat')
conNU = loadmat('../datas/conNU.mat')

Nu_data = Nu['nu']  # (25,928,3500)
conNU_data = conNU['condNU']  # (928, 1)

neurons = Nu_data[0]
neurons_array = np.empty(shape=[25, 928, 3500])
trial_number = 3500

for index, neuron in np.ndenumerate(neurons):
    neurons_array[index] = neuron


def getTrialByCondition(neuron_number, condition):
    s = neurons_array[neuron_number, (conNU_data == condition).squeeze(), :]
    data = np.sum(s, axis=0)
    print(s.shape)
    print(data)

    # return dict(zip(unique, counts))
    return data, s.shape[0]


summation, number_of_trials = getTrialByCondition(11, 1)
hist = summation / number_of_trials
plt.plot(hist, '-')
plt.show()
