import math

seconds = 7 * 24 * 60 * 60

N = int(input().strip())

factorial = math.factorial(N)

weeks = factorial // seconds

print(weeks)