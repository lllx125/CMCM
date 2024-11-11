#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:35:26 2024

@author: lihao
"""

import numpy as np
from scipy.special import erf
from trash_data import TRASH_AVG, TRASH_STD

W_p = TRASH_AVG*7*10**3
SIGMA_p = TRASH_STD*7*10**3
SIGMA_c = np.array([0]*12)*10**3
P = np.array([78380,92445,163141,131351,63600,155614,222129,231983,110458,130440,125771,180206])/10**3
A = np.floor(np.array([40710976, 37719022, 46882269, 49291774, 43796730, 38695300, 53154204, 55045848, 41892850, 39080798, 66146445, 77969957])/10.764/10**3)/10**3
N_total = 1000
Z_min = 0.001
Z_max = 5
Q_bound = 4
R = 12*10**3
MAX_ITERATION = 500
SQRT_2 = np.sqrt(2)
SQRT_2_OVER_PI = np.sqrt(2/np.pi)

#T = np.array([ 59,  66, 123,   92,  48,  98, 157, 168,  87, 103, 106, 145])
T = np.array([ 58,  65, 121,   90,  47,  96, 155, 165,  85, 100, 105, 142])


mu = W_p-R*T
sigma = np.sqrt(SIGMA_p**2+SIGMA_c**2*T)
delta = 1/2*(mu*erf(mu/(SQRT_2*sigma))+mu+SQRT_2_OVER_PI*sigma*np.exp(-mu**2/(2*sigma**2)))
S = np.average(delta/(A*P))
Q = np.sqrt(1/12*np.sum((delta/(A*P)-S)**2))

print(delta)
print(Q)
print(A)
print(np.sum(T))