from collections import deque
from sys import stdin

input = stdin.readline

def bfs(graph) :

    parent = [0 for _ in range(len(graph)+1)]
    need_visit = deque()
    need_visit.append(1)
    
    while need_visit:
        n = need_visit.popleft()
        for i in graph[n]:
            if parent[i] == 0:
                parent[i] = n
                need_visit.append(i)

    return parent
                 
    
def main():
    N = int(input())
    
    graph = [[] for _ in range(N+1)]
    
    for _ in range(N-1):
        go, stop = map(int,input().split())
        graph[go].append(stop)
        graph[stop].append(go)
        
    parent_nodes = bfs(graph)

    for i in range(2, N + 1):
        print(f"{parent_nodes[i]}")


if __name__ == "__main__":
    main()