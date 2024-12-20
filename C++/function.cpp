#include<iostream>
#include<cmath>
using namespace std;

void sayHello(string name){
    cout<< "Hello " << name << "\n" ;
}

double root (double num){
    return sqrt(num);
}

int main(){
    string name;
    cout << "Enter a name: ";
    cin >> name;
    sayHello(name);

    int num = 12;
    cout << root(num) ;
    return 0;
}