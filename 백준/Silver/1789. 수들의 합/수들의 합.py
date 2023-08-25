S = int(input())

sum_ = 0
n = 0

while sum_ + (n + 1) <= S:
    n += 1
    sum_ += n

print(n)