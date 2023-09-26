from sys import stdin
input = stdin.readline

def matrix_mul(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def matrix_pow(A, B):
    n = len(A)
    if B == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] %= 1000
        return A
    elif B % 2:
        return matrix_mul(A, matrix_pow(A, B-1))
    else:
        half_pow = matrix_pow(A, B//2)
        return matrix_mul(half_pow, half_pow)

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = matrix_pow(matrix, b)

for row in result:
    print(' '.join(map(str, row)))