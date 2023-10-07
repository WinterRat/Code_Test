#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    int count_0 = 0;  // 1에서 0으로
    int count_1 = 0;  // 0에서 1로 

    if (s[0] == '1') {
        count_1++;
    } else {
        count_0++;
    }

    for (int i = 1; i < s.size(); i++) {
        if (s[i] != s[i-1]) {  // 이전 문자와 현재 문자가 다를 경우
            if (s[i] == '1') {
                count_1++;
            } else {
                count_0++;
            }
        }
    }

    cout << min(count_0, count_1) << endl;

    return 0;
}