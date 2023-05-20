from sys import stdin

input = stdin.readline

def sugar(n):
    count = 0
    while n >= 0:
        if n % 5 == 0:
            count += n // 5
            return count
        n -= 3
        count += 1

    return -1

N = int(input())
print(sugar(N))