import numpy as np
import matplotlib.pylab as plt

Ini=np.genfromtxt("PlacaIni.dat")
T100=np.genfromtxt("t100.dat")
T2500=np.genfromtxt("t2500.dat")

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(Ini)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Placa Inicial")
plt.colorbar()

plt.subplot(1,3,2)
plt.imshow(T100)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Placa T100")
plt.colorbar()

plt.subplot(1,3,3)
plt.imshow(T2500)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Placa T2500")
plt.colorbar()

plt.savefig("plot.png")
plt.close()
