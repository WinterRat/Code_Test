from sys import stdin
from collections import deque

input = stdin.readline

def bfs(N,K):
    visited = [False] * 100001
    queue = deque([(N, 0)])

    while queue:
        x, time = queue.popleft()

        if x == K:
            return time

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time+1))
    
    
def main():
    N, K = map(int, input().split())
    print(bfs(N,K))
    
    
if __name__ == "__main__":
    main()