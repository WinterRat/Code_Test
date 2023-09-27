from sys import stdin
input = stdin.readline

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, path):
    global max_val
    max_val = max(max_val, len(path))

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in path:
            dfs(nx, ny, path + board[nx][ny])

max_val = 1
dfs(0, 0, board[0][0])
print(max_val)