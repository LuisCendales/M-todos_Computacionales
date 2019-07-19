################################################################## clase ######################################################################################
# Ejercicio 1:

import numpy as np
from numpy.linalg import inv
from numpy.linalg import solve
# 1a.) Tiene un sistema de 3 ecuaciones lineales Ax=B, donde:

A=np.matrix([[8.,2.,1.],[1.,-2.,-3.],[-1.,1.,2,]])
print(A)

B=np.array([-8.,0.,3.])


# Implemente el algoritmo de eliminacion gaussiana para resolver este sistema de ecuaciones. IMPRIMA la matriz aumentada paso a paso. IMPRIMA su vector solucion
def GJ(A,B):
    NA=len(A)
    paso=0
    for c in range(NA):
        for r in range(NA):
            if(r==c):
                B[r]=B[r]/A[r,c]
                A[r,:]=A[r,:]/A[r,c]
                paso+=1
                print('Paso',paso)
                print(A)
            if(r>c):
                B[r]=B[r]-(B[c]*A[r,c])
                A[r,:]=A[r,:]-(A[c,:]*A[r,c])
                paso+=1
                print('Paso',paso)
                print(A)
            
    for c in range(NA):
        for r in range(NA):
            if(r<c):
                B[r]=B[r]-(B[c]*A[r,c])
                A[r,:]=A[r,:]-(A[c,:]*A[r,c])
                paso+=1
                print('Paso',paso)
                print(A)
    print('El vector solución es:',B)
    
GJ(A,B)
            


# IMPRIMA la solucion encontrada usando los paquetes de numpy
print('Usando los paquetes de numpy la solución da:',solve(A,B))


# 1b). Repita lo anterior para un sistema de ecuaciones mas general: Imprimiendo los pasos intermedios.
#Escriba aca un codigo GENERAL de eliminacion Gaussiana para resolver el sistema Ax=B.

print('')
print('PUNTO 1B')
print('')

N=np.random.randint(3 , 8)
print ('Matriz de tamaño:',N,'x',N)
Arreglo=(np.random.random((N,N))*10.0)-5.0
B=(np.random.random((N,1))*10.0)-5.0

print ('Matriz A =')
print (Arreglo)
print ('B =')
print (B)
print('')
print('Solución')
GJ(Arreglo,B)

# IMPRIMA la solucion encontrada usando los paquetes de numpy 

print('Usando los paquetes de numpy la solución da:',solve(Arreglo,B))



 










