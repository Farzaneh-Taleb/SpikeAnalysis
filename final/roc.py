import utility_functions as utility
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn import svm
from sklearn.metrics import  accuracy_score
from sklearn.metrics import  roc_curve,auc
from scipy import interp

"""
@author Farzaneh.Tlb
2/28/19 7:31 PM
Implementation of ROC
"""


ut = utility.Utility_Functions()
all_X1  = np.zeros(shape=[928 , 25])
all_X2  = np.zeros(shape=[928 , 25])
all_Y = ut.conNU_data[:,0]

all_Y = np.where(all_Y <= 8 ,1, 2)
for n  in range(ut.number_of_neurons):
    neuron_all = ut.get_neuron(n)
    neuron1  = neuron_all[:, 1000:1501]
    neuron2  = neuron_all[:, 2700:3200]
    all_X1[:,n] = np.transpose(ut.compute_summation_over_time(neuron1))
    all_X2[:,n] = np.transpose(ut.compute_summation_over_time(neuron2))


kf = KFold(n_splits=4)
clf = svm.SVC(kernel='linear', decision_function_shape='ovr',probability=True)


tprs = []
aucs = []
mean_fpr = np.linspace(0, 1, 100)

def calculate_ROC(all_X):
    i = 0
    for train, test in kf.split(all_X ,all_Y):
        X_train, X_test, y_train, y_test = all_X[ train], all_X[ test], all_Y[train], all_Y[test]
        probas_ = clf.fit(X_train, y_train).predict_proba(X_test)
        print("p" , probas_)
        # Compute ROC curve and area the curve
        fpr, tpr, thresholds = roc_curve(y_test, probas_[:, 1] , pos_label=2)
        # tprs.append(interp(mean_fpr, fpr, tpr))
        # tprs[-1][0] = 0.0
        roc_auc = auc(fpr, tpr)
        # aucs.append(roc_auc)
        plt.plot(fpr, tpr, lw=1, alpha=0.3,
                 label='ROC fold %d (AUC = %0.2f)' % (i, roc_auc))

        i += 1
    plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r',
             label='Chance', alpha=.8)
    return roc_auc

    # mean_tpr = np.mean(tprs, axis=0)
    # mean_tpr[-1] = 1.0
    # mean_auc = auc(mean_fpr, mean_tpr)
    # std_auc = np.std(aucs)
    # plt.plot(mean_fpr, mean_tpr, color='b',
    #          label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
    #          lw=2, alpha=.8)

    # std_tpr = np.std(tprs, axis=0)
    # tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
    # tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
    # plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.2,
    #                  label=r'$\pm$ 1 std. dev.')

# print("auc" ,calculate_ROC(all_X1))
# plt.xlim([-0.05, 1.05])
# plt.ylim([-0.05, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic example')
# plt.legend(loc="lower right")
# plt.show()
print("auc" ,calculate_ROC(all_X2))
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()