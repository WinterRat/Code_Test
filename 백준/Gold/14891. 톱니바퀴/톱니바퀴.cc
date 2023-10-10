#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> gears(4);

void rotate(int num, int dir) {
    if(dir == 1) { // 시계 방향
        char temp = gears[num][7];
        for(int i=7; i>0; i--) {
            gears[num][i] = gears[num][i-1];
        }
        gears[num][0] = temp;
    } else { // 반시계 방향
        char temp = gears[num][0];
        for(int i=0; i<7; i++) {
            gears[num][i] = gears[num][i+1];
        }
        gears[num][7] = temp;
    }
}

void move(int num, int dir, vector<bool>& visited) {
    visited[num] = true;
    int left = num - 1;
    int right = num + 1;
    if(left >= 0 && !visited[left] && gears[left][2] != gears[num][6]) {
        move(left, -dir, visited);
    }
    if(right <= 3 && !visited[right] && gears[right][6] != gears[num][2]) {
        move(right, -dir, visited);
    }
    rotate(num, dir);
}

int main() {
    for(int i=0; i<4; i++) {
        cin >> gears[i];
    }

    int K;
    cin >> K;
    for(int i=0; i<K; i++) {
        int num, dir;
        cin >> num >> dir;
        vector<bool> visited(4, false);
        move(num-1, dir, visited);
    }

    int result = 0;
    if(gears[0][0] == '1') result += 1;
    if(gears[1][0] == '1') result += 2;
    if(gears[2][0] == '1') result += 4;
    if(gears[3][0] == '1') result += 8;

    cout << result << endl;

    return 0;
}

