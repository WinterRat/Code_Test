from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def solve(start_row, start_col):
    counts = [0, 0] 
    for i in range(start_row, start_row + 8):
        for j in range(start_col, start_col + 8):
            if (i + j) % 2 == 0:
                if board[i][j] != 'B': 
                    counts[0] += 1
                if board[i][j] != 'W': 
                    counts[1] += 1
            else:
                if board[i][j] != 'W':  
                    counts[0] += 1
                if board[i][j] != 'B':  
                    counts[1] += 1
    return min(counts)

min_count = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        min_count = min(min_count, solve(i, j))

print(min_count)