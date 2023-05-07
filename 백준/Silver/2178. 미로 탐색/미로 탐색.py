import sys
from collections import deque

input = sys.stdin.readline

def find(start,end):
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    q = deque()
    q.append((start,end))
    
    while q:
        x, y = q.popleft()             
        
        for dx,dy in ((1,0), (-1,0), (0,1), (0,-1)):
            if 0 <= x+dx < M and 0 <= y+dy < N and visited[y+dy][x+dx] == 0 and graph[y+dy][x+dx] == 1:
                q.append((x+dx,y+dy))
                visited[y+dy][x+dx] = visited[y][x] + 1
                
    return visited[N-1][M-1]     
                
                 
N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

print(find(0,0))