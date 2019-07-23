import numpy as np
import matplotlib.pylab as plt

datos=np.genfromtxt("canal_ionico.txt",delimiter='\t')
x=datos[:,0]
y=datos[:,1]

theta=np.linspace(0,2*np.pi,1000)


def x(r,xi):
    return r*np.cos(theta)+xi

def y(r,yi):
    return r*np.cos(theta)+yi

def L(xobs,xmed):
    chicuad=np.sum((xobs-xmed)**2)
    return np.exp(-0.5*chicuad)

def bayes(N,sigma):
    rdat=np.zeros(N)
    xdat=np.zeros(N)
    ydat=np.zeros(N)
    lx=np.zeros(N)
    ly=np.zeros(N)
    
    rdat[0]=np.random.random()
    xdat[0]=np.random.random()
    ydat[0]=np.random.random()
    
    xi=x(rdat[0],xdat[0])
    yi=y(rdat[0],ydat[0])
    
    lx[0]=L(xdat,xi)
    ly[0]=L(ydat,yi)
    
    for i in range(N):
        rold=rdat[i-1]
        xold=xdat[i-1]
        yold=ydat[i-1]
        
        rnew=np.random.normal(rold,sigma)
        xnew=np.random.normal(xold,sigma)
        ynew=np.random.normal(yold,sigma)
        
        xiold=x(rold,xold)
        yiold=y(rold,yold)
        lxold=L(xdat,xiold)
        lyold=L(ydat,yiold)
        
        xnew=x(rnew,xnew)
        ynew=y(rnew,ynew)
        lxnew=L(xdat,xnew)
        lynew=L(ydat,ynew)
        
        alphax=lxnew/lxold
        alphay=lynew/lyold
        
        if(alphax>1):
            rdat[i]=rnew
            xdat[i]=xnew
            lx[i]=lxnew
        else:
            betax=np.random.random()
            if(betax<alphax):
                rdat[i]=rnew
                xdat[i]=xnew
                lx[i]=lxnew
            else:
                rdat[i]=rold
                xdat[i]=xold
                lx[i]=lxold
       
        if(alphay>1):
            rdat[i]=rnew
            ydat[i]=ynew
            ly[i]=lynew
        else:
            betay=np.random.random()
            if(betay<alphay):
                rdat[i]=rnew
                ydat[i]=ynew
                ly[i]=lynew
            else:
                rdat[i]=rold
                ydat[i]=yold
                ly[i]=lyold
        
    mx=np.argmax(lx)
    my=np.argmax(ly)
        
    return xdat[mx],ydat[mx]

xbest,ybest=bayes(1000,0.1)
    
    
plt.figure()
plt.scatter(x,y,s=10)
plt.scatter(xbest,ybest,c='r')
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("Canal.png")
plt.close()