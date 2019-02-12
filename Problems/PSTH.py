
"""
@author Farzaneh.Tlb
1/30/2019 1:07 AM
Implementation of PSTH (Fill this line)
"""
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

Nu = loadmat('../datas/Nu.mat')
conNU = loadmat('../datas/conNU.mat')

Nu_data = Nu['nu'] #(25,928,3500)
conNU_data = conNU['condNU'] #(928, 1)

neurons = Nu_data[0]
neurons_array = np.empty(shape = [25,928,3500])
trial_number = 3500


for index, neuron in np.ndenumerate(neurons):
    neurons_array[index] = neuron

def getTrialByCondition(neuron_number , condition):
    # condition_indecis =np.where(conNU_data[:,0] == condition)
    # print("c" , np.asarray(condition_indecis).shape)
    # ind =  np.where(neurons_array[neuron_number , condition_indecis  , : ] ==1)
    # print ("ind" ,  np.asarray(ind))
    # print ("indShape" ,  np.asarray(ind).shape)
    # selected_neuron = neurons_array[np.where(neurons_array[neuron_number , np.asarray(condition_indecis)  , : ] ==1)]
    # unique, counts = np.unique(ind, return_counts=True)
    print("x" , conNU_data==condition)

    s = neurons_array[neuron_number,(conNU_data==condition).squeeze() , :]
    data = np.sum(s , axis=0 )
    print(s.shape)
    print(data)

    # return dict(zip(unique, counts))
    return data , s.shape[0]
summation , number_of_trials =getTrialByCondition(11, 1)
hist = summation / number_of_trials
plt.plot(hist,'-')
plt.show()