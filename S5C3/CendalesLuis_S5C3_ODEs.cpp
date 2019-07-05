#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

double D1(double t,double x,double v);

double D2(double t,double x,double v);

int main(){
    double t = 0.;
    double tfinal = 5.;
    double h = 0.0001;
    double n = (tfinal-t)/h;
    double x = 0.1;
    double v = 0;
    double k11,k12,k21,k22,k31,k32,k41,k42;
    double kprom1;
    double kprom2;
    ofstream outfile;
        
    
    outfile.open("datos.dat");
    for(int i=0;i<n;i++){
        k11 = h*D1(t, x, v);
        k12 = h*D2(t, x, v);
        k21 = h*D1(t+h*0.5, x+0.5*k11, v+0.5*k12);
        k22 = h*D2(t+h*0.5, x+0.5*k11, v+0.5*k12);
        k31 = h*D1(t+h*0.5, x+0.5*k21, v+0.5*k22);
        k32 = h*D2(t+h*0.5, x+0.5*k21, v+0.5*k22);
        k41 = h*D1(t+h, x+k31, v+k31);
        k42 = h*D2(t+h, x+k31, v+k32);
        
        kprom1=(k11+(2*k21)+(2*k31)+k41)/6;
        kprom2=(k12+(2*k22)+(2*k32)+k42)/6;
            
        outfile<<t<<" "<<x<<" "<<v<<endl;
        t=t+h;
        x=x+kprom1;
        v=v+kprom2;
        
    }
    
    outfile.close();
}

double D1(double t,double x,double v){
    return v;
}

double D2(double t,double x,double v){
    double k =300;
    double m =2;
    return x*(-k/m);
}