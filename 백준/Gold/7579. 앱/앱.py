from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
memorys = list(map(int, input().strip().split()))
costs = list(map(int, input().strip().split()))

max_cost = sum(costs)
dp = [[0] * (max_cost + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(max_cost + 1):
        if j < costs[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + memorys[i - 1])

for j in range(max_cost + 1):
    if dp[N][j] >= M:
        print(j)
        break