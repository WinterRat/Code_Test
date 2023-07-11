from sys import stdin
input = stdin.readline

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    dp = [0,1,1,1] + [0] * N
    for i in range(4, N+1):
        dp[i]=dp[i-2]+dp[i-3]
    result.append(dp[N])

for c in result:
    print(c)