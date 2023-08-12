from collections import deque
from sys import stdin

input = stdin.readline
n, m = map(int, input().strip().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
group = [[-1] * m for _ in range(n)]
group_size = {}

def bfs(x, y, label):
    q = deque([(x, y)])
    count = 1
    group[x][y] = label
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and group[nx][ny] == -1:
                group[nx][ny] = label
                q.append((nx, ny))
                count += 1
    return count

label = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and group[i][j] == -1:
            group_size[label] = bfs(i, j, label)
            label += 1

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            wall_group = set()
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < n and 0 <= nj < m and group[ni][nj] != -1:
                    wall_group.add(group[ni][nj])
            grid[i][j] = (sum(group_size[g] for g in wall_group) + 1) % 10
    print(''.join(map(str, grid[i])))