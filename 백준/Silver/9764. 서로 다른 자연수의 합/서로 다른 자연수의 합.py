from sys import stdin
input = stdin.readline

MAX_N = 2000

def solve(N):
    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1

    for i in range(1, N+1):
        for j in range(N+1):
            dp[i][j] = dp[i-1][j]
            if j >= i:
                dp[i][j] = (dp[i][j] + dp[i-1][j-i]) % 100999
    return dp[N][N]

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    result.append(solve(N))

print(*result, sep='\n')