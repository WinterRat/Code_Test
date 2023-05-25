from sys import stdin
from collections import deque

input = stdin.readline

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
result = [0]*(N+1)

def dfs(start):
    stack = [start]
    visited = [False]*(N+1)
    visited[start] = True
    count = 0
    
    while stack:
        node = stack.pop()
        count += 1
        for adj in graph[node]:
            if not visited[adj]:
                stack.append(adj)
                visited[adj] = True
    result[start] = count

for _ in range(M):
    e,s = map(int,input().split())
    graph[s].append(e)

for i in range(1,N+1):
    dfs(i)

max_value = max(result)
max_index = [i for i, num in enumerate(result) if num == max_value]
print(*max_index)