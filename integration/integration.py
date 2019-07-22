#########################################################################################
################### preparacion S2C1 integracion numerica ###############################
#########################################################################################

#Este ejercicio preparatorio busca que usted implemente correctamente tres metodos de integracion numerica. Haga este ejercicio despues de haber leido y entendido los algoritmos correspondientes a los distintos metodos. Si quiere complementar este ejercicio, puede repetir el proceso para el metodo de Monte Carlo y el metodo del valor medio.

# Ejercicio: Integrales

import numpy as np
import matplotlib.pylab as plt

# Funcion a integrar
def funcion(x1):
	return np.cos(x1)


#El intervalo de integracion es de 0 a 3pi/2. Divida el intervalo de integracion en M secciones para calcular sus integrales.
a = 0
b = 3*np.pi/2
M = 100

def Ianalítica(a,b):
    return np.sin(b)-np.sin(a)

# 1a). Usando el metodo de suma de rectangulos, calcule la integral de la funcion. Compare su valor obtenido numericamente con el valor analitico e imprima ambos valores
'''
def rectangulos(a,b,M):
    h = (b-a)/M
    w=h
    suma=0
    x=a
    for i in range(int(M)):
        suma+=funcion(x)*w
        x+=h
    return suma
'''
def rectangulos(a,b,M):
    h=(b-a)/(M-1)
    w=h
    x=np.linspace(a,b,M)
    f=funcion(x)
    return np.sum(f*w)

print('Integral analítica es: ',Ianalítica(a,b))
print('Integral por suma de rectángulos da: ',rectangulos(a,b,M))


# 1b). Usando el metodo de trapezoide, calcule la integral de la funcion. Compare su valor obtenido numericamente con el valor analitico e imprima ambos valores.
'''
def trapezoide(a,b,M):
    h=(b-a)/(M-1)
    x=a
    suma=0
    for i in range(int(M)):
        if (i==0 or i==M-1):
            w=h/2
        else:
            w=h
        suma+=funcion(x)*w
        x+=h
    return suma
'''

def trapezoide(a,b,M):
    h=(b-a)/(M-1)
    x=np.linspace(a,b,M)
    w=np.zeros(M)
    for i in range(M):
        if(i==0 or i==M-1):
            w[i]=h/2
        else:
            w[i]=h
    f=funcion(x)
    return np.sum(f*w)
print('Integral por el método de trapezoide da: ',trapezoide(a,b,M))

# 1c). Usando el metodo de Simpson, calcule la integral de la funcion. Compare su valor obtenido numericamente con el valor analitico e imprima ambos valores.
'''
def simpson(a,b,M):
    if(M%2==0):
        M=M-1
    h=(b-a)/(M-1)
    x=a
    suma=0
    for i in range(int(M)):
        if (i==0 or i==M-1):
            w=h/3
        elif(i%2==1):
            w=4*h/3
        else:
            w=2*h/3
        suma+=funcion(x)*w
        x+=h
    return suma
'''
def simpson(a,b,M):
    if(M%2==0):
        M=M-1
    h=(b-a)/(M-1)
    x=np.linspace(a,b,M)
    w=np.zeros(M)
    for i in range(int(M)):
        if (i==0 or i==M-1):
            w[i]=h/3
        elif(i%2!=0):
            w[i]=(4/3)*h
        else:
            w[i]=(2/3)*h
    f=funcion(x)
    return np.sum(f*w)
print('Integral por el método de Simpson da: ',simpson(a,b,M))

#########################################################################################
################### S2C1 errores para diferentes metodos  ###############################
#########################################################################################
print('')
print('ERRORES DE MÉTODOS')
print('')
# 1d). Repita el procedimiento para distintios valores de M (10**2 a 10**7 aumentando logaritmicamente, use np.logspace: https://docs.scipy.org/doc/numpy/reference/generated/numpy.logspace.html) para calcular la integral y haga una grafica de error ((valor numerico - valor analitico)/valor analitico) en funcion de M (haga una curva por cada metodo). Guarde dicha grafica sin mostrarla en ErrorRTS.pdf

xlog=np.logspace(2,7,6)
logrectangulos=[]
logtrapezoide=[]
logsimpson=[]
for i in range(len(xlog)):
    logrectangulos.append(rectangulos(a,b,int(xlog[i])))
    logtrapezoide.append(trapezoide(a,b,int(xlog[i])))
    logsimpson.append(simpson(a,b,int(xlog[i])))

ER=np.abs((logrectangulos-Ianalítica(a,b))/Ianalítica(a,b))
ET=np.abs((logtrapezoide-Ianalítica(a,b))/Ianalítica(a,b))
ES=np.abs((logsimpson-Ianalítica(a,b))/Ianalítica(a,b))

plt.figure()
plt.plot(xlog,ER,c='b',label='Error Rectángulos')
plt.plot(xlog,ET,c='g',label='Error Trapezoide')
plt.plot(xlog,ES,c='r',label='Error Simpson')
plt.title('Error de métodos')
plt.xlabel('X')
plt.ylabel('abs(error)')
plt.loglog()
plt.legend()
plt.savefig('ErrorRTS.png')
#########################################################################################
################### S2C1 otros metodos de integracion numerica ##########################
#########################################################################################

# 1e). Usando el metodo de valor medio, calcule la integral de la funcion cos(theta) entre 0 y pi/2 usando N=10000 puntos aleatorios. Compare su valor obtenido numericamente con el valor analitico e imprima ambos valores.
def VM(a,b,N):
    x=np.cos((np.random.random(N)*(b-a))+a)
    suma=np.sum(x)
    I=(suma*(b-a))/N
    return I
print('La integral por valor medio da: ',VM(0,np.pi/2,10000))
print('La integral analítica da: ',Ianalítica(0,np.pi/2))

# 1f). Usando el metodo de sampleo directo de Monte Carlo, calcule la integral de la funcion sin(theta) entre 0 y pi/2 usando N=10000 puntos aleatorios. Compare su valor obtenido numericamente con el valor analitico e imprima ambos valores.

# 1g). Repita el procedimiento para distintios valores de M (10**2 a 10**7 aumentando logaritmicamente) para calcular la integral y haga una grafica de error ((valor numerico - valor analitico)/valor analitico) en funcion de M (haga una curva por cada metodo). Guarde dicha grafica sin mostrarla en ErrorRTS.pdf
