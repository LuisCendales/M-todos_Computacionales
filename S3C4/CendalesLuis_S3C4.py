import numpy as np
import matplotlib.pylab as plt


#1) almacene los datos de WDBC.dat. Los contenidos de cada columna estan descritos en WDBC.doc. En la columna de benigno y maligno se cambio en m y b por 1 y 0 (http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/)

entrada=np.genfromtxt("WDBC.dat",delimiter=',')

datos=entrada[:,2:]
muestras,variables=np.shape(datos)

#2) Usando su propia implementacion, calcule e imprima la matriz de covarianza de sus datos. Revise que su matriz sea correcta comprarando con el resultado de np.cov.

def covarianza(v1,v2):
    N=len(v1)
    cov=(np.sum((v1-np.mean(v1))*(v2-np.mean(v2))))/(N-1)
    return cov

def covmatrix(matriz):                    # Entra matriz con #filas=#muestras y #columnas=#variables
    m,v=np.shape(matriz)
    A=np.zeros((v,v))
    
    for i in range(v):
        for j in range(v):
            A[i,j]=(covarianza(datos[:,i],datos[:,j]))
            
    return A

M=covmatrix(datos)
print('La matriz de covarianza obtenida es:')
print(M)


#3) Usando los paquetes de numpy calcule los autovalores y autovectores de las variables originales.
evalues,evectors=np.linalg.eig(M)
porcentajes=np.zeros(len(evalues))

for i in range(len(evalues)):
    porcentajes[i]=(evalues[i]*100)/np.sum(evalues)

# 4) Organice sus autovalores y autovectores e imprima el autovector con mayor autovalor (puede usar paquetes de numpy para encontrar autovalores y autovectores. lea cuidadosamente la documentacion.)
print('')
for i in range(len(evalues)):
    print('PC',i+1)
    print('Eigenvalue:',evalues[i],'. Percentage:',porcentajes[i],'%')
    print('Corresponding eigenvector:')
    print(evectors[:,i])

# 5) Grafique sus datos en el nuevo sistema de referencia (PC1 PC2), usando colores distintos si el tumor es maligno o beningno.

PC1=np.dot(datos,evectors[:,0])
PC2=np.dot(datos,evectors[:,1])

lista=np.array([entrada[:,1],PC1,PC2])
lista=lista.transpose()
malignos=[]
benignos=[]
for i in range(len(PC1)):
    if(entrada[i,1]==1):
        benignos.append([PC1[i],PC2[i]])
    else:
        malignos.append([PC1[i],PC2[i]])
        
m=np.array(malignos)
b=np.array(benignos)

plt.figure()
plt.scatter(b[:,0],b[:,1],c='b',s=10,label='Benignos')
plt.scatter(m[:,0],m[:,1],c='r',s=10,label='Malignos')
plt.title('PCA')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.grid()
plt.savefig('PCA.png')
plt.close()

# 6) Imprima un mensaje diciendo si usted cree que el metodo de PCA puede ser util para hacer la clasificacion entre tumores malignos y benignos y ayudar al diagnostico para ciertos pacientes, argumentando claramente su posicion.
print('Los datos se pueden observar claramente diferenciados en el diagrama de PCA, por lo que realmente sí es útil a la hora de clasificar tumores malignos y benignos')
#
