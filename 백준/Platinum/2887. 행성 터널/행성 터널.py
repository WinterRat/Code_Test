from sys import stdin
input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    A = find(a)
    B = find(b)
    
    if A != B:
        parent[B] = A

N = int(input())
planet = []
parent = [i for i in range(N)]

for i in range(N):
    x, y, z = map(int, input().split())
    planet.append((x, y, z, i))

edges = []
for i in range(3):
    planet.sort(key=lambda x: x[i])
    for j in range(1, N):
        edges.append((planet[j-1][3], planet[j][3], abs(planet[j-1][i] - planet[j][i])))

edges.sort(key=lambda x: x[2])

result = 0
for a, b, cost in edges:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)