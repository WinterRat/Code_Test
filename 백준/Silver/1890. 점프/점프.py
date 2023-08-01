from sys import stdin

input = stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            break
        if dp[i][j]>0: 
            jump = graph[i][j]
            if i + jump < n: # 오른쪽으로 이동 
                dp[i + jump][j] += dp[i][j]
            if j + jump < n: # 아래로 이동 
                dp[i][j + jump] += dp[i][j]

print(dp[n-1][n-1])