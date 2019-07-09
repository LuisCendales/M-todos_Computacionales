#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

const double c = 300.0;

int main(){
    double L = 1.0, x0 = 0, dx = 0.005;   
    int n = (L-x0)/dx + 1;
    
    double xlista[n];
    for(int i=0;i<n;i++){
        xlista[i]=x0;
        x0+=dx;
    }
    
    double tfin = 0.1, t0 = 0., dt= 0.005;
    double A0=0.01;
    double pendiente=A0/(L/2);
    
    double phi_pasado[n];
    double phi_presente[n];
    double phi_futuro[n];
    ofstream outfile1;
    ofstream outfile2;
    ofstream outfile3;
    
    for(int i=0;i<n;i++){
        if(i<(n/2)){
            phi_pasado[i]=xlista[i]*pendiente;
        } else{
            phi_pasado[i]=xlista[i]*(-pendiente)+2*A0;
        }
    }
        
    
//     Se supone que hasta acá todo está bien
    double r = pow(c*dt/dx,2);
    for(int i=0;i<n;i++){
        phi_presente[i]=phi_pasado[i] + ((r/2)*(phi_pasado[i+1]+phi_pasado[i-1]-2*phi_pasado[i]));
    }
    
    
    outfile1.open("datos1.dat");
    for(int i=0;i<n;i++){
        outfile1<<xlista[i]<<" "<<phi_pasado[i]<<" "<<phi_presente[i]<<"\n";
    }
    
    outfile1.close();
    
//     for(int i=0;i<n;i++){
    
//     }
    return 0;
}