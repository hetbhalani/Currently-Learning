#include<iostream>
using namespace std;

int main(){
    int age;
    string name;

    cout << "Enter your age: " << endl;
    cin >> age;

    // cin.ignore(1000,'\n'); //ignores last 1000 chars in buffer 

    cout << "Enter your name: "<< endl;
    getline(cin,name);

    cout <<"Your name is "<< name << endl;
    cout<< "Your age is "<< age << endl; 
    return 0;
}