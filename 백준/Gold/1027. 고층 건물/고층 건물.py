from sys import stdin
input = stdin.readline

n = int(input())
heights = list(map(int, input().split()))

result = 0

for i in range(n):
    cnt = 0
    
    # 왼쪽 빌딩 검사
    min_slope = float('inf')
    for j in range(i-1, -1, -1):
        slope = (heights[j] - heights[i]) / (j - i)
        if slope < min_slope:
            cnt += 1
            min_slope = slope

    # 오른쪽 빌딩 검사
    max_slope = float('-inf')
    for j in range(i+1, n):
        slope = (heights[j] - heights[i]) / (j - i)
        if slope > max_slope:
            cnt += 1
            max_slope = slope

    result = max(result, cnt)

print(result)