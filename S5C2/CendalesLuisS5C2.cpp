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
    
    n=(max-min)/h;
    
    double x = 0.;
    double y = 1.;
    
    outfile1.open("euler.dat");
    for(int i=0;i<n;i++){
        outfile1<<x<<" "<<y<<endl;
        y=y+(h*ecuacion(x,y));
        x=x+h;
    }
    outfile1.close();
    return 0;
}

double ecuacion(double x, double y){
    return -y;
}
