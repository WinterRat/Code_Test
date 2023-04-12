from sys import stdin
from collections import deque

input = stdin.readline

def bfs(graph):
    dx = [1, 2, 3, 4, 5, 6]
    visited = [False] * 101
    queue = deque([(1, 0)])
    visited[1] = True

    while queue:
        x, count = queue.popleft()
        if x == 100:
            return count

        for i in range(6):
            nx = x + dx[i]
            if 1 <= nx <= 100 and not visited[nx]:
                if graph[nx] != 0:
                    nx = graph[nx]
                visited[nx] = True
                queue.append((nx, count + 1))

    return -1

def main():
    N, M = map(int, input().split())
    graph = [0] * 101

    for _ in range(N):
        x, y = map(int, input().split())
        graph[x] = y

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u] = v

    print(bfs(graph))

if __name__ == "__main__":
    main()