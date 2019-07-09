#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

const double c = 300;

int main(){
    double L = 1.0;
    double x0 = 0;
    double dx = 0.05;    
    int n;
    n=(L-x0)+1/dx;
    
    double xlista[n];
    for(int i=0;i<n;i++){
        xlista[i]=x0;
        x0+=dx;
    }
    
    double tfin = 0.1;
    double t0 = 0.;
    double dt= 0.01;
    double A0=0.01;
    double pendiente=A0/(L/2);
    
    double phi[n];
    double phi_new[n];
    ofstream outfile;
    
    for(int i=0;i<n;i++){
        if(i<(n/2)){
            phi[i]=xlista[i]*pendiente;
        } else{
            phi[i]=xlista[i]*(-pendiente)+2*A0;
        }
    }
    double phi1[n];
    double r = ((c*c)*(dt*dt))/(dx*dx);
    for(int i=0;i<n;i++){
        if(i=0){
            phi1[i]=(r/2)*(phi[i+1]+phi[i]-2*phi[i]);
        }else if(i=(n-1)){
            phi1[i]=(r/2)*(phi[i]+phi[i-1]-2*phi[i]);
        }else{
            phi1[i]=(r/2)*(phi[i+1]+phi[i-1]-2*phi[i]);
        }
    }    
    
    
    
    
    
    outfile.open("datos.dat");
    for(int i=0;i<n;i++){
        outfile<<xlista[i]<<" "<<phi[i]<<endl;
    }
    
    outfile.close();
    
    return 0;
}