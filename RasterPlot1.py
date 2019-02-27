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


array_color = ['green' , 'red' , 'blue' , 'yellow','black' , 'orange' , 'gray' , 'red']
for n in range(ut.number_of_neurons):
    for  c in range(ut.conditions-8):
        trials = ut.get_trial_by_condition(n,c+1)
        selected_trials = trials[0:20,:]
        # for index, trial in np.ndenumerate(selected_trials):
        trial_index = 1
        for trial in selected_trials:
            spikes = np.nonzero(trial)
            print(spikes[0].size)
            plt.scatter(spikes,np.ones(spikes[0].size)*10*(c+1) + trial_index/2 , marker='.',edgecolors=array_color[c]  , s=1 )
            x = 10*(c+1) + trial_index
            trial_index +=1
            print("x" ,x)

    plt.axhline(y=10 )
    plt.axhline(y=20)
    plt.axhline(y=30)
    plt.axhline(y=40)
    plt.axhline(y=50)
    plt.axhline(y=60)
    plt.axhline(y=70)
    plt.axhline(y=80)
    plt.legend()
    y_axis = np.arange(10, 90, 10)

    plt.yticks(y_axis, ['condition 1' ,'condition 2','condition 3','condition 4','condition 5','condition 6','condition 7','condition 8'])

    plt.show()