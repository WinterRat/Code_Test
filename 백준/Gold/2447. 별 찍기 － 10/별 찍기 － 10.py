import math
import sys
input = sys.stdin.readline

def solve(pattern):
    grid = []
    for i in range(3 * len(pattern)): # 0 ~ 8 > 0 ~ 26 > 0 ~ 80
        if i // len(pattern) == 1:
            grid.append(pattern[i % len(pattern)] + " " * len(pattern) + pattern[i % len(pattern)])
        else:
            grid.append(pattern[i % len(pattern)] * 3)
    return list(grid)

set = ["***",
       "* *",
       "***"]
N = int(input())
e = 0
while N != 3:
    N = N // 3
    e += 1
    
for i in range(e):
    set = solve(set)
    
print("\n".join(set))