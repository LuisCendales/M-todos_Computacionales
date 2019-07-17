# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt


# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion. 
def mifun(x):
    x_0 = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_0)**2 + a**2)

# Dentro de una funcion que reciba como parametros el numero de pasos y el sigma de la distribucion gausiana que va a usar para calcular el paso de su caminata, implemente el algortimo de Metropolis-Hastings. Finalmente, haga un histograma de los datos obtenidos y grafique en la misma grafica, la funcion de distribucion de probabilidad fx (Ojo, aca debe normalizar). Guarde la grafica sin mostrarla en un pdf. Use plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf"), donde sigma y pasos son los parametros que recibe la funcion. 


def metropolis(x,f,N,sigma):
    datos=np.zeros(N)
    datos[0]=np.random.random()*max(x)
    for i in range(1,N):
        xold=datos[i-1]
        xnew=np.random.normal(xold,sigma)
        alpha=f(xnew)/f(xold)
        if(alpha>1):
            datos[i]=xnew
        else:
            beta=np.random.random()
            if(beta<alpha):
                datos[i]=xnew
            else:
                datos[i]=xold
    return datos

# Cuando haya verificado que su codigo funciona, use los siguientes parametros:
# sigma = 5, pasos =100000 
# sigma = 0.2, pasos =100000 
# sigma = 0.01, pasos =100000 
# sigma = 0.1, pasos =1000 
# sigma = 0.1, pasos =100000 
# este puede ser muy demorado dependiendo del computador: sigma = 0.1, pasos =500000
sigma=[5,0.2,0.01,0.1,0.1,0.1]
pasos=[100000,100000,100000,1000,100000,500000]


# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.

x=np.linspace(-4,4,1000)
y=mifun(x)

for i in range(len(pasos)):
    s=sigma[i]
    N=pasos[i]
    MH=metropolis(x,mifun,N,s)
    
    plt.figure()
    plt.hist(MH,bins=100,density=True,label="MH")
    plt.plot(x,y,label="Función")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title('Metropolis con $\sigma$ ='+str(s)+' y '+str(N)+ ' pasos.')
    plt.savefig("histograma_"+str(s)+"_"+str(N)+".png")
    plt.close()


