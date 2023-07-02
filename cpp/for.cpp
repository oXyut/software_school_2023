#include <iostream>

using namespace std;

int main(){
    int a = 0;
    for(int i=0; i < 10; i++){
        a++;
        cout << i << " " << a << endl;
    }
    cout << a << endl;
    cout << a / 20 << endl;
    cout << a / 20.0 << endl;
    return 0; 
}
