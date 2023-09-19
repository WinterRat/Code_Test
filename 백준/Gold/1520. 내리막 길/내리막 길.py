from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[-1]*m for _ in range(n)]

def dfs(x, y):
    # 도착점에 도달하면 1 반환
    if x == n-1 and y == m-1:
        return 1

    # 이미 계산된 dp 값이라면 해당 값을 바로 반환
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 방문 표시 (현재 위치에서 시작하는 경로의 수를 0으로 초기화)
    dp[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]   

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] < board[x][y]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))