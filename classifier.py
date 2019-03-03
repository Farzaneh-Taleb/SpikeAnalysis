import numpy as np
import utility_functions as utility
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from scipy.stats import sem, t
from scipy import mean





"""
@author Farzaneh.Tlb
2/27/19 11:22 AM
Implementation of classifier 
"""
ut = utility.Utility_Functions()
all_X  = np.zeros(shape=[928 , 25])
all_Y = ut.conNU_data[:,0]

all_Y = np.where(all_Y <= 8 , all_Y, all_Y-8)
for n  in range(ut.number_of_neurons):
    neuron = ut.get_neuron(n)
    all_X[:,n] = np.transpose(ut.compute_summation_over_time(neuron))



# kf = KFold(n_splits=4)
# for train , test  in kf.split(all_X ,all_Y):
#     X_train, X_test, y_train, y_test = all_X[ train], all_X[ test], all_Y[train], all_Y[test]
#
#     clf = svm.SVC(kernel='linear', decision_function_shape='ovr').fit(X_train, y_train)
#     y  =clf.predict(X_test)
#     print(accuracy_score(y, y_test))


clf = svm.SVC(kernel='linear', decision_function_shape='ovr')
scores = cross_val_score(clf, all_X, all_Y, cv=5)
print(scores)
print("Accuracy:"  , scores.mean(),"(+/-" , scores.std() * 2 , ")")
print(scores.mean() +  scores.std() * 2 , scores.mean() -  scores.std() * 2)


n = ut.number_of_all_trials
mean = mean(scores)
std_err = sem(scores)

CI1 = mean + 1.96 * std_err
CI2 = mean - 1.96 * std_err
print(CI1  , CI2 , 1.96*std_err)
# up = scores.mean() + 1.96 * np.sqrt( (std_err * (1 - std_err)) / n)
# low = scores.mean() - 1.96 * np.sqrt( (std_err * (1 - std_err)) / n)
# print("up" , up)
# print("low" , low)




#sem sigma / radical n


