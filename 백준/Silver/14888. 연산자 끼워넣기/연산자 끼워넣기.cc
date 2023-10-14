#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<int> numbers;
vector<int> operators;

int max_result = -1e9; 
int min_result = 1e9;  
// by 재귀
void solve(int depth, int current) {
    if (depth == N - 1) { // 모든 연산자를 사용한 경우
        max_result = max(max_result, current);
        min_result = min(min_result, current);
        return;
    }

    for (int i = 0; i < 4; ++i) {
        if (operators[i] > 0) { // 해당 연산자를 아직 다 사용하지 않았다면
            int next = current;
            if (i == 0) next += numbers[depth + 1];
            else if (i == 1) next -= numbers[depth + 1];
            else if (i == 2) next *= numbers[depth + 1];
            else if (i == 3) next /= numbers[depth + 1];

            operators[i]--;
            solve(depth + 1, next);
            operators[i]++;
        }
    }
}

int main() {
    cin >> N;
    numbers.resize(N);
    operators.resize(4);

    for (int i = 0; i < N; ++i) {
        cin >> numbers[i];
    }
    for (int i = 0; i < 4; ++i) {
        cin >> operators[i];
    }
    solve(0, numbers[0]);
    cout << max_result << "\n" << min_result << "\n";
    return 0;
}