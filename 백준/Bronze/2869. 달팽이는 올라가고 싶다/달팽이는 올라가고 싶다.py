import math

A, B, V = map(int, input().split())

n = math.ceil((V-A) / (A-B))

print(n+1)