from sys import stdin
from bisect import bisect_left
input = stdin.readline

n = int(input())
sy = list(map(int, input().split()))

sorted_long = [sy[0]]

for i in range(n):
    # 새로온게 크면 이어서 붙여주고
    if sorted_long[-1] < sy[i]:
        sorted_long.append(sy[i])
    # 같거나 작으면 순서맞춰서 앞에 넣어줌
    else:
        sorted_long[bisect_left(sorted_long, sy[i])] = sy[i]

print(len(sorted_long))