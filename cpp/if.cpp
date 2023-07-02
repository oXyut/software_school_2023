#include <iostream>

using namespace std;

int main(){
    int a = 0;
    for(int i=0; i < 10; i++){
       if(a % 2 == 0) cout << a << endl;
       a++;
    }
    return 0;
}

