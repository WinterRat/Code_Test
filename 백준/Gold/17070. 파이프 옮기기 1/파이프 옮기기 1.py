from sys import stdin
input = stdin.readline

N = int(input())
house = [[0]*(N+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N+1)] for _ in range(N+1)]
dp[1][2][0] = 1

for i in range(1, N+1):
    for j in range(2, N+1):
        if house[i][j] == 0:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] += dp[i-1][j][1] + dp[i-1][j][2]
            
            if house[i-1][j] == 0 and house[i][j-1] == 0:
                dp[i][j][2] += sum(dp[i-1][j-1])

print(sum(dp[N][N]))