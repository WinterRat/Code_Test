from sys import stdin

input = stdin.readline


N = int(input())
M = int(input())
broken = [False]*10

if M > 0:
    arr = list(map(int, input().split()))
else:
    arr = []

for x in arr:  
    broken[x] = True

min_cnt = abs(100 - N)

for i in range(1000001):
    str_i = str(i)
    for j in range(len(str_i)):
        if broken[int(str_i[j])]:
            break
        elif j == len(str_i) - 1:
            min_cnt = min(min_cnt, abs(N - i) + len(str_i))
print(min_cnt)
