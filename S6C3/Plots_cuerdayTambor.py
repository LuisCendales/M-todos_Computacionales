import numpy as np
import matplotlib.pylab as plt

datos=np.genfromtxt("datos1.dat")
x=datos[0,:]


plt.figure()
for i in range(1,len(datos)):
    plt.plot(x,datos[i,:],label="t="+str(i))
plt.xlabel("x")
plt.ylabel("phi")
plt.title("Cuerda")
plt.grid()
plt.legend(loc=1)
plt.savefig("plot.png")
plt.close()
