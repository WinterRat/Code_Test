from sys import stdin
input = stdin.readline

N = int(input())
M = int(input())
S = input()

count = 0
length = 0
id = 1

while id < M - 1:
    if S[id-1] == 'I' and S[id] == 'O' and S[id+1] == 'I':
        length += 1
        if length == N:
            count += 1
            length -= 1
        id += 2
    else:
        length = 0
        id += 1

print(count)