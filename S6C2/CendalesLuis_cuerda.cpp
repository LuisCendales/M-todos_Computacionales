#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

const double c = 300;

int main(){
    double L = 1.0;
    double x0 = 0;
    double dx = 0.05;    
    double n;
    n=(L-x0)/dx;
    
    double xlista[n];
    for(int i=0;i<n;i++){
        xlista[i]=x0;
        x0+=dx;
    }
    
    double tfin = 0.1;
    double A0=0.01;
    double alpha=tan(A0/(L/2));
    
    double phi[n];
    ofstream outfile;
    
    for(int i=0;i<n;i++){
        if(i<(L/2)){
            phi[i]=xlista[i]/cos(alpha);
        } else{
            phi[i]=-xlista[i]/cos(alpha);
        }
    }
    outfile.open('datos.dat');
    for(int i=0;i<n;i++){
        outfile<<xlista[i]<<" "<<phi[i]<<endl;
    }
    
    outfile.close()
    
    return 0;
}