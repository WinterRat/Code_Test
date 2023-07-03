from sys import stdin
input = stdin.readline

x, y, w, s = map(int, input().split())

# 직선만 이동
case1 = (x+y) * w

# 대각선으로만 이동
if (x + y) % 2 == 0:
    case2 = max(x, y) * s
# 대각선이동 + 평행이동 1번
else:
    case2 = (max(x, y) - 1) * s + w

# 평행이동 + 대각선이동
case3 = (min(x, y) * s) + (abs(x-y) * w)

print(min(case1, case2, case3))