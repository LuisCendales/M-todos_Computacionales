#include <iostream>

using namespace std;

int factorial(int n);

int main(){
    int a=7;
    int b=77;
    int fa,fb;
    
    fa=factorial(a);
    fb=factorial(b);
        
    cout<<"El factorial de "<<a<<" da: "<<fa<<endl;
    cout<<"El factorial de "<<b<<" da: "<<fb<<endl;
       
    
    return 0;
}

int factorial(int a){
    int f = 1;
    for(int i=1;i<=a;i++){
        f=f*i;
    }
    return f;
}