#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(pair<int, int> a, pair<int, int> b) {
    return a.first > b.first;
}

int main() {
    vector<pair<int, int>> scores;

    for (int i = 0; i < 8; i++) {
        int score;
        cin >> score;
        scores.push_back({score, i + 1});
    }

    sort(scores.begin(), scores.end(), comp);

    int sum = 0;
    vector<int> selected_questions;
    for (int i = 0; i < 5; i++) {
        sum += scores[i].first;
        selected_questions.push_back(scores[i].second);
    }

    cout << sum << endl;

    sort(selected_questions.begin(), selected_questions.end());
    for (int i = 0; i < 5; i++) {
        cout << selected_questions[i] << " ";
    }

    return 0;
}