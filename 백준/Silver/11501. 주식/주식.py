from sys import stdin
from collections import deque
input = stdin.readline

# 1) 산다. 2) 원하는 만큼 판다. 3) 아무것도안함

def solve(p):
    cur_high = p[-1]
    profit = 0
    for i in range(len(p)-2,-1,-1):
        if p[i] > cur_high:
            cur_high = p[i]
        else :
            profit += cur_high - p[i]

    return profit
             
T = int(input())
result = []
for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))

    result.append(solve(price))
print(*result, sep='\n')
