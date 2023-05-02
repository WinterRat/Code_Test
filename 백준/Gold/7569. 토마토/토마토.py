from sys import stdin
from collections import deque

input = stdin.readline

def bfs(graph,m,n,h,start):
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque(start)
    days = -1
    while q:
        z, y, x ,d= q.popleft()
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = 1
                q.append((nz, ny, nx, d+1))
                days = d+1
                
    return days    
    
def main():
    m,n,h = map(int, input().split())
    graph = []
    start = [] # 익은 토마토의 위치를 넣으면서 저장하자.
    for i in range(h): # 높이 depth
        matrix = []
        for j in range(n): # 세로 row
            row = list(map(int, input().split()))
            for k in range(m): # 가로 col
                if row[k] == 1:
                    start.append((i,j,k,0))
            matrix.append(row)
        graph.append(matrix)
        
    if all(all(all(x != 0 for x in row) for row in matrix) for matrix in graph if matrix):
        print(0)
    else :
        days = bfs(graph,m,n,h,start)
        for i in range(h):
            for j in range(n):
                for k in range(m):
                    if graph[i][j][k] == 0:  # 익지 않은 토마토가 있으면 -1 반환
                        print(-1)
                        return
        print(days)
    
if __name__ == "__main__":
    main()