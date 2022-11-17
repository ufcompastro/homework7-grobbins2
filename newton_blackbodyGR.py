import numpy as np

def B(T):
    return  (2*h*(v**3)/(c**2)) /((np.exp((h*v)/(k*T)))-1)
h = 6.626e-27 # in erg s                                                                                                                             
c = 3.00e10 #in cm                                                                                                                               
wavelength = 0.087 #in cm                                                                                                                      
v = c / wavelength
k = 1.38e-16 #in ergsK                                                                                                           
B_obs = 1.25e-12 #in cgs                                                                                                                                                             

n = .01 #step size
                                                                                                                                              
def Bprime(T,B,n):
    return (B(T + n) - B(T - n))/(2*n) #defining derivative
T0 = np.random.randint(1,10000) #guessing T
Tnew = T0
print("initial/random temp:",Tnew) 
counter = 0
while(B(T0) > B_obs*1.0002) or (B(T0) < B_obs/1.0002): # repeat until within tolerance
    if B(T0) < B_obs: #account for which direction of derivative
        Tnew = T0 + B(T0)/(Bprime(T0,B,n)*10000)
    else:
        Tnew = T0 - B(T0)/(Bprime(T0,B,n)*10000)
    T0 = Tnew
    counter +=1
    if counter > 100000: #prevent inifinity time
        print('need more time')
        break
    if (B(T0) < B_obs*1.0002) and (B(T0) > B_obs/1.0002): #double ensure within tolerance
        print('')
        break
print('estimated intensity within tolerance:',B(Tnew))
print("using Newton-Rhapson method, the estimated temperature is",Tnew,"Kelvin")
