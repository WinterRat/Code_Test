from sys import stdin
from collections import deque

input = stdin.readline
def solve():
    result = []
    queue = deque()

    # 시작 0인 노드 큐에 
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 위상 정렬!
    while queue:
        now = queue.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 된 노드를 큐에 삽입
            if indegree[i] == 0:
                queue.append(i)

    return result


N, M = map(int, input().split())
indegree = [0] * (N + 1)  # 진입 차수 0으로 초기화
graph = [[] for _ in range(N + 1)]  # 각 노드에 연결된 간선 정보담음

# 방향 그래프의 모든 간선 정보 입력 
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  # A에서 B로 이동 가능
    indegree[b] += 1  # 진입 차수를 증가

result = solve()

for i in result:
    print(i, end=' ')
