from sys import stdin

input = stdin.readline
dx = [-1, 0, 0, 0, 1]
dy = [0, -1, 0, 1, 0]


def flip(a, x, y):
    for i in range(5):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10:
            if a[nx][ny] == '#':
                a[nx][ny] = 'O'
            else:
                a[nx][ny] = '#'

def solve(a):
    ans = -1
    for nowon in range(1<<10):
        b = [a[i][:] for i in range(10)]
        cnt = 0
        for i in range(10):
            if (nowon & (1<<i)) > 0:
                flip(b, 0, i)
                cnt += 1
        for i in range(1, 10):
            for j in range(10):
                if b[i-1][j] == 'O':
                    flip(b, i, j)
                    cnt += 1
        if all(b[i][j] == '#' for i in range(10) for j in range(10)):
            if ans == -1 or ans > cnt:
                ans = cnt
    return ans

a = [list(input().strip()) for _ in range(10)]
print(solve(a))