#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;
int ppunto(int m[],int n[]);
int producto(int i,int m[],int n[]);

int main(){
    int arr1[]={1,2,3,4,5};
    int arr2[]={10,20,30,40,50};
    int dot;
    
    cout<<"El producto entre los dos arrays es: "<<endl;
    for(int i=0;i<5;i++){
        int a;
        a=producto(i,arr1,arr2);
        cout<<a<<endl;
    }
    
    cout<<"El producto punto entre los dos arrays es: "<<dot<<endl;
    return 0;
}
int ppunto(int m[],int n[]){
    int a;
    for(int i=0;i<5;i++){
        a+=(m[i]*n[i]);
    }
    return a;
}

int producto(int i,int m[],int n[]){
    int a;
    a=m[i]*n[i];
    return a;
}