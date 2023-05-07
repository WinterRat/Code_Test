import sys
input = sys.stdin.readline
def d(n):
    if v[n]:
        return False
    else :
        v[n] = True
    for a_n in g[n]:
        if not s[a_n] or d(s[a_n]):
            s[a_n] = n
            return True
    return False
N, M = map(int, input().split())
g = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)
s = [0] * (N+1)
c = 0
for i in range(1, N+1):
    v = [False] * (N+1)
    if d(i):
        c += 1
print(c//2)