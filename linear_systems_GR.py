#code worked on by Grady Robbins
import numpy as np

A = np.array([[0,1,4,1],[3,4,-1,-1],[1,-4,0,5],[2,-2,1,3]])# setting up arrays
v = np.array([-4,3,9,7])
Nrows = len(v)
for m in range(Nrows):
    while A[m,m] == 0:#pivoting scheme
        i = np.random.randint(0,4)        
        Aold = np.copy(A)
        vold = np.copy(v)
        A[m] = Aold[i]
        A[i] = Aold[m]
        v[m] = vold[i]
        v[i] = vold[m]
        
for m in range(Nrows): #solve linear equations
    divisor = A[m,m]
    A[m,:] = A[m,:]/divisor
    v[m] = v[m]/divisor
    for i in range(m+1,Nrows):
        mult_factor = A[i,m]
        A[i,:] = A[i,:] - mult_factor*A[m,i]
        v[i] = v[i] - mult_factor*v[m]
#back substitution
x = np.zeros(Nrows)
for m in range(Nrows-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,Nrows):
        x[m] = x[m] - A[m,i]*x[i]
print(x)
