from sys import stdin
input = stdin.readline

N = int(input())
seq = list(map(int, input().split()))
dp = [[0]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if seq[i] == seq[j]:
            if j-i == 1 or dp[i+1][j-1]:
                dp[i][j] = 1

M = int(input())
result = []
for _ in range(M):
    S, E = map(int, input().split())
    result.append(dp[S-1][E-1])
    
print(*result, sep='\n')