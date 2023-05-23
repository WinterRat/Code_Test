from sys import stdin
from collections import deque
input = stdin.readline
## 0북 1동 2남 3서 
def bfs(r,c,d):
    q = deque()
    q.append((c,r,d))
    cnt = 0

    while q:
        x,y,h = q.popleft()
        if graph[y][x] == 0:
            graph[y][x] = 2
            cnt += 1

        # 북동남서 0이 하나도 없는 경우
        if graph[y+1][x] != 0 and graph[y][x+1] != 0 and graph[y-1][x] != 0 and graph[y][x-1] != 0:
            # 바라보는 방향 유지 한칸 후진 가능하면
            if h == 0 and graph[y+1][x] != 1 :
                q.append((x,y+1,h))

            elif h == 1 and graph[y][x-1] != 1 :
                q.append((x-1,y,h))

            elif h == 2 and graph[y-1][x] != 1 :
                q.append((x,y-1,h))

            elif h == 3 and graph[y][x+1] != 1 :
                q.append((x+1,y,h))

            else:
                return cnt
        ## 북동남서 청소하지않은 0이 있는경우     
        elif graph[y+1][x] == 0 or graph[y][x+1] == 0 or graph[y-1][x] == 0 or graph[y][x-1] == 0:
            dh = h-1
            if h-1 < 0 :
                dh = 3
            
            ## 북쪽을 보고 앞에가 0이면
            if 0 <= y-1 and dh == 0 and graph[y-1][x] == 0:
                q.append((x,y-1,dh))


            elif x+1 <M and dh == 1 and graph[y][x+1] == 0:
                q.append((x+1,y,dh))


            elif y+1 < N and dh == 2 and graph[y+1][x] == 0:
                q.append((x,y+1,dh))


            elif 0 <= x-1 and dh == 3 and graph[y][x-1] == 0:
                q.append((x-1,y,dh))

            else :
                q.append((x,y,dh))
            


    return cnt


    
N, M = map(int, input().split())
r,c,d = map(int,input().split()) ## r=x좌표, c=y좌표, d= 0 북동남서 순
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

print(bfs(r,c,d))