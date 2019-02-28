import utility_functions as utility
import numpy as np
from sklearn.model_selection import KFold
from sklearn import svm
from sklearn.metrics import  accuracy_score
from sklearn.metrics import  roc_curve



"""
@author Farzaneh.Tlb
2/28/19 7:31 PM
Implementation of ROC
"""


ut = utility.Utility_Functions()
all_X  = np.zeros(shape=[928 , 25])
all_Y = ut.conNU_data[:,0]

all_Y = np.where(all_Y <= 8 ,1, 2)
for n  in range(ut.number_of_neurons):
    neuron = ut.get_neuron(n)
    neuron  = neuron[:, 1000:1501]
    all_X[:,n] = np.transpose(ut.compute_summation_over_time(neuron))


kf = KFold(n_splits=4)

for train , test  in kf.split(all_X ,all_Y):
    X_train, X_test, y_train, y_test = all_X[ train], all_X[ test], all_Y[train], all_Y[test]

    clf = svm.SVC(kernel='linear', decision_function_shape='ovr').fit(X_train, y_train)
    y  =clf.predict(X_test)
    score = accuracy_score(y, y_test)
    print(score)

    fpr, tpr, thresholds = roc_curve(y, y_test, pos_label=2)
    print("fpr" , fpr)
    print("tpr" , tpr)
    print("th" , thresholds)
