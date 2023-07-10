from sys import stdin
input = stdin.readline
T = int(input())
result =[]
for _ in range(T):
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]

        for i in range(2, n):
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])

    result.append(max(dp[0][n-1], dp[1][n-1]))

for c in result:
    print(c)