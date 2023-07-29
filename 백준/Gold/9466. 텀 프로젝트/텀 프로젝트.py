import sys
sys.setrecursionlimit(111111) 
input = sys.stdin.readline

def dfs(x):
    global team
    visited[x] = True
    cycle.append(x)
    number = numbers[x]
    
    if visited[number]:
        if number in cycle:
            team += cycle[cycle.index(number):] 
        return
    else:
        dfs(number)

result = []
for _ in range(int(input())):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * n 
    team = [] 

    for i in range(1, n+1):
        if not visited[i]: 
            cycle = []
            dfs(i) 
            
    result.append(n - len(team)) 

print(*result,sep='\n')