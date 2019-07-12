import numpy as np
import matplotlib.pylab as plt

Ini=np.genfromtxt("PlacaIni.dat")
t1b=np.genfromtxt("t1b.dat")
t1c=np.genfromtxt("t1c.dat")
t2b=np.genfromtxt("t2b.dat")
t2c=np.genfromtxt("t2c.dat")
t3b=np.genfromtxt("t3b.dat")
t3c=np.genfromtxt("t3c.dat")

plt.figure(figsize=(15,15))

plt.subplot(3,3,1)
plt.imshow(Ini)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Placa Cerrada")
plt.colorbar()

plt.subplot(3,3,2)
plt.imshow(t1b)
plt.xlabel("x")
plt.ylabel("y")
plt.title("T100 Cerrada")
plt.colorbar()

plt.subplot(3,3,3)
plt.imshow(t1c)
plt.xlabel("x")
plt.ylabel("y")
plt.title("T2500 Cerrada")
plt.colorbar()

plt.subplot(3,3,4)
plt.imshow(Ini)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Placa Abierta")
plt.colorbar()

plt.subplot(3,3,5)
plt.imshow(t2b)
plt.xlabel("x")
plt.ylabel("y")
plt.title("T100 Abierta")
plt.colorbar()

plt.subplot(3,3,6)
plt.imshow(t2c)
plt.xlabel("x")
plt.ylabel("y")
plt.title("T2500 Abierta")
plt.colorbar()

plt.subplot(3,3,7)
plt.imshow(Ini)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Placa Periódica")
plt.colorbar()

plt.subplot(3,3,8)
plt.imshow(t3b)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Placa Periódica")
plt.colorbar()

plt.subplot(3,3,9)
plt.imshow(t3c)
plt.xlabel("x")
plt.ylabel("y")
plt.title("T2500 Periódica")
plt.colorbar()

plt.savefig("plot.png")
plt.close()