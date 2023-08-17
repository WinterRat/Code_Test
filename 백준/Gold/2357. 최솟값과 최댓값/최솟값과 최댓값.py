from sys import stdin
input = stdin.readline

def init(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
        return tree[node]
    mid = (start + end) // 2
    left_min, left_max = init(node*2, start, mid)
    right_min, right_max = init(node*2+1, mid+1, end)
    tree[node] = (min(left_min, right_min), max(left_max, right_max))
    return tree[node]

def query(node, start, end, left, right):
    if left > end or right < start:
        return float('inf'), 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    left_min, left_max = query(node*2, start, mid, left, right)
    right_min, right_max = query(node*2+1, mid+1, end, left, right)
    return min(left_min, right_min), max(left_max, right_max)

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [(0, 0)] * (4*N)

init(1, 0, N-1)
result = []
for _ in range(M):
    a, b = map(int, input().split())
    result.append(query(1, 0, N-1, a-1, b-1))
    
for c in result:
    print(f'{c[0]} {c[1]}')