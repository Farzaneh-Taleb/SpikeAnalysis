import numpy
import utility_functions as utility
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

"""
@author Farzaneh.Tlb
2/26/19 12:10 AM
Implementation of another betttter PSTH [hip hip hoOoOoOoOray] 
"""
ut = utility.Utility_Functions()

for n in range(ut.number_of_neurons):
    fig, axs = plt.subplots(1, 2, sharex='col', sharey='row',figsize=(20, 10)  )
    # fig, axs = plt.subplots(1, 2  )

    for c in range(ut.conditions):
        trials = ut.get_trial_by_condition(n, c + 1)

        # ax2 = fig.add_subplot(1, 2, c//8+1)
        selected_trial = trials
        print(selected_trial.shape)
        # temp = [sum(selected_trial[i:i + 10]) for i in range(0, selected_trial.shape[1], 10)]
        # = [1, 0, 0, 0, 0, 2, 0, 0, 0, 0]
        s=20
        temp = np.add.reduceat(selected_trial, np.arange(0, selected_trial.shape[1], s) , axis=1)
        print("temp" , temp.shape)
        temp = np.sum(temp,axis=0) /s
        print(temp.shape)
        # plt.xlim(0, 3500)
        # plt.ylim(0, 30)
        # plt.tick_params(
        #     axis='x',  # changes apply to the x-axis
        #     which='both',  # both major and minor ticks are affected
        #     bottom=False,  # ticks along the bottom edge are off
        #     top=False,  # ticks along the top edge are off
        #     labelbottom=False)
        # plt.xticks(np.arange(0,3500,1000))
        time = np.arange(0,3500,s)
        print(time.shape)
        print(temp.shape)
        # ax2.plot(t, s1, t, s2)
        # ax2.set_xlabel('time')
        # ax2.set_ylabel('s1 and s2')
        # ax2.grid(True)
        plt.subplot(1,2,c//8+1)
        plt.plot(time  ,temp,label="condition" + str(c + 1))
        # plt.set_xlim(0, 3500)

        # plt.plot(time  ,temp,label="condition" + str(c + 1),marker='')
        plt.legend()
        # sns.kdeplot(temp,  ax=axs[c // 8], label="condition" + str(c + 1) , cut = 0)

    # plt.title("neuron" + str(n))
    fig.suptitle("neuron" + str(n), fontsize=18)
    fig.text(0.5, 0.04, 'time', ha='center')
    fig.text(0.04, 0.5, 'firing rate (HZ)', va='center', rotation='vertical')

    plt.show()


