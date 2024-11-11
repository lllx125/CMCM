import matplotlib.pyplot as plt
import numpy as np
from algorithm import C_min, C_max, Q, lower, upper

randplt = []
fixplt = []
MAX_ITERATION = 500

def findMin(T_11,C, iterations):
    # append the 12th index to T_11 to make T
    T = np.append(T_11, C-np.sum(T_11))
    # compute Q
    Q_current = Q(T)

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
                Q_new = Q(T_new)
                
                # If the new schedule has a lower Q, than record that move
                if Q_new < Q_min:
                    target_move = [i,j]
                    Q_min = Q_new
    
    # if not moving is the best option, then the current Q is minimum               
    if target_move[1] == 0:
        return  Q_current
    
    
    # do the move
    T_11_new = T_11
    T_11_new[target_move[0]]+=target_move[1]
    
    # iterate
    return findMin(T_11_new, C, iterations+1)
    
    

#Check whether the cost has any possible schedule within the constraint
def min_Q(C,T_11):
    #initial position
    #T_11 = np.round((upper[:11]-lower[:11])*(C-C_min)/(C_max-C_min))+lower[:11]
    #random initial position
    #T_11 = np.array([np.random.randint(l, u + 1) for l, u in zip(lower[:11], upper[:11])])
    return findMin(T_11,C,0) 

for i in range(int(C_min),int(C_max)+1):
    for j in range (10):
        T_11 = np.array([np.random.randint(l, u + 1) for l, u in zip(lower[:11], upper[:11])])
        randplt.append((i,np.log(min_Q(i,T_11))))
    T_11 = np.round((upper[:11]-lower[:11])*(i-C_min)/(C_max-C_min))+lower[:11]
    fixplt.append((i,np.log(min_Q(i,T_11))))
  
x, y = zip(*randplt)  
plt.scatter(x, y, color = 'blue',s=5,label='random initial value')
x, y = zip(*fixplt)  
# plot 
plt.scatter(x, y, color = 'orange',s=5, label='proposed initial value')
plt.legend()
plt.xlabel("C")    # X-axis label
plt.ylabel("log(Q)")    # Y-axis label   