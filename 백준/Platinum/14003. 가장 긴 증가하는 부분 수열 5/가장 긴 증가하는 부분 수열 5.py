from sys import stdin
from bisect import bisect_left
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

V = [A[0]]
V_index = [0 for _ in range(N)]  # 각 위치에서 선택된 LIS의 마지막 요소의 인덱스를 저장할거임.
result = [0 for _ in range(N)]

for i in range(1,N):
    if A[i] > V[-1]:
        V.append(A[i])
        V_index[i] = len(V) - 1 # 새 요소가 추가될 때마다 해당 요소의 인덱스를 저장함.
    else:
        idx = bisect_left(V, A[i])
        V[idx] = A[i]
        V_index[i] = idx # 기존 요소가 갱신될 때마다 해당 요소의 인덱스를 저장함.

print(len(V))

idx = len(V) - 1
for i in range(N-1, -1, -1):
    if V_index[i] == idx:
        result[idx] = A[i]
        idx -= 1

for i in range(len(V)):
    print(result[i], end=' ')