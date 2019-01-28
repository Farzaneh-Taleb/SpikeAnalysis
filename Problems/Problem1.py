# from mat4py import loadmat
from scipy.io import loadmat
import numpy as np

"""
@author Farzaneh.Tlb
Implementation of RasterPlot and PSTH
"""

Nu = loadmat('../datas/Nu.mat')
condLFP = loadmat('../datas/condLFP.mat')
LFP1 = loadmat('../datas/LFP1.mat')
conNU = loadmat('../datas/conNU.mat')

Nu_data = Nu['nu'] #(25,928,3500)
condLFP_data = condLFP['Cond'] #(963,1)
LFP_data = LFP1['LFP'] #(963, 8000)
conNU_data = conNU['condNU'] #(928, 1)
