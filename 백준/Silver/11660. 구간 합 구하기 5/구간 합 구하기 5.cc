#include <iostream>
#include <vector>

using namespace std;

int main() {
    // for codetest cpp
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M;
    cin>>N>>M;

    vector<vector<int>> xy(N+1, vector<int>(N+1, 0));
    vector<vector<int>> dp(N+1, vector<int>(N+1, 0));

    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            cin>>xy[i][j];
        }
    }
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= N; ++j) {
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + xy[i][j];
        }
    }

    for (int i = 0; i < M; ++i) {
        int x1, y1, x2, y2;
        cin>>x1>>y1>>x2>>y2;

        int sum = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1];
        cout << sum <<'\n';
    }
    return 0;
}