from sys import stdin
from collections import deque

input = stdin.readline

def bfs(graph, w, h):
    visited = [[False] * w for _ in range(h)]
    queue = deque()
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    count = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                count += 1
                visited[i][j] = True
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(8):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
    return count

def main():
    result = []
    while True:
        graph = []
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        for i in range(h):
            graph.append(list(map(int, input().split())))
        result.append(bfs(graph, w, h))
        
    for island_c in result:
        print(island_c)

if __name__ == "__main__":
    main()