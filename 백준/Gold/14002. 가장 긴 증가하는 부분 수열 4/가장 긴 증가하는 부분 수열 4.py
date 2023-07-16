from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0] * n
# 이전 위치를 저장
v = [-1] * n

for i in range(n):
    # 자기자신만 포함
    dp[i] = 1
    # 지금 i 에서 이전의 모든 위치 탐색
    for j in range(i):
        # 이전 원소들 중 가장 큰 dp값 + 1
        if a[j] < a[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            v[i] = j
            
# 가장 긴 수열 길이 저장
max_value = max(dp)
index = dp.index(max_value)
result = []

while index != -1:
    result.append(a[index])
    index = v[index]

result.reverse()

print(max_value)
print(*result, sep=' ')