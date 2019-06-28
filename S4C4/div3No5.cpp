#include <iostream>

using namespace std;

int main(){
    cout<<"Los números de 0-100 divisibles entre 3 pero no entre 5 son:"<<endl;
    for(int i=0;i<101;i++){
        if(i%3==0){
            if(i%5!=0){
                cout<<i<<endl;
            }
        }
    }
}
