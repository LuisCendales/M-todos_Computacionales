import numpy as np
import matplotlib.pylab as plt

dataeuler=np.genfromtxt("euler.dat")

plt.figure()
plt.plot(dataeuler[:,0],dataeuler[:,1])
plt.xlabel('t')
plt.ylabel('y')
plt.title('ODE por Euler')
plt.grid()
plt.savefig("euler.png")
plt.close()