from sys import stdin
from collections import defaultdict

def dfs_find(node):
    if visited[node]:
        return False
    else :
        visited[node] = True

    for adj_node in graph[node]:
        if not seleted[adj_node] or dfs_find(seleted[adj_node]):
            seleted[adj_node] = node
            return True
    return False

N, M = map(int, stdin.readline().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

seleted = [0] * (N+1)
count = 0

for i in range(1, N+1):
    visited = [False] * (N+1)
    if dfs_find(i):
        count += 1

print(count//2)