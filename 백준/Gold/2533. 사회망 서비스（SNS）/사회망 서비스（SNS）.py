import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def dfs(u, parent, dp, graph):
    # u는 현재 노드, parent는 부모 노드
    dp[u][0] = 0  # 현재 노드가 얼리 어답터X
    dp[u][1] = 1  # 현재 노드가 얼리 어답터O
    
    for v in graph[u]:
        if v == parent:
            continue
        dfs(v, u, dp, graph)
        
        dp[u][0] += dp[v][1]  # 현재 노드가 얼리 어답터가 아닐 때, 자식 노드는 반드시 얼리 어답터
        dp[u][1] += min(dp[v][0], dp[v][1])  # 현재 노드가 얼리 어답터일 때, 자식 노드는 얼리 어답터일 수도, 아닐 수도

N = int(input())
graph = [[] for _ in range(N+1)]
dp = [[-1, -1] for _ in range(N+1)]  # dp[i][0]는 i가 얼리 어답터가 아닐 때, dp[i][1]는 i가 얼리 어답터일 때 필요한 최소 얼리 어답터 수

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0, dp, graph)
print(min(dp[1][0], dp[1][1]))