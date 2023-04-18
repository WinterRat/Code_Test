from sys import stdin

input = stdin.readline

T = int(input())

for i in range(T):
    R, S = input().split()
    for j in S:
        print(j*int(R), end='')
    print()