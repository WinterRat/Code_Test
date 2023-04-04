from sys import stdin
from collections import deque
input = stdin.readline

def bfs(graph, start_end):
    dx = [-2, -2, 0, 0, 2, 2]
    dy = [-1, 1, -2, 2, -1, 1]

    queue = deque([(start_end[0], start_end[1], 0)]) # 이동횟수를 추가
    visited = set([(start_end[0], start_end[1])]) # 중복 방문 제거

    while queue:
        x, y, dist = queue.popleft()
        if x == start_end[2] and y == start_end[3]: # 도착지에 도착시 이동횟수 반환.
            return dist

        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph) and (nx, ny) not in visited:
                # 튜플은 add
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))

    return -1 # 다 해도 못가면 -1을 반환.
        
        
    
def main() :
    N = int(input())
    # r1 c1 r2 c2
    start_end = list(map(int, input().split()))    
    graph = [[-1 for _ in range(N) ] for _ in range(N)]
    
    print(bfs(graph, start_end))
    
if __name__=="__main__":
    main()