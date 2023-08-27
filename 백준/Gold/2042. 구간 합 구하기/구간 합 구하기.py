from sys import stdin

input = stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]

def sum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return sum(node * 2, start, (start + end) // 2, left, right) + sum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)

N, M, K = map(int, input().split())
arr = []
tree = [0] * (4 * N)
result = []

for _ in range(N):
    arr.append(int(input()))

init(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b - 1]
        arr[b - 1] = c
        update(1, 0, N - 1, b - 1, diff)
    else:
        result.append(sum(1, 0, N - 1, b - 1, c - 1))

print(*result, sep = '\n')