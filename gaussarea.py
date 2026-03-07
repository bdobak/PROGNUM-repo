import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

A=float(input("Enter A: "))
x0=float(input("Enter x0: "))
Asig=float(input("Enter sigma: "))
z0=float(input("Enter z0= "))
a=float(input("Enter the lower limit: "))
b=float(input("Enter upper limit: "))

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

x=np.linspace(-10,10,200)
y=gauss(x,A,x0,sig,z0)
plt.plot(x,y)

A1=quad(gauss,a,b, (A,x0,sig,z0))
print(f"The area under the curve from {a} to {b} is {A1[0]}")
x1=np.linspace(a,b,200)
y1=gauss(x1,A,x0,sig,z0)
plt.fill_between(x1,y1)

plt.show()