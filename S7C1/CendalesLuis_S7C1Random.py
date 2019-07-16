#Ejercicio 0
#Lean el capitulo 5 del Landau (ver el programa del curso).

import numpy as np
import matplotlib.pylab as plt

#Ejercicio 1
# Usando los generadores de numeros aleatorios de numpy (https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.random.html):
# a) Genere 1000 numeros aleatorios que sigan una distribucion uniforme y esten entre -10 y 10. Haga un histograma y guardelo sin mostrarlo en un archivo llamado uniforme.pdf

uniforme=(np.random.random(1000)*20)-10

plt.figure()
plt.hist(uniforme,bins=50)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Distribución Uniforme")
plt.grid()
plt.savefig("uniforme.png")
plt.close()

# a) Genere 1000 numeros aleatorios que sigan una distribucion gausiana centrada en 17 y de sigma 5. Haga un histograma y guardelo sin mostrarlo en un archivo llamado gausiana.pdf

gaussiana=np.random.normal(17,5.0,1000)

plt.figure()
plt.hist(gaussiana,bins=50)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Distribución Gausiana")
plt.grid()
plt.savefig("gausiana.png")
plt.close()

# Ejercicio 2
# Escriba un programa en Python que: 
# Genere puntos aleatorios distribuidos uniformemente dentro de un cuadrado de lado 30.5. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado cuadrado.pdf.

xcuad=np.random.random(3000)*30
ycuad=np.random.random(3000)*5

plt.figure()
plt.scatter(xcuad,ycuad)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cuadrado 30x5")
plt.grid()
plt.savefig("cuadrado.png")
plt.close()

# Genere puntos aleatorios distribuidos uniformemente dentro de circulo de radio 23. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado circulo.pdf.

xr=(np.random.random(3000)*46)-23
yr=(np.random.random(3000)*46)-23
xcirc=[]
ycirc=[]

for i in range(len(xr)):
    s=np.sqrt((xr[i]**2)+(yr[i]**2))
    if(s<=23):
        xcirc.append(xr[i])
        ycirc.append(yr[i])
        
plt.figure()
plt.scatter(xcirc,ycirc)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Circulo de rad 23")
plt.grid()
plt.savefig("circulo.png")
plt.close()

# Ejercicio 3 
# Lean sobre caminatas aleatorias.


# Ejercicio 4
# Tome los puntos distribuidos aleatoriamente dentro del cuadrado y haga que cada punto siga una caminata aleatoria de 100 pasos. 
# La magnitud de los pasos de esta caminata debe seguir una distribucion gaussiana centrada en el punto y de sigma igual a 0.25
# Implemente condiciones de frontera periodicas: si un punto se "sale" de cuadrado por un lado, "entra" por el otro

def RW(xini,yini,N=100,sigma=0.25):
    x=np.zeros(N)
    y=np.zeros(N)
    x[0]=xini
    y[0]=yini
    
    i=0
    while(i<100):        
        paso=np.random.normal(scale=sigma)
        angulo=np.random.random()*2*np.pi
        
        xpaso=paso*np.cos(angulo)
        ypaso=paso*np.sin(angulo)
        xpaso+=x[i]
        ypaso+=y[i]
        
        if(xpaso<30 and xpaso>0):
            if(ypaso<5 and ypaso>0):
                x[i]=xpaso
                y[i]=ypaso
                
        i+=1
    
    return x,y


    

# Grafique la distribucion final de puntos y guarde dicha grafica sin mostrarla en un archivo llamado DistCaminata.pdf
# Grafique la caminata de UNO de sus puntos y guarde dicha grafica sin mostrarla en un archivo llamado puntoCaminata.pdf

xipunto=xcuad[np.random.randint(len(xcuad))]
yipunto=ycuad[np.random.randint(len(xcuad))]

xpunto,ypunto=RW(xipunto,yipunto)
print(xpunto)
print(ypunto)

plt.figure()
plt.plot(xpunto,ypunto)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Caminata de uno")
plt.grid()
plt.savefig("puntoCaminata.png")
plt.close()

# Repita el proceso para sigma = 0.00025 y sigma= 2.5. Grafique la caminata de UNO de sus puntos para los distintos sigmas y guardela sin mostrarla en sigmaCaminata.pdf

# Repita el proceso para condiciones abiertas: si un punto se "sale" del cuadrado deja de ser considerado en la simulacion.

# Si le queda tiempo puede:

##################################################################################################################################################################
############################################################ Ejercicio  ##########################################################################
##################################################################################################################################################################

#difusion: una gota de crema en un Cafe.
#
#Condiciones iniciales:
#Cafe: 10000 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 230
#Crema: 100 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 2
#
#Nota: si su codigo se esta demorando mucho en correr, puede usar 1000 particulas de cafe en vez de 10000.
#
# 1) Haga una grafica de las condiciones iniciales donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheIni.pdf
#
#2) Todas las particulas deben hacer una caminata aleatoria de 1000 pasos. Los pasos en las coordenadas x y deben seguir una distribucion gausiana de sigma 2.5. Si va a usar coordenadas polares elija un sigma apropiado.
#
#3) Condiciones de frontera: implemente unas condiciones tales que si la particulas "sale" del circulo, usted vuelva a dar el paso. Si no puede implementar solo las condiciones antes descritas, debe al menos escribir comentarios explicando que hace cada linea de codigo de las condiciones propuestas (comentado abajo)
#
# 4) Haga una grafica de las posiciones finales de las particulas despues de la caminata donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheFin.pdf
#

import numpy as np
import matplotlib.pylab as plt


#Una posible implementacion de condiciones de frontera. Trate de hacer la suya propia sin usar esta. 
#Si usa esta (obtiene menos puntos) debe comentar cada una de las lineas explicando en palabras que hace el codigo. Debe tambien naturalmente usar los nombres de variables que uso en el resto de su codigo propio.
#indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>230)
#indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>230)
#while(len(indexcafe[0])>1):
#	xcafenuevo[indexcafe]=xcafe[indexcafe] + np.random.normal(0,sigma)
#	ycafenuevo[indexcafe]=ycafe[indexcafe] + np.random.normal(0,sigma)
#	indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>=230)
#while(len(indexcrema[0])>1):
#	xcremanuevo[indexcrema]=xcrema[indexcrema] + np.random.normal(0,sigma)
#	ycremanuevo[indexcrema]=ycrema[indexcrema] + np.random.normal(0,sigma)
#	indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>=230) 



	
