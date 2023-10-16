#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int N;
int S[20][20];
bool visited[20];
int answer = 1e9;

void calculate() {
    vector<int> start, link;
    for (int i = 0; i < N; i++) {
        if (visited[i])
            start.push_back(i);
        else
            link.push_back(i);
    }

    int s_sum = 0, link_sum = 0;
    for (int i = 0; i < N / 2; i++) {
        for (int j = 0; j < N / 2; j++) {
            if (i == j) continue;
            s_sum += S[start[i]][start[j]];
            link_sum += S[link[i]][link[j]];
        }
    }

    int diff = abs(s_sum - link_sum);
    answer = min(answer, diff);
}

void dfs(int idx, int cnt) {
    if (cnt == N / 2) {
        calculate();
        return;
    }

    for (int i = idx; i < N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            dfs(i + 1, cnt + 1);
            visited[i] = false;
        }
    }
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> S[i][j];

    dfs(0, 0);

    cout << answer;
    return 0;
}