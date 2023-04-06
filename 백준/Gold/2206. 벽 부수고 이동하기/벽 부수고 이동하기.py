from sys import stdin
from collections import deque

input = stdin.readline

def bfs(graph):
    visited = [[[-1, -1] for _ in range(M)] for _ in range(N)]
    queue = deque([(0, 0, 0)])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[0][0][0] = 1

    while queue:
        x, y, count = queue.popleft()
        if x == M-1 and y == N-1:
            return visited[y][x][count] if visited[y][x][count] != -1 else visited[y][x][1-count]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0 and visited[ny][nx][count] == -1:
                    visited[ny][nx][count] = visited[y][x][count] + 1
                    queue.append((nx, ny, count))

                elif graph[ny][nx] == 1 and count == 0:
                    if visited[ny][nx][1] == -1:
                        visited[ny][nx][1] = visited[y][x][0] + 1
                        queue.append((nx, ny, 1))
    return -1

def main():
    global N, M
    N, M = map(int, input().split())
    graph = [list(map(int, input().strip())) for _ in range(N)]

    print(bfs(graph))

if __name__ == "__main__":
    main()