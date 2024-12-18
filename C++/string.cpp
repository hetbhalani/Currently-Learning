#include<iostream>
using namespace std;

int main(){
    string name = "Bat Manas";
    cout << name.length() << endl ;
    cout << name[2] << endl;
    cout << name.find("a",4) << endl;
    cout<< name.substr(4,5) << endl; //4th index thi 5 chars lese
    
    // cout << "nvi liti" << endl;
    return 0;
}