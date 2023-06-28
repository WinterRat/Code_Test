#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>

using namespace std;

int N, K;
bool visit[1000001][11];

int main() {
    cin>>N>>K;

    queue<pair<int, int>> q;
    q.push({N, 0});
    int result = -1;

    while (!q.empty()) {
        int curN = q.front().first;
        int curK = q.front().second;
        q.pop();

        if (curK == K) {
            result = max(result, curN);
            continue;
        }

        string s = to_string(curN);

        for (int i = 0; i < s.size(); i++) {
            for (int j = i + 1; j < s.size(); j++) {
                if (i == 0 && s[j] == '0') continue;

                swap(s[i], s[j]);
                int nextN = stoi(s);

                if (!visit[nextN][curK + 1]) {
                    visit[nextN][curK + 1] = true;
                    q.push({nextN, curK + 1});
                }

                swap(s[i], s[j]);
            }
        }
    }
    cout << result <<"\n";

    return 0;
}