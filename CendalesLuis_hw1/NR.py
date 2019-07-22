import numpy as np
import matplotlib.pylab as plt

def funcion(x):
    return x**5 - 2*(x**4) - 10*(x**3) + 20*(x**2) + 9*x - 18

xx=np.linspace(-3.5,3.5,100)

plt.figure()
plt.plot(xx,funcion(xx))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Gráfica de la función')
plt.grid()
plt.savefig('NRpoli.pdf')
plt.close()

def NR(x,funcion,precision=1*(10**-5)):
    N=0
    dx=3**-1
    for i in range(10000):
        F=funcion(x)
        if(abs(F)<precision):
            break
        df= (funcion(x+(dx/2))-funcion(x-(dx/2)))/dx
        dx=-F/df
        x+=dx
        N+=1
    return x,N

# x_guess = -3
print('')

xmenos3,Nmenos3=NR(-3,funcion)

print('Con un x_guess inicial de -3 el valor de la raíz X0r da: ',xmenos3,'y el valor de f(X0r) da: ',funcion(xmenos3))

# x_guess = -1
print('')

xmenos1,Nmenos1=NR(-1,funcion)

print('Con un x_guess inicial de -1 el valor de la raíz X1r da: ',xmenos1,'y el valor de f(X1r) da: ',funcion(xmenos1))


# Número de iteraciones

xx2=np.linspace(-4,4,1000)
Ns=np.zeros(len(xx2))
raices=np.zeros(len(xx2))

for i in range(len(xx2)):
    raiz,N=NR(xx2[i],funcion,precision=1*(10**-10))
    Ns[i]=N
    raices[i]=raiz
    
plt.figure()
plt.scatter(xx2,Ns,s=15)
plt.xlabel('X_guess')
plt.ylabel('No. Iteraciones')
plt.title('Número de iteraciones')
plt.grid()
plt.savefig('NR_itera.pdf')
plt.close()

plt.figure()
plt.scatter(xx2,raices,s=15)
plt.xlabel('X_guess')
plt.ylabel('Raíz')
plt.title('Raíces encontradas')
plt.grid()
plt.savefig('NRxguess.pdf')
plt.close()

print('')
print('Se puede observar claramente que los puntos de X_guess en los que el método necesita una mayor cantidad de iteraciones (Gráfica NR_itera.pdf) está correlacionado con las partes de la función (Gráfica NRpoli.pdf) en las que su derivada es cercana a cero. Esto se debe a que el método busca puntos en el eje x que se crucen con la pendiente de la funcion de x0, lo que significa que esos nuevos puntos de x serán muy lejanos del x0 y el método necesitará mucho más tiempo para encontrar una raíz en la que la función de 0.')
print('')
print('Además, se puede observar que también hay una correlación con los tramos de X_guess (Gráfica NRxguess.pdf) en los que la raiz encontrada es variable. Esto se da por la misma razón de que la distancia entre nuevos puntos de x y el x anterior es muy grande y los ceros encontrados son de una parte lejana de la función.')
