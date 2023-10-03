#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int T, N;
    cin >> T;

    while(T--) {
        cin >> N;
        vector<pair<int, int>> scores(N);
        
        for(int i = 0; i < N; ++i) {
            cin >> scores[i].first >> scores[i].second;
        }

        sort(scores.begin(), scores.end());

        int count = 1; // 첫 번째 사람은 무조건 선발
        int minInterviewScore = scores[0].second;

        for(int i = 1; i < N; ++i) {
            if(scores[i].second < minInterviewScore) {
                count++;
                minInterviewScore = scores[i].second;
            }
        }

        cout << count << '\n';
    }

    return 0;
}