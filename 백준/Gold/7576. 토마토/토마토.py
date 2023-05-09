from sys import stdin
from collections import deque

input = stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(start):
    q = deque(start)

    day = -1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<M and 0<=ny<N and graph[ny][nx]==0:
                    graph[ny][nx] = 1
                    q.append((nx,ny)) # 1로 변햇으니 추가
        day += 1        
    return day
    
M,N = map(int, input().split()) # M 가로, N 세로 칸
graph = [list(map(int,input().strip().split())) for _ in range(N)]
start = [(j, i) for i in range(N) for j in range(M) if graph[i][j] == 1]
zero_count = sum(x.count(0) for x in graph)

if zero_count == 0:
    print(0)
else :
    days = bfs(start)
    if sum(x.count(0) for x in graph) > 0:
        print(-1)
    else:
        print(days)