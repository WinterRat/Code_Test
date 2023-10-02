#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, C;
vector<int> house;

bool can_inst(int dist) {
    int cnt = 1; // 첫 집에는 항상 공유기 설치
    int last_house = house[0];

    for (int i = 1; i < N; i++) {
        if (house[i] - last_house >= dist) {
            cnt++;
            last_house = house[i];
        }
    }

    return cnt >= C;
}

int main() {
    cin >> N >> C;
    house.resize(N);

    for (int i = 0; i < N; i++) {
        cin >> house[i];
    }

    sort(house.begin(), house.end());

    int left = 1;
    int right = house[N-1] - house[0];
    int result = 0;

    while (left <= right) {
        int mid = (left + right) / 2;

        if (can_inst(mid)) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    cout << result << '\n';

    return 0;
}