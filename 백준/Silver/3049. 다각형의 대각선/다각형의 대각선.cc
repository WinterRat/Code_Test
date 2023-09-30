#include <iostream>
using namespace std;
// 조합론으로
int main() {
    int n;
    cin >> n;

    long long result = 1;
    for(int i = 0; i < 4; i++) {
        result *= n-i;
    }
    result /= 24;

    cout << result << '\n';
    return 0;
}