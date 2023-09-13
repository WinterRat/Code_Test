#include <iostream>
#include <string>
using namespace std;

bool is_valid(const string &str, int s, int e) {
    if (s > e) return true;

    int mid = (s + e) / 2;

    int left = mid - 1;
    int right = mid + 1;

    while (left >= s && right <= e) {
        if (str[left] == str[right]) return false; // 같은 문자면 잘못 접힘
        left--;
        right++;
    }
    return is_valid(str, s, mid - 1) && is_valid(str, mid + 1, e);
}

int main() {
    int n;
    cin >> n;
    while (n--) {
        string str;
        cin >> str;
        if (is_valid(str, 0, str.size() - 1)) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}