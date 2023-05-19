from sys import stdin

input = stdin.readline

N = int(input())
graph = [0]*10000

for i in range(N):
    a = int(input())
    graph[a-1] += 1
    
for i in range(10000):
    if graph[i] != 0:
        for j in range(graph[i]):
            print(i+1)