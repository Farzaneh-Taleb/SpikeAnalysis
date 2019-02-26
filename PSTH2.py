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
trials1 = ut.get_trial_by_condition(0,1)
trial_numbers1 , times1 = ut.get_indecis_of_spikes(trials1)

trials2 = ut.get_trial_by_condition(0,2)
trial_numbers2 , times2 = ut.get_indecis_of_spikes(trials2)

trials3 = ut.get_trial_by_condition(0,3)
trial_numbers3 , times3 = ut.get_indecis_of_spikes(trials3)
# plt.hist(times, bins='auto')
sns.distplot(times1,bins='auto',norm_hist=True,hist=False)
sns.distplot(times2,bins='auto',norm_hist=True,hist=False)
sns.distplot(times3,bins='auto',norm_hist=True,hist=False)
plt.show()
# print(times)


# p_r =
# p_s =
# p_r_s =
# p_s_r =