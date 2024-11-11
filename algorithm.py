

import numpy as np
from scipy.special import erf
from trash_data import TRASH_AVG, TRASH_STD

# parameters
W_p = TRASH_AVG*7*10**3
SIGMA_p = TRASH_STD*7*10**3
SIGMA_c = np.array([1]*12)*10**3
P = np.array([78380,92445,163141,131351,63600,155614,222129,231983,110458,130440,125771,180206])/10**3
A = np.array([40710976, 37719022, 46882269, 49291774, 43796730, 38695300, 53154204, 55045848, 41892850, 39080798, 66146445, 77969957])/10.764/10**6
N_total = 1000
Z_min = 1
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
def Q(T):
    mu = W_p-R*T
    sigma = np.sqrt(SIGMA_p**2+SIGMA_c**2*T)
    delta = 1/2*(mu*erf(mu/(SQRT_2*sigma))+mu+SQRT_2_OVER_PI*sigma*np.exp(-mu**2/(2*sigma**2)))
    S = np.average(delta/(A*P))
    return np.sqrt(1/12*np.sum((delta/(A*P)-S)**2))

#use hill climbing algorithm to find the minimum Q
def findMin(T_11,C, iterations):
    #if the number of iterations is greater than maximum iterations, return
    if iterations > MAX_ITERATION:
        print("\t Max iterations reached")
        return False
    # append the 12th index to T_11 to make T
    T = np.append(T_11, C-np.sum(T_11))
    # compute Q
    Q_current = Q(T)
    # whether there the current is within the constraint for Q
    if Q_current <= Q_bound:
        print("\t Q = "+str(Q_current)+" is minimized with "+str(iterations)+" steps at: " + str(T))
        return True
    
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
                Q_new = Q(T_new)
                
                # If the new schedule has a lower Q, than record that move
                if Q_new < Q_min:
                    target_move = [i,j]
                    Q_min = Q_new
         
    # is not moving is the best option, then the current Q is minimum
    if target_move[1] == 0:
        print("\t Q = "+str(Q_current)+" is minimized with "+str(iterations)+" steps at: " + str(T))
        return False
    
    # do the move
    T_11_new = T_11
    T_11_new[target_move[0]]+=target_move[1]
    
    # iterate
    return findMin(T_11_new, C, iterations+1)

#Check whether the cost has any possible schedule within the constraint
def valid(C):
    #initial position
    T_11 = np.round((upper[:11]-lower[:11])*(C-C_min)/(C_max-C_min))+lower[:11]
    print("\nCost = " + str(C)+ " with Q = "+str(Q(np.append(T_11, C-np.sum(T_11)))))
    return findMin(T_11,C,0) 

#Binary search

left = C_min
right = C_max

while left < right:
    mid = (left + right) // 2
    if valid(mid):
        right = mid
    else:
        left = mid+1

print("Cost boundary: " + str(C_min)+"<= Cost <="+str(C_max))
print("The minimum cost is : "+str(left))

    
