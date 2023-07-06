#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, L;
    cin >> N >> L;

// 2개면 pair 가 편함
    vector<pair<int, int>> holes(N);
    for(int i = 0; i < N; ++i) {
        cin >> holes[i].first >> holes[i].second;
    }

    sort(holes.begin(), holes.end());

    int planks = 0, last = 0;
    // 구멍들을 찾아다니면서
    for(auto &hole : holes) {
        // 현재 구멍의 마지막이 기존보다 작으면 건너뛰어
        if(hole.second <= last) continue;
        // 아니면 새로운 구멍 정보 갱신 
        hole.first = max(hole.first, last);  
        int needed = (hole.second - hole.first + L - 1) / L;  
        last = hole.first + needed * L;  
        planks += needed;
    }

    cout << planks << "\n";
    return 0;
}