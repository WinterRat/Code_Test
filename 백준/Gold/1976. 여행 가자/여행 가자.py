from sys import stdin
from collections import deque
input = stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())

parent = [i for i in range(N+1)]

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j] == 1:
            union(parent, i+1, j+1)

plan = list(map(int, input().split()))

PF = True
for i in range(M-1):
    if find(parent, plan[i]) != find(parent, plan[i+1]):
        PF = False
        break

print("YES" if PF else "NO")