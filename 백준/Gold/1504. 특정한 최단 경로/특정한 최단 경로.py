import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start, graph, distance):
    q = [(0, start)]  # 시작노드거리 더하고 시작
    distance[start] = 0  # 시작거리는 0
    while q:  
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # 이미 처리된 노드면
            continue
        for i in graph[now]:  # 갈수있는 모든 노드
            length= dist + i[1]  # 노드 이동거리 +
            if length< distance[i[0]]:  # 해당 거리가 최단거리라면
                distance[i[0]] = length
                heapq.heappush(q, (length, i[0])) 

def short_road(N, E, graph, v1, v2):
    dist1, dist2, dist3 = [INF] * (N + 1), [INF] * (N + 1), [INF] * (N + 1)

    dijkstra(1, graph, dist1)
    dijkstra(v1, graph, dist2)
    dijkstra(v2, graph, dist3)

    # 가능한 경로 고려
    answer = min(dist1[v1] + dist2[v2] + dist3[N], dist1[v2] + dist3[v1] + dist2[N])

    if answer < INF:
        return answer
    else:
        return -1

def main():
    N, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, sys.stdin.readline().split())
    print(short_road(N, E, graph, v1, v2))

if __name__ == "__main__":
    main()