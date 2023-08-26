from sys import stdin
input = stdin.readline

min_val, max_val = map(int, input().split())
sv = [True] * (max_val - min_val + 1)
count = max_val - min_val + 1

for i in range(2, int(max_val ** 0.5) + 1):
    square = i * i
    start = (min_val + square - 1) // square

    for j in range(start * square, max_val + 1, square):
        if sv[j - min_val]:
            sv[j - min_val] = False
            count -= 1

print(count)