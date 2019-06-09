import utility_functions as utility
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

"""
@author Farzaneh.Tlb
2/26/19 11:18 AM
Implementation of Mutual Information 
"""
ut = utility.Utility_Functions()

ent_r_s = np.zeros(shape=[8, ])
p_s = np.zeros(shape=[8, ])
p_r_s = np.zeros(shape=[8, ])
p_r = 0

def cal_p_r( n, start_time , end_time):
    sum = 0
    trials  = ut.get_neuron(n)
    num = trials.shape[0]
    for trial in trials:
        sum += np.sum(trial[start_time:end_time])
    return sum/(num*(end_time-start_time))

def cal_p_r_3( n , t, start_time , end_time):
    sum = 0
    trials  = ut.get_neuron(n)
    trial  =trials[t]
    return np.sum(trial[start_time : end_time])/ (end_time - start_time)

def get_number_of_trial_per_neuron(n) :
    trials  = ut.get_neuron(n)
    return trials.shape[0]



def calculate_MI(start_time, end_time):
    MI = np.zeros(shape=[25, ])
    MI2 = np.zeros(shape=[25, ])
    MI3 = np.zeros(shape=[25, ])
    for n in range(ut.number_of_neurons):
        p_r  = cal_p_r( n  ,start_time, end_time)


        # p_r  = cal_p_r_3( n ,0 ,start_time, end_time)
        print("pr", p_r)
        for c in range(ut.conditions - 8):
            trials1 = ut.get_trial_by_condition(n, c + 1)
            trials2 = ut.get_trial_by_condition(n,c+9)
            all_trials = np.concatenate((trials1,trials2))




            print("tr" , all_trials.shape)
            number_of_trials_per_c = all_trials.shape[0]
            data_to_histogram = ut.get_indecis_of_spikes(all_trials[:, start_time:end_time])
            hist, bins = np.histogram(data_to_histogram, bins='fd', density=True)
            print(np.sum(hist[0]))
            ent_r_s[c] = -(hist[0] * np.log2(np.abs(hist[0]))).sum()

            s = ut.compute_summation_over_time(all_trials)
            p_r_s[c] = s.sum()/((end_time -start_time)*number_of_trials_per_c)
            # p_s[c] = number_of_trials_per_c / ut.number_of_all_trials
            p_s[c] = number_of_trials_per_c / get_number_of_trial_per_neuron(n)

        trials = ut.get_neuron(n)
        print("ttt2"  , trials.shape)
        trials = trials[: ,start_time:end_time]
        s = 20
        temp = np.add.reduceat(trials, np.arange(0, 500, s), axis=1)
        # temp = np.sum(temp, axis=0) / s
        temp = temp[11]/20
        print("temppp", temp)
        exp1 = -(np.multiply(temp, np.log2(temp))).sum()
        print("exp1",exp1)

        exp2 = np.multiply(p_s , p_r_s)
        exp3 = np.multiply(exp2 , np.log2(p_r_s))

        x2 = np.multiply(ent_r_s, p_s)
        x2 = np.sum(x2)
        trials_by_neuron = ut.get_neuron(n)
        data_to_histogram = ut.get_indecis_of_spikes(trials_by_neuron[:, start_time:end_time])
        hist = np.histogram(data_to_histogram, bins='fd', density=True)
        ent_r = -(hist[0] * np.log2(np.abs(hist[0]))).sum()
        MI[n] = ent_r - x2
        MI2[n] = (np.multiply(p_s,p_r_s)*np.log2(p_r_s / p_r)).sum()

        print("E" , exp1 , exp3)
        MI3[n] = exp1 + exp3.sum()



    return MI3




MI1 = calculate_MI(1000, 1501)
MI2 = calculate_MI(2700, 3201)

fig, axs = plt.subplots(1, 3,figsize=(20, 10))

# axs[0].hist(MI1, bins='fd' ,alpha=0.5  )
# axs[0].hist(MI2, bins='fd' , alpha=0.5 )
# plt.show()

axs[1].bar(np.arange(1, 26), MI1 , alpha=0.5 ,   )
axs[1].bar(np.arange(1, 26), MI2 , alpha=0.5 , )

# plt.show()

axs[2].scatter(MI1.flatten(), MI2.flatten())
# plt.scatter(MI2.flatten())
plt.show()

print(stats.ttest_ind(MI1, MI2))

# p_r =
# p_r_s =
# p_s_r =
