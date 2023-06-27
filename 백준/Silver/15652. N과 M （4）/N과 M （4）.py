# By itertools
from itertools import combinations_with_replacement
N, M = map(int, input().split())
cs = combinations_with_replacement(range(1, N+1), M)
for c in cs:
    print(' '.join(map(str, c)))