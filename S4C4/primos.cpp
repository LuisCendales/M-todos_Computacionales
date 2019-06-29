#include <iostream>

using namespace std;

bool check(int a);

int main(){
    int a,b;
    
    cout<<"Este programa busca los números primos entre dos límites"<<endl;
    
    cout<<"Introduzca el límite entero inferior: ";
    cin>>a;
    cout<<"Introduzca el límite entero superior: ";
    cin>>b;
    
    cout<<"Los números primos son: "<<endl;
    for(int i=a;i<=b;i++){
        bool c=check(i);
        if(c==false and i>=2){
            cout<<i<<endl;
        }
    }
    return 0;
}

bool check(int a){
    bool c=false;
    for(int i=2;i<a;i++){
        if(a%i==0){
            c=true;
        }
    }
    return c;
}