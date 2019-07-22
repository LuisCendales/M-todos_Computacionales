import numpy as np
import matplotlib.pylab as plt

a=np.genfromtxt('TempPomedios.txt')

plt.figure()
plt.plot(a[:,0],a[:,1],label='T')
plt.title('Variaciones de T con respecto al promedio')
plt.xlabel('Años')
plt.ylabel('T con respecto al promedio (Celcius)')
plt.grid()
plt.legend()
plt.savefig('plotTemp.png')
plt.close()