from sys import stdin

input = stdin.readline

N = int(input())
homes = [list(map(int, input().strip().split())) for _ in range(N)]

INF = int(1e9)
result = INF

for first_color in range(3):
    dp = [[0] * 3 for _ in range(N)]
    for i in range(3):
        if i == first_color:
            dp[0][i] = homes[0][i]
        else:
            dp[0][i] = INF
            
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + homes[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + homes[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + homes[i][2]

    for color in range(3):
        if color == first_color: continue
        result = min(result, dp[N-1][color])

print(result)