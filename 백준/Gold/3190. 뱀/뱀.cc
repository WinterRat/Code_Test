#include <iostream>
#include <deque>
#include <vector>
#include <map>
using namespace std;

struct Position {
    int x, y;
};

int N, K, L;
int board[101][101]; // 0: 빈칸, 1: 사과, 2: 뱀
deque<Position> snake;
map<int, char> changes;

const Position directions[4] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}; // 우, 하, 좌, 상

bool TF_position(Position p) {
    return p.x >= 0 && p.x < N && p.y >= 0 && p.y < N;
}

int main() {
    cin >> N;
    cin >> K;

    for(int i=0; i<K; i++) {
        int x, y;
        cin >> x >> y;
        board[x-1][y-1] = 1;
    }

    cin >> L;
    for(int i=0; i<L; i++) {
        int time; char dir;
        cin >> time >> dir;
        changes[time] = dir;
    }

    int direction = 0; // 시작은 오른쪽
    int time = 0;
    snake.push_front({0, 0});
    board[0][0] = 2;

    while(true) {
        time++;

        Position n_pos = {snake.front().x + directions[direction].x, snake.front().y + directions[direction].y};

        if(!TF_position(n_pos) || board[n_pos.x][n_pos.y] == 2) {
            // 벽에 부딪히거나 뱀의 몸통과 부딪히면 게임 종료
            break;
        }
        // 사과 없을때
        if(board[n_pos.x][n_pos.y] == 0) {
            Position tail = snake.back();
            snake.pop_back();
            board[tail.x][tail.y] = 0;
        }

        snake.push_front(n_pos);
        board[n_pos.x][n_pos.y] = 2;

        if(changes.count(time)) {
            // 방향 전환
            if(changes[time] == 'L') direction = (direction + 3) % 4;
            else direction = (direction + 1) % 4;
        }
    }

    cout << time << endl;
    return 0;
}