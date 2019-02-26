# from mat4py import loadmat
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt


"""
@author Farzaneh.Tlb
Implementation of RasterPlot
"""

Nu = loadmat('../datas/Nu.mat')
# condLFP = loadmat('../datas/condLFP.mat')
# LFP1 = loadmat('../datas/LFP1.mat')
conNU = loadmat('../datas/conNU.mat')

Nu_data = Nu['nu'] #(25,928,3500)
conNU_data = conNU['condNU'] #(928, 1)
# condLFP_data = condLFP['Cond'] #(963,1)
# LFP_data = LFP1['LFP'] #(963, 8000)

# Nu_data = np.array(Nu_data) #(25,928,3500)
# conNU_data  = np.array(conNU_data ) #(25,928,3500)
# print(conNU_data)



neurons = Nu_data[0]
trial_number = 3500

neurons_array = np.empty(shape = [25,928,3500])

for index, neuron in np.ndenumerate(neurons):
    neurons_array[index] = neuron
    # print(index ,np.count_nonzero(neuron[in]))


print("nnA" , neurons_array.shape)

nueron_numbers = [1,3,5]

# fig, axs = plt.subplots(4, 1)
# axs[0, 0].eventplot(neurons_array[0])
# print("X" ,np.nonzero(x))
colors1 = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1],
                    [1, 1, 0],
                    [1, 0, 1],
                    [0, 1, 1]])


selected_trials =neurons_array[0,0:6]

it = np.nditer(selected_trials ,flags =['multi_index'] , op_flags =['writeonly'])
with it:
    while not it.finished:
        it[0] = it[0] * (it.multi_index[0] +1)
        it.iternext()
print(selected_trials)

def numpy_fillna(data):
    # Get lengths of each row of data
    lens = np.array([len(i) for i in data])

    # Mask of valid places in each row
    mask = np.arange(lens.max()) < lens[:,None]

    # Setup output array and put elements from data into masked positions
    out = np.zeros(mask.shape)
    out[mask] = np.concatenate(data)
    return out






#
# ready_to_plot = np.empty([6,3500])
# # plt.plot(x)
# for i  ,spike_train in  np.ndenumerate(selected_trials) :
#     print(i[0])
#     print(spike_train)
#     spike_train = spike_train * (i[0]+1)
#     ready_to_plot[i] = spike_train
ready_to_plot_indices = []
print(selected_trials.shape)

k= 1
j=i=0
ready_to_plot_indices = []
max = 0
for trial in selected_trials:
    # print("x" , np.nonzero(trial)[0])
    ready_to_plot_indices.append(np.nonzero(trial)[0])

numpy_fillna(ready_to_plot_indices)


# print(ready_to_plot_indices.size)
plt.eventplot(ready_to_plot_indices , orientation='horizontal' , linelengths=0.2)


lineoffsets1 = np.arange(0,3500,1)


plt.show()

