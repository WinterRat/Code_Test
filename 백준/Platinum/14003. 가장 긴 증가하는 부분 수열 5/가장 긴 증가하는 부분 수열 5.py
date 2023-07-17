from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = []
dp_indices = [0 for _ in range(N)]
result = [0 for _ in range(N)]

for i in range(N):
    if i == 0 or A[i] > dp[-1]:
        dp.append(A[i])
        dp_indices[i] = len(dp) - 1
    else:
        idx = bisect_left(dp, A[i])
        dp[idx] = A[i]
        dp_indices[i] = idx

print(len(dp))

idx = len(dp) - 1
for i in range(N-1, -1, -1):
    if dp_indices[i] == idx:
        result[idx] = A[i]
        idx -= 1

for i in range(len(dp)):
    print(result[i], end=' ')