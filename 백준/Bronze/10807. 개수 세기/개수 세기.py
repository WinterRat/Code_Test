from sys import stdin
input = stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
v = int(input())
count = 0
for vv in numbers:
    if vv == v:
        count+=1

print(count)