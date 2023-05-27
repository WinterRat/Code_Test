N=int(input())
graph = []
for _ in range(N):
    graph.append(int(input().strip()))
    
for c in sorted(graph):
    print(c)