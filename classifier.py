import numpy as np
import utility_functions as utility
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score



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
    # print("n" , n  ,all_X)

# print(all_X.shape)
# print(all_Y.shape)

# X_train, X_test, y_train, y_test = train_test_split( all_X, all_Y, test_size=0.3)
# print(X_train.shape)
# print(X_test.shape)
# print(y_train.shape)
# print(y_test.shape)
# clf = svm.SVC(kernel='linear' , decision_function_shape='ovr' ).fit(X_train,y_train)
# y  =clf.predict(X_test)
# print(accuracy_score(y , y_test))


kf = KFold(n_splits=4)

for train , test  in kf.split(all_X ,all_Y):
    X_train, X_test, y_train, y_test = all_X[ train], all_X[ test], all_Y[train], all_Y[test]

    clf = svm.SVC(kernel='linear', decision_function_shape='ovr').fit(X_train, y_train)
    y  =clf.predict(X_test)
    print(accuracy_score(y, y_test))
