from sys import stdin

input = stdin.readline

MOD = 1000000007

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(8)) % MOD for j in range(8)] for i in range(8)]

def matpow(A, p):
    if p == 1:
        return A
    if p % 2:
        return matmul(A, matpow(A, p-1))
    half_pow = matpow(A, p//2)
    return matmul(half_pow, half_pow)

D = int(input())

adj = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

result = matpow(adj, D)

print(result[0][0])