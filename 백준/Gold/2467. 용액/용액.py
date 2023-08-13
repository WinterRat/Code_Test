import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))

left = 0
right = n - 1
arr.sort()
best_sum = float('inf')
answer = (0, 0)

while left < right:
    sum = arr[left] + arr[right]
    
    if abs(sum) < abs(best_sum):
        best_sum = sum
        answer = (arr[left], arr[right])
    
    if sum < 0:
        left += 1
    else:
        right -= 1

print(*answer)