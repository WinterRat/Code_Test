from sys import stdin
import heapq

input = stdin.readline
INF = int(1e9)

def dj(s, e):
    q = []
    ## 코스트 가야할 곳
    heapq.heappush(q,(0,s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]]=cost
                heapq.heappush(q,(cost,i[1]))


N = int(input()) ## 도시 수
M = int(input()) ## 버스 수
graph = [[] for _ in range(N+1)]
distance=[INF]*(N+1)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

s,e = map(int, input().split())
dj(s,e)
print(distance[e])