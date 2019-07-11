#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(){
    double x = 1., y = 1., dx=0.01, dy=0.01;          //Inicialización de datos
    int nx = x/dx+1;
    int ny = y/dy+1;
    double dt = 0.1, tfinal = 2500;
    int nt= tfinal/dt+1;
    double v=0.0001;
    
    double T[ny][nx];
    ofstream outfile;
    ofstream t100;
    ofstream t2500;
    
    for(int j=0;j<ny;j++){                           //inicializo placa
        for(int i=0;i<nx;i++){
            T[j][i]=50;
            if(j>40 and j<60){
                if(i>20 and i<40){
                    T[j][i]=100;
                }
            }
        }
    }
    
    outfile.open("PlacaIni.dat");
    for(int j=0;j<ny;j++){
        for(int i=0;i<nx;i++){
            outfile<<T[j][i]<<" ";
        }
        outfile<<"\n";
    }
    outfile.close();
    
    double r = (v*dt)/(dx*dx);
    
    for(int t=0;t<nt;t++){
        for(int j=1;j<ny-1; j++){
            for(int i=1;i<nx-1;i++){
                T[j][i]=r*(T[j+1][i]+T[j-1][i]-2*T[j][i] + T[j][i+1]+T[j][i-1]-2*T[j][i]) + T[j][i];
            }
        }
        if(t*dt==100){
            t100.open("t100.dat");
            for(int j=0;j<ny;j++){
                for(int i=0;i<nx;i++){
                    t100<<T[j][i]<<" ";
                }
                t100<<"\n";
            }
            t100.close();
        }
        if(t*dt==2500){
            t2500.open("t2500.dat");
            for(int j=0;j<ny;j++){
                for(int i=0;i<nx;i++){
                    t2500<<T[j][i]<<" ";
                }
                t2500<<"\n";
            }
            t2500.close();
        }
    }
    return 0;
}