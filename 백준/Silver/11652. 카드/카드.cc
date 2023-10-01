#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<long long> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    long long answer = arr[0];
    int max_cnt = 1, cnt = 1;

    for (int i = 1; i < n; i++) {
        if (arr[i] == arr[i - 1]) {
            cnt++;
        } else {
            cnt = 1;
        }

        if (cnt > max_cnt) {
            max_cnt = cnt;
            answer = arr[i];
        }
    }

    cout << answer << '\n';
    return 0;
}