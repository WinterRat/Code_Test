from collections import deque
from sys import stdin

input = stdin.readline

def dfs(start):
    visit = [0] * (N + 1)
    stack = [start]

    while stack:
        curr = stack.pop()
        if not visit[curr]:
            visit[curr] = 1
            for n in group[curr]:
                if not visit[n]:
                    stack.append(n)
                    c_point[n] += c_point[curr]


N, M = map(int, input().split())

boss = list(map(int, input().split()))
group = [[] for _ in range(N + 1)]

c_point =[0] * (N+1)


for i in range(1, N+1) :
    if boss[i-1]!=-1 : 
        group[boss[i-1]].append(i) 

for _ in range(M):
    i, w = map(int, input().split())
    # 바로 더해버려
    c_point[i] += w
    
dfs(1)
print(*c_point[1:])