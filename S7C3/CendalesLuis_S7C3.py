#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt


# 1) lea los datos de resorte.dat y almacenelos.
# 
spring=np.genfromtxt("resorte.dat")

# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por 
# xt=a*np.exp(-gamma*t)*np.cos(omega*t)
# Donde a, gamma, y omega son parametros.
tdata=spring[:,0]
xdata=spring[:,1]


# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:

# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne el modelo  


def x(t,a,gamma,omega):
    return a*np.exp(-gamma*t)*np.cos(omega*t)


# 2b.) Definir una funcion que retorne la funcion de verosimilitud

def L(xobs,xmed):
    chicuad=np.sum((xobs-xmed)**2)
    like=np.exp(-0.5*chicuad)
    return like


# 2c.) Caminata
#condiciones iniciales
aini=7.5
gammaini=0.6
omegaini=18.2


def bayes(N,sigma):
    a=np.zeros(N)
    g=np.zeros(N)
    o=np.zeros(N)
    l=np.zeros(N)
    
    a[0]=7.5
    g[0]=0.6
    o[0]=18.2
    
    xi=x(tdata[0],a[0],g[0],o[0])
    l[0]=L(xdata[0],xi)
    
    for i in range(1,N):
        aold=a[i-1]
        gold=o[i-1]
        oold=g[i-1]
        
        anew=np.random.normal(aold,sigma)
        gnew=np.random.normal(oold,sigma)
        onew=np.random.normal(gold,sigma)
        
        xold=x(tdata,aold,gold,oold)
        lold=L(xdata,xold)
        
        xnew=x(tdata,anew,gnew,onew) 
        lnew=L(xdata,xnew)
        
        alpha=lnew/lold
        
        if(alpha>1):
            a[i]=anew
            g[i]=gnew
            o[i]=onew
            l[i]=lnew
        else:
            beta=np.random.random()
            if(beta<=alpha):
                a[i]=anew
                g[i]=gnew
                o[i]=onew
                l[i]=lnew
            else:
                a[i]=aold
                g[i]=gold
                o[i]=oold
                l[i]=lold
    
    mx=np.argmax(l)                
    return a[mx],g[mx],o[mx],l[mx]


#numero de pasos
iteraciones=100000

a,g,o,l=bayes(iteraciones,0.1)

# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."
print("Los mejores parametros son a= "+str(a)+" gamma= "+str(g)+" y omega= "+str(o))

# 2f.) Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.pdf
xbest=x(tdata,a,g,o)

plt.figure()
plt.scatter(tdata,xdata,s=10,c='r',label="datos")
plt.plot(tdata,xbest,c='b',label="Modelo")
plt.title('Modelo Estimación Bayesiana - Resorte')
plt.xlabel('$t$')
plt.ylabel('$Posición$')
plt.legend()
plt.grid()
plt.savefig("Resorte.png")
plt.close()

# 3) SABIENDO QUE omega=np.sqrt(k/m), IMPRIMA UN MENSAJE DONDE EXPLIQUE SI PUEDE O NO DETERMINAR k Y m DE MANERA INDIVIDUAL USANDO EL METODO ANTERIOR. JUSTIFIQUE BIEN SU RESPUESTA (PUEDE ADEMAS HACER PRUEBAS CON EL CODIGO PARA RESPONDER ESTA PREGUNTA).



