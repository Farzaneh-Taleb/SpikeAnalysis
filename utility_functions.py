"""
@author Farzaneh.Tlb
2/24/19 7:09 PM
Implementation of .... (Fill this line)
"""
from scipy.io import loadmat
import numpy as np


class Utility_Functions:
    def __init__(self):
        Nu = loadmat('datas/Nu.mat')
        conNU = loadmat('datas/conNU.mat')
        self.Nu_data = Nu['nu']  # (25,928,3500)
        self.conNU_data = conNU['condNU']  # (928, 1)

        condLFP = loadmat('datas/condLFP.mat')
        LFP1 = loadmat('datas/LFP1.mat')
        self.condLFP_data = condLFP['Cond'] #(963,1)
        self.LFP_data = LFP1['LFP'] #(963, 8000)
        self.neurons = self.Nu_data[0]
        self.neurons_array = np.empty(shape=[25, 928, 3500])
        self.times = 3500
        self.number_of_neurons=25
        self.conditions = 16
        self.number_of_all_trials = 928
        self.get_nurons_array()

    def get_nurons_array(self):
        for index, neuron in np.ndenumerate(self.neurons):
            self.neurons_array[index] = neuron
        return self.neurons_array

    def get_neuron(self,i):
        return  self.neurons_array[i]

    def getTrialsSummationByCondition(self  , neuron_number , condition):
        s = self.neurons_array[neuron_number,(self.conNU_data==condition).squeeze() , :]
        data = np.sum(s , axis=0 )
        return data, s.shape[0]

    def  get_trial_by_condition(self, neuron_number, condition):
        s = self.neurons_array[neuron_number,(self.conNU_data==condition).squeeze() , :]
        return  s

    def get_indecis_of_spikes(self,trials):
        non_zero_indecis  = np.nonzero(trials)
        return non_zero_indecis[0] , non_zero_indecis[1]

    def get_condition(self , cond_number):
        if cond_number > 8:
            angle = cond_number - 8
        else:
            angle = cond_number
        if cond_number > 8:
            radial = 2
        else:
            radial = 1
        return angle, radial


    def compute_summation_over_time(self, trials):
        return  np.sum(trials , axis=1)

    def get_radial_over_trials(self , trials):
        radial_over_trials = np.where(trials > 8, 2, 1)
        return radial_over_trials
