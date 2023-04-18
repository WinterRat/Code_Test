from sys import stdin

input = stdin.readline

t = int(input())

for i in range(t):
    result = input()
    a = 0
    b = 1
    for j in range(len(result)):
        if result[j] == 'O':
            a += b
            b += 1
        else:
            b = 1
    print(a)