import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MOD = 1000000007

def matmul(A, B):
    return (
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    )

def matpow(matrix, n):
    result = [[1, 0], [0, 1]]
    while n:
        if n % 2:
            result = matmul(result, matrix)
        matrix = matmul(matrix, matrix)
        n //= 2
    return result

def fibonacci(n):
    if n == 0: 
        return 0
    matrix = [[1, 1], [1, 0]]
    result = matpow(matrix, n-1)
    return result[0][0]

n = int(input())
print(fibonacci(n))