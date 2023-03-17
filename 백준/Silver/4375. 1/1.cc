#include <iostream>
using namespace std;

int main() {

    int n, d;
    while (!(cin>>n).eof()) {
        d = 1;
        int num = 1;
        while(true) {
            if (num % n == 0) { break; }
            d++;
            num = num * 10 + 1;
            num %= n;
        }
        cout<<d<<endl;
    }
    return 0;
}