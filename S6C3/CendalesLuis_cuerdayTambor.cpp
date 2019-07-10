#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

const double c = 300.0;

int main(){
    double L = 1.0, x0 = 0, dx = 0.005;        // Inicialización
    int n = (L-x0)/dx + 1;
    
    double xlista[n];
    for(int i=0;i<n;i++){
        xlista[i]=x0;
        x0+=dx;
    }
    
    double tfin = 0.1, t0 = 0., dt= 0.00001;    // r (linea 40) debe ser menor a 1
    int nt = (tfin-t0)/dt +1;
    double A0=0.01;
    double pendiente=A0/(L/2);
    
    double phi_pasado[n];
    double phi_presente[n];
    double phi_futuro[n];
    ofstream cuerda1;
    ofstream outfile2;
    ofstream outfile3;
    
    cuerda1.open("datos1.dat");
    
    for(int i=0;i<n;i++){                      // Estado inicial de la cuerda
        if(i<(n/2)){
            phi_pasado[i]=xlista[i]*pendiente;
        } else{
            phi_pasado[i]=xlista[i]*(-pendiente)+2*A0;
        }
    }
    
    
    double r = (c*c*dt*dt)/(dx*dx);
    
    for(int i=0;i<n;i++){                     // Primer paso
        
        phi_presente[i]=phi_pasado[i] + ((r/2)*(phi_pasado[i+1]+phi_pasado[i-1]-2*phi_pasado[i]));
    }   
    
    for(int i=0;i<n;i++){
        cuerda1<<xlista[i]<<" ";
    }
    cuerda1<<"\n";
    
    for(int i=0;i<n;i++){
        cuerda1<<phi_presente[i]<<" ";
    }
    cuerda1<<"\n";
    
    for(int j=0;j<nt;j++){                     // Ciclo para siguientes tiempos
        for(int i=0;i<n;i++){
            phi_futuro[i] = phi_presente[i]*2 - phi_pasado[i] + r*(phi_presente[i+1]+phi_presente[i-1]-2*phi_presente[i]);
        }
        for(int x=0;x<n;x++){
           phi_pasado[x]=phi_presente[x];
        }
        for(int x=0;x<n;x++){
           phi_presente[x]=phi_futuro[x];
        }
        
        if(j%1000==0 and j>999){
            for(int y=0;y<n;y++){
                cuerda1<<phi_presente[y]<<" ";
            }
            cuerda1<<"\n";
        }
    }
    cuerda1.close();
    return 0;
}