import numpy as np

def B(T):
    return  (2*h*(v**3)/(c**2)) /((np.exp((h*v)/(k*T)))-1)
h = 6.626e-27 # in erg s
c = 3.00e10 #in cm 
wavelength = 0.087 #in cm
v = c / wavelength
k = 1.38e-16 #in ergsK
B_obs = 1.25e-12 #in cgs

#Bisection Method

T0 = np.random.randint(1,1000)
T1 = np.random.randint(1,1000)
m = 0
while (B(T0) and B(T1) > B_obs) or (B(T1) and B(T0) < B_obs):
    T0 = np.random.randint(1,1000)
    T1 = np.random.randint(1,1000)
    m +=1
    if m > 10000:
        break
if T0 > T1:
    T0,T1 = T1,T0
print(T0,T1)
T1new = T1
l=0
while (B(T0) < B_obs*10) and (B(T0) > B_obs/10):
    T0new = (T1 + T0)/2
    if (B(T0new) > B_obs):
        T0new = T0
        T1new = (T1 + T0)/2
    T1 = T1new
    T0 = T0new
    l +=1
    if l>100:
        break
    print(T0,T1)
print(B(T0),B(T1))

print("the observed Temperature using bisection method is near",T0,"Kelvin")
