import numpy as np
import matplotlib.pylab as plt

datos=np.genfromtxt("datos.dat")
t=datos[:,0]
x=datos[:,1]
v=datos[:,2]

plt.figure()
plt.plot(t,x,c='r')
plt.xlabel("t")
plt.ylabel("x")
plt.title("Posición vs. Tiempo Resorte sin fricción")
plt.grid()
plt.savefig("CendalesLuisResorte.png")
plt.close()
