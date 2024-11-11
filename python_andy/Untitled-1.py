

import numpy as np
from scipy.special import erf
from trash_data import TRASH_AVG, TRASH_STD

# parameters
W_p = TRASH_AVG*7*10**3
SIGMA_p = TRASH_STD*7*10**3
SIGMA_c = np.array([0.18]*12)*10**3
P = np.array([78380,92445,163141,131351,63600,155614,222129,231983,110458,130440,125771,180206])/10**3
A = np.floor(np.array([40710976, 37719022, 46882269, 49291774, 43796730, 38695300, 53154204, 55045848, 41892850, 39080798, 66146445, 77969957])/10.764/10**6)
N_total = 1000
Z_min = 2
Z_max = 5
Q_bound = 4
R = 12*10**3
MAX_ITERATION = 500

#Calculate lower bound for each district
lower = np.ceil((2*R*W_p+Z_min**2*SIGMA_c**2+((2*R*W_p+Z_min**2*SIGMA_c**2)**2-4*R**2*(W_p**2-Z_min**2*SIGMA_p**2))**(1/2))/(2*R**2)) 

#Calculate upper bound for each district
upper = np.floor((2*R*W_p+Z_max**2*SIGMA_c**2+((2*R*W_p+Z_max**2*SIGMA_c**2)**2-4*R**2*(W_p**2-Z_max**2*SIGMA_p**2))**(1/2))/(2*R**2)) 

#bounds for C
C_min = np.sum(lower)
C_max = np.sum(upper)

# constants
SQRT_2 = np.sqrt(2)
SQRT_2_OVER_PI = np.sqrt(2/np.pi)

# whether the upper bound is too lose
if np.sum(upper)>12*N_total:
    print("upper bound is too lose")

#compute Q
T = np.array([ 61.  ,68. ,127.  ,94.  ,51., 100., 161., 172.  ,90., 108. ,108., 154.])

mu = W_p-R*T
sigma = np.sqrt(SIGMA_p**2+SIGMA_c**2*T)
delta = 1/2*(mu*erf(mu/(SQRT_2*sigma))+mu+SQRT_2_OVER_PI*sigma*np.exp(-mu**2/(2*sigma**2)))
S = np.average(delta/(A*P))
Q = np.sqrt(1/12*np.sum((delta/(A*P)-S)**2))

print(delta)
