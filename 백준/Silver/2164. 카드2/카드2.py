from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
    queue.popleft()  
    queue.append(queue.popleft()) 

print(queue.pop())