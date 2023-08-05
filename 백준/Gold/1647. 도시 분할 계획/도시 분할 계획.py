from sys import stdin
import heapq
input = stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solve():
    n, m = map(int, input().split())
    parent = [0] * (n + 1)
    edges = []
    result = 0

    for i in range(1, n + 1):
        parent[i] = i

    for _ in range(m):
        a, b, cost = map(int, input().split())
        heapq.heappush(edges, (cost, a, b))

    max_cost = 0
    while edges:
        cost, a, b = heapq.heappop(edges)
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost
            max_cost = cost

    return result - max_cost

print(solve())