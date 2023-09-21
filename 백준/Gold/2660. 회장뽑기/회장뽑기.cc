#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> dist(n + 1, vector<int>(n + 1, INF));

    for(int i = 1; i <= n; i++) {
        dist[i][i] = 0;
    }

    int a, b;
    while(true) {
        cin >> a >> b;
        if(a == -1 && b == -1) break;
        dist[a][b] = 1;
        dist[b][a] = 1;
    }
    
    for(int k = 1; k <= n; k++) {
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    vector<int> scores(n + 1, 0);
    int minScore = INF;
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= n; j++) {
            scores[i] = max(scores[i], dist[i][j]);
        }
        minScore = min(minScore, scores[i]);
    }

    vector<int> members;
    for(int i = 1; i <= n; i++) {
        if(scores[i] == minScore) members.push_back(i);
    }

    cout << minScore << " " << members.size() << endl;
    for(int member : members) {
        cout << member << " ";
    }

    return 0;
}