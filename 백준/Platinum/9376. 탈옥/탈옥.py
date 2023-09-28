from collections import deque
from sys import stdin

input = stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y, graph):
    h, w = len(graph), len(graph[0])
    visited = [[-1 for _ in range(w)] for _ in range(h)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == -1:
                if graph[nx][ny] == '*':
                    continue
                elif graph[nx][ny] == '#':
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx, ny))
                else:
                    visited[nx][ny] = visited[a][b]
                    q.appendleft((nx, ny))
    return visited

N = int(input())
result = []
for _ in range(N):
    h, w = map(int, input().split())
    graph = ['.' * (w + 2)]
    for _ in range(h):
        graph.append('.' + input() + '.')
    graph.append('.' * (w + 2))

    prison = [(i, j) for i in range(h+2) for j in range(w+2) if graph[i][j] == '$']

    outsect = bfs(0, 0, graph)
    ta = bfs(prison[0][0], prison[0][1], graph)
    tb = bfs(prison[1][0], prison[1][1], graph)

    ans = float('inf')
    for i in range(h + 2):
        for j in range(w + 2):
            if ta[i][j] != -1 and tb[i][j] != -1 and outsect[i][j] != -1:
                total = ta[i][j] + tb[i][j] + outsect[i][j]
                if graph[i][j] == '#':
                    total -= 2
                ans = min(ans, total)

    result.append(ans)
print(*result, sep ='\n')