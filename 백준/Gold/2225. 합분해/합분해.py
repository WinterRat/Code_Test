from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
dp[0][0] = 1

for j in range(1, K+1):
    for i in range(0, N+1):
        for l in range(i+1):
            dp[i][j] += dp[l][j-1]
            dp[i][j] %= 1000000000

print(dp[N][K])