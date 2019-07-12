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
    
    double T1[ny][nx];
    double T2[ny][nx];
    double T3[ny][nx];
    ofstream t1a;
    ofstream t1b;
    ofstream t1c;
    
    ofstream t2b;
    ofstream t2c;
    
    ofstream t3b;
    ofstream t3c;
    
    for(int j=0;j<ny;j++){                           //inicializo placa
        for(int i=0;i<nx;i++){
            T1[j][i]=50;
            T2[j][i]=50;
            T3[j][i]=50;
            if(j>40 and j<60){
                if(i>20 and i<40){
                    T1[j][i]=100;
                    T2[j][i]=100;
                    T3[j][i]=100;
                }
            }
        }
    }
    
    t1a.open("PlacaIni.dat");
    for(int j=0;j<ny;j++){
        for(int i=0;i<nx;i++){
            t1a<<T1[j][i]<<" ";
        }
        t1a<<"\n";
    }
    t1a.close();
    
    double rx = (v*dt)/(dx*dx);
    double ry = (v*dt)/(dy*dy);
    
    for(int t=0;t<nt;t++){
        for(int j=1;j<ny-1; j++){
            for(int i=1;i<nx-1;i++){
                T1[j][i]=rx*(T1[j+1][i]+T1[j-1][i]-2*T1[j][i]) + ry*(T1[j][i+1]+T1[j][i-1]-2*T1[j][i]) + T1[j][i];
            }
        }
        if(t*dt==100){
            t1b.open("t1b.dat");
            for(int j=0;j<ny;j++){
                for(int i=0;i<nx;i++){
                    t1b<<T1[j][i]<<" ";
                }
                t1b<<"\n";
            }
            t1b.close();
        }
        if(t*dt==2500){
            t1c.open("t1c.dat");
            for(int j=0;j<ny;j++){
                for(int i=0;i<nx;i++){
                    t1c<<T1[j][i]<<" ";
                }
                t1c<<"\n";
            }
            t1c.close();
        }
    }
    
    for(int t=0;t<nt;t++){                            //abiertas
        for(int j=0;j<ny; j++){
            for(int i=0;i<nx;i++){
                if(j>0 and j<(ny-1)){
                    if(i>0 and i<(nx-1)){
                        T2[j][i]=rx*(T2[j+1][i]+T2[j-1][i]-2*T2[j][i]) + ry*(T2[j][i+1]+T2[j][i-1]-2*T2[j][i]) + T2[j][i];
                    }
                }
                if(j==0){
                    T2[j][i]=T2[j+1][i];
                }
                if(i==0){
                    T2[j][i]=T2[j][i+1];
                }
                if(j==ny-1){
                    T2[j][i]=T2[j-1][i];
                }
                if(i==nx-1){
                    T2[j][i]=T2[j][i-1];
                }
            }
        }
        if(t*dt==100){
            t2b.open("t2b.dat");
            for(int j=0;j<ny;j++){
                for(int i=0;i<nx;i++){
                    t2b<<T2[j][i]<<" ";
                }
                t2b<<"\n";
            }
            t2b.close();
        }
        if(t*dt==2500){
            t2c.open("t2c.dat");
            for(int j=0;j<ny;j++){
                for(int i=0;i<nx;i++){
                    t2c<<T2[j][i]<<" ";
                }
                t2c<<"\n";
            }
            t2c.close();
        }
    }
    
    for(int t=0;t<nt;t++){                            //Periodicas
        for(int j=0;j<ny; j++){
            for(int i=0;i<nx;i++){
                if(j>0 and j<(ny-1)){
                    if(i>0 and i<(nx-1)){
                        T3[j][i]=rx*(T3[j+1][i]+T3[j-1][i]-2*T3[j][i]) + ry*(T3[j][i+1]+T3[j][i-1]-2*T3[j][i]) + T3[j][i];
                    }
                }
                if(j==0){
                    T3[j][i]=T3[ny-2][i];
                }
                if(i==0){
                    T3[j][i]=T3[j][nx-1];
                }
                if(j==ny-1){
                    T3[j][i]=T3[1][i];
                }
                if(i==nx-1){
                    T3[j][i]=T3[j][1];
                }
            }
        }
        if(t*dt==100){
            t3b.open("t3b.dat");
            for(int j=0;j<ny;j++){
                for(int i=0;i<nx;i++){
                    t3b<<T3[j][i]<<" ";
                }
                t3b<<"\n";
            }
            t3b.close();
        }
        if(t*dt==2500){
            t3c.open("t3c.dat");
            for(int j=0;j<ny;j++){
                for(int i=0;i<nx;i++){
                    t3c<<T3[j][i]<<" ";
                }
                t3c<<"\n";
            }
            t3c.close();
        }
    }
    
    
    
    return 0;
}