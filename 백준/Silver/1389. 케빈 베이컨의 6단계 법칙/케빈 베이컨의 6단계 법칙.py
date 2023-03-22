from collections import deque

def bfs(graph, start):
    visited = [False] * (len(graph) + 1) ## 직관적인 구현을 위해 1부터 시작하게끔
    distance = [0] * (len(graph) + 1)
    queue = deque([start])

    visited[start] = True ##시작은 방문한걸로 하고 시작

    while queue:  # 큐가 빌 때까지 반복
        v = queue.popleft() ## 방문한 곳은 꺼냄
        # 그리고 방금 꺼낸곳에서 연결된 곳, 가야할곳 조회
        for i in graph[v]:
            if not visited[i]: # 방문 안했다면
                queue.append(i) # 이제 오른쪽에 방문할곳으로 넣어두고
                visited[i] = True # i 번재 노드는 
                distance[i] = distance[v] + 1

    return sum(distance)

def main():
    N, M = map(int, input().split()) ## 친구 수, 관계 수
    graph = [[] for _ in range(N + 1)] # 0번 index []

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    kevin = [0] * (N + 1)

    for i in range(1, N + 1):
        kevin[i] = bfs(graph, i)

    print(kevin.index(min(kevin[1:])))

if __name__ == "__main__":
    main()