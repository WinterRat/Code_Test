#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<int> arr(n + 1, 0);
    vector<int> sum(n + 1, 0); 
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
        sum[i] = sum[i - 1] + arr[i];
    }

    for (int i = 0; i < m; i++) {
        int start, end;
        cin >> start >> end;

        cout << sum[end] - sum[start - 1] << '\n';
    }
    return 0;
}