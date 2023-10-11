#include <iostream>
#include <vector>
#include <map>
using namespace std;

int bingo[5][5];
map<int, pair<int, int>> position;
vector<int> calls;

int check_line(int x, int y) {
    int count = 0;
    // 가로 체크
    bool h = true;
    for(int i = 0; i < 5; i++) {
        if(bingo[x][i] != 0) {
            h = false;
            break;
        }
    }
    if(h) count++;

    // 세로 체크
    bool v = true;
    for(int i = 0; i < 5; i++) {
        if(bingo[i][y] != 0) {
            v = false;
            break;
        }
    }
    if(v) count++;

    // 대각선 체크
    if(x == y) {
        bool d1 = true;
        for(int i = 0; i < 5; i++) {
            if(bingo[i][i] != 0) {
                d1 = false;
                break;
            }
        }
        if(d1) count++;
    }
    
    if(x + y == 4) {
        bool d2 = true;
        for(int i = 0; i < 5; i++) {
            if(bingo[i][4-i] != 0) {
                d2 = false;
                break;
            }
        }
        if(d2) count++;
    }

    return count;
}

int main() {
    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 5; j++) {
            cin >> bingo[i][j];
            position[bingo[i][j]] = {i, j};
        }
    }
    
    for(int i = 0; i < 25; i++) {
        int num;
        cin >> num;
        calls.push_back(num);
    }

    int line_count = 0;
    for(int k = 0; k < 25; k++) {
        int num = calls[k];
        int x = position[num].first;
        int y = position[num].second;
        bingo[x][y] = 0;

        if(check_line(x, y)) {
            line_count += check_line(x, y);
            if(line_count >= 3) {
                cout << k+1 << endl;
                break;
            }
        }
    }
    return 0;
}