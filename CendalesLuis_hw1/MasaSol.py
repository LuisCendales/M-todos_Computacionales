import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits import mplot3d

AU = 149597870700                     # 1 Unidad Astronómica en metros
G = 6.673*(10**-11)                   # Constante de Gravitación Universal (N*m2/kg2)


earth=np.genfromtxt('EarthOrbit.dat')
Et=np.array(earth[:,0]*31536000)                # El tiempo se pasa de años a segundos
EX=np.array(earth[:,1]*AU)                     # Posición de la Tierra se pasa a metros en x, y y z
EY=np.array(earth[:,2]*AU)
EZ=np.array(earth[:,3]*AU)
Er=np.array(np.sqrt((EX**2)+(EY**2)+(EZ**2)))  # Lista de distancias hasta el sol en cada posición



mars=np.genfromtxt('MarsOrbit.dat')
Mt=np.array(mars[:,0]*31536000)                 # El tiempo se pasa de años a segundos
MX=np.array(mars[:,1]*AU)                      # Posición de Marte se pasa a metros en x, y y z
MY=np.array(mars[:,2]*AU)
MZ=np.array(mars[:,3]*AU)
Mr=np.array(np.sqrt((MX**2)+(MY**2)+(MZ**2)))   # Lista de distancias hasta el sol en cada posición


plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(EX, EY, EZ,'black',label='Earth')
ax.plot3D(MX, MY, MZ,'blue',label='Mars')
plt.title('ORBITS')
plt.xlabel('X(m)')
plt.ylabel('Y(m)')
plt.legend()
plt.savefig('Orbitas.pdf')
plt.close()

def derivada(x,t):
    
    D=np.zeros(len(x))
    
    for i in range(len(t)):
        if(i==len(t)-1):
            D[i]=(x[-1]-x[-2])/(t[-1]-t[-2])
        else:
            D[i]=(x[i+1]-x[i])/(t[i+1]-t[i])
            
    return D
    

def velocidad(x,t):
    velocidad = derivada(x,t)
    return velocidad

def aceleracion(x,y,z,t):
    
    ax=derivada(velocidad(x,t),t)
    ay=derivada(velocidad(y,t),t)
    az=derivada(velocidad(z,t),t)
    
    lista_aceleraciones = np.sqrt((ax**2)+(ay**2)+(az**2))
        
    return np.array(lista_aceleraciones)

Ea = aceleracion(EX,EY,EZ,Et)
Ma = aceleracion(MX,MY,MZ,Mt)

def masaSol(a,r):
    
    m = (a*(r**2))/G                        # Fórmula obtenida después de igualar la ecuación de la fuerza gravitacional con F = m*a
    
    masa=np.mean(m)
    
    return masa

E_mSol=masaSol(Ea,Er)
M_mSol=masaSol(Ma,Mr)
    

print('La masa estimada del Sol obtenida a partir de las posiciones de la Tierra es', E_mSol,' kg y la obtenida a partir de las posiciones de Marte es', M_mSol,' kg')