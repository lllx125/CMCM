import numpy as np

T = np.array([ 60.,  67., 126.,  93.,  49.,  99., 159., 170.,  89., 106., 106.,
        152.])/3
m = np.array([0.5]*12)

# no element is set A, all element is in set B
A = 0
minimum = np.sum(T*m)

#enumerate all combinations
for i in range(2**12):
    # trucks in plan A morning
    Am = 0
    # trucks in plan A evening
    Ae = 0
    # trucks in plan B morning
    Bm = 0
    # trucks in plan B evening
    Be = 0
    for n in range(12):
        # whether district n is in A is determined by (i//2^n)%2==1, district is from 0 to 11
        if (i//2**n)%2==1:
            Am += np.ceil(T[n]*m[n])
            Ae += np.ceil(T[n]*(1-m[n]))
        else:
            Bm += np.ceil(T[n]*m[n])
            Be += np.ceil(T[n]*(1-m[n]))
    if minimum > max(Am,Ae,Bm,Be):
        minimum =  max(Am,Ae,Bm,Be)
        A = i

for n in range(12):
    print("District "+str(n+1)+": ", 'A' if (A//2**n)%2==1 else "B")
    
print(minimum)

