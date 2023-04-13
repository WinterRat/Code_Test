from sys import stdin
from collections import deque

input = stdin.readline

def bfs(graph, k, N):
    visited = [[False] * N for _ in range(2)]
    queue = deque([(0, 0, 0)])  # left/right, x, time

    while queue:
        lr, x, t = queue.popleft()
        if x >= N:
            return 1
        # 칸이 사라지는거 고려
        if x < 0 or x < t or visited[lr][x]:
            continue
        visited[lr][x] = True

        for d_lr, d_x in [(0, 1), (0, -1), (1, k)]:
            next_lr = (lr + d_lr) % 2
            next_x = x + d_x
            if 0 <= next_x < N and graph[next_lr][next_x] == '1':
                queue.append((next_lr, next_x, t + 1))
            elif next_x >= N:
                return 1
    return 0

def main():
    N, k = map(int, input().split())
    graph = []
    graph.append(input().strip())
    graph.append(input().strip())

    print(bfs(graph, k, N))

if __name__ == "__main__":
    main()