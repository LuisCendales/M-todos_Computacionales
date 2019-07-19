#######################################################    De la clase S3C1 #############################################################################
import numpy as np
import matplotlib.pylab as plt


# Escriba aca su funcion GENERAL de eliminacion Gaussiana para resolver el sistema Ax=B.

def GJ(A,B):
    NA=len(A)
    for c in range(NA):
        for r in range(NA):
            if(r==c):
                B[r]=B[r]/A[r,c]
                A[r,:]=A[r,:]/A[r,c]
            if(r>c):
                B[r]=B[r]-(B[c]*A[r,c])
                A[r,:]=A[r,:]-(A[c,:]*A[r,c])
            
    for c in range(NA):
        for r in range(NA):
            if(r<c):
                B[r]=B[r]-(B[c]*A[r,c])
                A[r,:]=A[r,:]-(A[c,:]*A[r,c])
    return B



########################################################################################################################################################
#######################################################   S3C2 minimos cuadrados     ###################################################################
########################################################################################################################################################
# Ejercicio: Minimos cuadrados (https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/secciones/05.SistemasEcuaciones/lin_algebra.pdf)


# Almacene los datos de parabolico.dat
datos=np.genfromtxt('parabolico.dat')

# Grafique los datos. Guarde la grafica sin mostrarla en plotdatos.pdf 
plt.figure()
plt.scatter(datos[:,0],datos[:,1],s=3,label='Datos')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Datos')
plt.legend()
plt.grid()
plt.savefig('plotdatos.pdf')
plt.close()
 
# teniendo en cuenta que el modelo que usted queiere ajustar a los datos es de la forma: xt=m1+m2*t+m3*0.5*t*t+ruido
# use los datos t y xt, implemente un esquema de minimos cuadrados para encontrar los mejores valores de los parametros m1, m2, m3. (ver explicación en el tablero)
t=datos[:,0]
xt=datos[:,1]
unos=np.ones(len(t))

AT=np.matrix([unos,t,(t**2)/2])   # La matriz creada de por sí es la Matriz transpuesta
A=AT.transpose()                # Se transpone la transpuesta para crear la matriz normal de tamaño N x 3
B=np.copy(xt)    

Anew=np.dot(AT,A)
Bnew=np.dot(AT,B)
Bnew=Bnew.transpose()           #se voltea para que quede una matriz 3x1 y pueda entrar en la eliminación gaussiana


Bsol=GJ(Anew,Bnew)

sol=np.dot(A,Bsol)
 
# Grafique los datos y el ajuste con los parametros obtenidos. Guarde la grafica sin mostrarla en plotAjustedatos.pdf 

plt.figure()
plt.scatter(datos[:,0],datos[:,1],s=3,c='b',label='Datos')
plt.plot(t,sol,c='r',label='Función')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Función Ajustada')
plt.legend()
plt.grid()
plt.savefig('plotAjustados.pdf')
plt.close()
########################################################################################################################################################
#######################################################   S3C3 Preparacion PCA       ###################################################################
########################################################################################################################################################
## Ejercicio casa:
# Los arrays `u` y `v` representan dos series en funcion del tiempo `t`.
# 1) Grafique las dos series de datos en una misma imagen y guarde dicha grafica sn mostrarla en 'serie.pdf'
# 2) Calcule la covarianza entre `u` y `v` e imprima su valor.
# 3) Calcule la varianza de `u` e imprima su valor.
# 4) Imprima un mensaje donde explique que puede inferir del valor de covarianza obtenido.
import numpy as np
t = np.array([0.,0.1,0.2,0.3,0.4,0.5,0.6, 0.8, 0.9])
u = np.array([-12.,-45.,-6.,-78.,-34.,-22.,10.,-31.,27.])
v = np.array([3.,11.,1.3,37.,11.,6.,-23.,7.,7.])

# si alcanzan:
# 5) Calcule la matriz de covarianza de los datos anteriores.
# Lectura preparatorias de PCA: https://github.com/ComputoCienciasUniandes/MetodosComputacionales/blob/master/secciones/05.SistemasEcuaciones/lin_algebra.pdf
# https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c

