import numpy as np
import matplotlib.pylab as plt

datos1=np.genfromtxt("datos1.dat")
x=datos1[:,0]
u1=datos1[:,1]
u2=datos1[:,2]


plt.figure()
plt.plot(x,u1,c='b')
plt.plot(x,u2,c='r')
plt.xlabel("x")
plt.ylabel("phi")
plt.title("Cuerda inicial")
plt.grid()
plt.savefig("plot.png")
plt.close()
