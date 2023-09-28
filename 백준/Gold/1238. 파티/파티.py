import heapq
from sys import stdin
input = stdin.readline

def dijkstra(start, graph, n):
    distance = [float('inf')] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

result = [0] * (n+1)

for i in range(1, n+1):
    temp = dijkstra(i, graph, n)
    result[i] += temp[x]

temp = dijkstra(x, graph, n)
for i in range(1, n+1):
    result[i] += temp[i]

print(max(result[1:]))