from sys import stdin
from collections import deque

input = stdin.readline

def bfs(N, K):
    visited = [0] * 100001
    queue = deque([(N, 0)])
    visited[N] = 1
    min_time = None
    count = 0

    while queue:
        x, time = queue.popleft()

        if min_time is not None and time > min_time:
            break

        if x == K:
            if min_time is None:
                min_time = time
            count += 1

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and (visited[nx] == 0 or visited[nx] >= time + 1):
                visited[nx] = time + 1
                queue.append((nx, time+1))

    return min_time, count

    
def main():
    N, K = map(int, input().split())
    print(bfs(N,K)[0])
    print(bfs(N,K)[1])
    
    
if __name__ == "__main__":
    main()  