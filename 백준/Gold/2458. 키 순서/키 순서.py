from sys import stdin

def dfs(graph, start):
    visited = [False] * len(graph)
    stack = [start]

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            for i, v in enumerate(graph[current]):
                if v == 1 and not visited[i]:
                    stack.append(i)
    return visited

input = stdin.readline

N, M = map(int, input().split())
row_graph = [[0] * N for _ in range(N)]
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split()) # a<b
    graph[a-1][b-1] = 1
    row_graph[b-1][a-1] = 1

count = 0
for i in range(N):
    visited_up = dfs(graph, i)  # i에서 갈 수 있는 모든 노드를 방문 나보다 큰쪽으로
    visited_down = dfs(row_graph, i)  # i로 올 수 있는 모든 노드를 방문 나보다 작은 쪽으로
    if visited_up.count(True) + visited_down.count(True) - 1 == N:
        count += 1

print(count)