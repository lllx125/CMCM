import matplotlib.pyplot as plt
import numpy as np
from scipy.special import erf
from algorithm import C_min, C_max, lower, upper
from trash_data import TRASH_AVG, TRASH_STD

SQRT_2 = np.sqrt(2)
SQRT_2_OVER_PI = np.sqrt(2/np.pi)

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

def Q(T):
    mu = W_p-R*T
    sigma = np.sqrt(SIGMA_p**2+SIGMA_c**2*T)
    delta = 1/2*(mu*erf(mu/(SQRT_2*sigma))+mu+SQRT_2_OVER_PI*sigma*np.exp(-mu**2/(2*sigma**2)))
    S = np.average(delta/(A*P))
    return np.sqrt(1/12*np.sum((delta/(A*P)-S)**2)), S

def findMin(T_11,C, iterations):
    # append the 12th index to T_11 to make T
    T = np.append(T_11, C-np.sum(T_11))
    # compute Q
    Q_current, S = Q(T)

    #if the number of iterations is greater than maximum iterations, return
    if iterations > MAX_ITERATION:
        return Q_current
    
    # record minimum Q and the move that minimize Q
    Q_min = Q_current 
    #target_move[0] is the index to change, target_move[1] is the direction of change, either -1 or 1, 0 means not moving
    target_move = [0,0] 
    
    # iterate through all possible moves
    for i in range(11):
        for j in [-1,1]:
            # whether the new condition lie within the upper and lower bounds for each index
            if lower[i]<=T[i]+j and T[i]+j <= upper[i] and lower[11]<=T[11]-j and T[11]-j <= upper[11]:
                # the new schedule
                T_new = T
                T_new[i]+=j
                T_new[11]-=j
                # compute Q for the new schedule
                Q_new, S = Q(T_new)
                
                # If the new schedule has a lower Q, than record that move
                if Q_new < Q_min:
                    target_move = [i,j]
                    Q_min = Q_new
    
    # if not moving is the best option, then the current Q is minimum               
    if target_move[1] == 0:
        return  Q_current, S
    
    
    # do the move
    T_11_new = T_11
    T_11_new[target_move[0]]+=target_move[1]
    
    # iterate
    return findMin(T_11_new, C, iterations+1)
    
    

#Check whether the cost has any possible schedule within the constraint
def min_Q(C):
    #initial position
    T_11 = np.round((upper[:11]-lower[:11])*(C-C_min)/(C_max-C_min))+lower[:11]
    #random initial position
    #T_11 = np.array([np.random.randint(l, u + 1) for l, u in zip(lower[:11], upper[:11])])
    return findMin(T_11,C,0) 

if __name__ == '__main__':
    x = range(int(C_min),int(C_max)+1)
    Qs = []
    Ss = []


    for i in x:
        #compute minimum Q for each cost
        res = min_Q(i)
        Qs.append(res[0])
        Ss.append(res[1])


        
    # plot 
    plt.plot(x,Qs)   
    plt.xlabel("C")    # X-axis label
    plt.ylabel("Q")    # Y-axis label
    plt.show()   