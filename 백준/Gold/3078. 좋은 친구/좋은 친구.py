import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().strip().split())
students = [len(input().strip()) for _ in range(n)]

#set
use_lengths = set(students)
deques = {length: deque() for length in use_lengths}

sum = 0

for i, length in enumerate(students):
    # 등수 높은 같은키 0 인덱스에 
    while deques[length] and i - deques[length][0] > k:
        deques[length].popleft()
        
    sum += len(deques[length])

    deques[length].append(i)

print(sum)