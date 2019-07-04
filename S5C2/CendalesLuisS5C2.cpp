#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

double ecuacion(double x, double y);

int main(){
//     Euler
    double min=0.;
    double max =4.;
    double h=0.001;
    int n;
    ofstream outfile1;
    ofstream outfile2;
    
    n=(max-min)/h;
    
    double x1 = 0.;
    double y1 = 1.;
    
    outfile1.open("euler.dat");
    for(int i=0;i<n;i++){
        outfile1<<x1<<" "<<y1<<endl;
        y1=y1+(h*ecuacion(x1,y1));
        x1=x1+h;
    }
    outfile1.close();
    
//     RK4
    
    double x2 = 0.;
    double y2 = 1.;
    double k1;
    double k2;
    double k3;
    double k4;
    double kprom;
        
    
    outfile2.open("RK4.dat");
    for(int i=0;i<n;i++){
        k1 = h*ecuacion(x2, y2);
        k2 = h*ecuacion(x2+0.5*h, y2+0.5*k1);
        k3 = h*ecuacion(x2+0.5*h, y2+0.5*k2);
        k4 = h*ecuacion(x2+h, y2+k3);
        
        kprom=(k1+(2*k2)+(2*k3)+k4)/6;
        outfile2<<x2<<" "<<y2<<endl;
        x2=x2+h;
        y2=y2+kprom;        
        
    }
    
    outfile2.close();
    
    return 0;
}

double ecuacion(double x, double y){
    return -y;
}
