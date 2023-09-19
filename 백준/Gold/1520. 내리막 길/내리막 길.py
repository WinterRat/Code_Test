import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, m, n, graph, dp):
    # (m, n)에 도달한 경우
    if x == m-1 and y == n-1:
        return 1
    # 이미 방문한 경우
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny]:
            dp[x][y] += dfs(nx, ny, m, n, graph, dp)
    return dp[x][y]

def main():
    m, n = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(m)]
    dp = [[-1] * n for _ in range(m)]
    print(dfs(0, 0, m, n, graph, dp))

if __name__ == "__main__":
    main()