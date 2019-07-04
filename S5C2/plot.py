import numpy as np
import matplotlib.pylab as plt

dataeuler=np.genfromtxt("euler.dat")
dataRK4=np.genfromtxt("RK4.dat")

plt.figure(figsize=(15,5))
plt.subplot(1,2,1)
plt.plot(dataeuler[:,0],dataeuler[:,1],c='b')
plt.xlabel('t')
plt.ylabel('y')
plt.title('ODE por Euler')
plt.grid()
plt.subplot(1,2,2)
plt.plot(dataRK4[:,0],dataRK4[:,1],c='r')
plt.xlabel('t')
plt.ylabel('y')
plt.title('ODE por RK4')
plt.grid()
plt.savefig("ODE.png")
plt.close()
