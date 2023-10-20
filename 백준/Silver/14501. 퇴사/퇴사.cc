#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> T(N + 1);
    vector<int> P(N + 1);
    vector<int> dp(N + 2, 0);  // dp[i]: i일째에 받을 수 있는 최대 이익

    for (int i = 1; i <= N; i++) {
        cin >> T[i] >> P[i];
    }

    for (int i = 1; i <= N + 1; i++) {
        // 이전까지의 최대 이익을 현재의 최대 이익으로 업데이트
        dp[i] = max(dp[i], dp[i - 1]);

        // 상담을 완료한 날짜에 상담료를 추가
        if (i + T[i] <= N + 1) {
            dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i]);
        }
    }

    cout << dp[N + 1] << endl;
    return 0;
}