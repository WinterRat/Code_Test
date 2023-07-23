from sys import stdin
input = stdin.readline

def factorial_DP(n):
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1, n+1):
        dp[i] = dp[i-1]*i

    return dp[n]

def combination(n, m):
    return int(factorial_DP(m) / (factorial_DP(n) * factorial_DP(m - n)))

T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())
    result.append(combination(N,M))
    
print(*result,sep='\n')