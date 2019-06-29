#include <iostream>

using namespace std;

int factorial(int n);

int main(){
    int a;
    int f;    
    
    cout<<"Valor para hallar su factorial: ";
    cin>>a;
    
    f=factorial(a);
    
    cout<<"El factorial de "<<a<<" da: "<<f<<endl;
       
    
    return 0;
}

int factorial(int a){
    int f = 1;
    for(int i=1;i<=a;i++){
        f=f*i;
    }
    return f;
}