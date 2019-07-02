#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;
const double h=0.0001

int main(){
    int inicio,fin,num;
    ofstream outfile;
    double dx;
    
    cout<<"Ingrese el límite inicial de la funcion: ";
    cin>>inicio;
    
    cout<<"Ingrese el límite final de la funcion: ";
    cin>>fin;
    
    cout<<"Ingrese la cantidad de datos a tomar en cuenta de la funcion: ";
    cin>>num;
    
    int x[num];
    dx=(fin-inicio)/(num-1);
    
    x[i]=inicio;
    
    for(i=0;i<num;i++){
        cout<<x[i]<<endl;
        x[i]+=dx;
    }
    
    
    
//     outfile.open('datos.dat');
    
//     outfile.close();
    return 0;
}

double derivada(){
    
}

