import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import fft, fftfreq, fft2, ifft2

seria=plt.imread("cara_02_grisesMF.png")
feliz=plt.imread("cara_03_grisesMF.png")

print(np.shape(feliz))

def LowP(imagen,corte=.1):
    r,M=np.shape(imagen)
    if(M%2!=0):
        M+=1
    h=np.sin(2*np.pi*corte*(imagen-(M/2)))/(imagen-(M/2))
    w=0.54-0.46*np.cos(2*np.pi*imagen/M)
    im=w*h
    return im

Fseria=fft2(seria).real
Fseria=np.log10(abs(Fseria))
print(np.shape(Fseria))
print(Fseria)

filtro=LowP(Fseria)
IFseria=ifft2(filtro).real


plt.figure()
plt.subplot(2,2,1)
plt.imshow(seria)
plt.subplot(2,2,2)
plt.imshow(filtro)
plt.subplot(2,2,3)
plt.imshow(IFseria)
plt.subplot(2,2,4)
plt.imshow(np.log10(abs(IFseria)))
plt.savefig("filtro.png")
plt.close()