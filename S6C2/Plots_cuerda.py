import numpy as np
import matplotlib.pylab as plt

datos=np.genfromtxt("datos.dat")
x=datos[:,0]
u=datos[:,1]

plt.figure()
plt.plot(x,u)
plt.xlabel("t")
plt.ylabel("x")
plt.title("Cuerda inicial")
plt.grid()
plt.savefig("plot.png")
plt.close()
