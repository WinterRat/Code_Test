from sys import stdin
input = stdin.readline

r, c = map(int, input().strip().split())
grid = [list(input().strip()) for _ in range(r)]
# 다이아몬드의 왼쪽 하단 방향, 오른쪽 하단 방향을 추적 2차원 배열 초기화
left_d = [[0]*c for _ in range(r)]
right_d = [[0]*c for _ in range(r)]
max_dia = 0 # 가장 큰 다이아 크기 저장

for i in range(r):
    for j in range(c):
        if grid[i][j] == '0':
            left_d[i][j] = 0
            right_d[i][j] = 0
        else:
            left_d[i][j] = 1
            right_d[i][j] = 1

# ld와 rd 배열을 업데이트. gird를 거꾸로 확인.
for i in range(r-2, -1, -1):
    for j in range(c):
        if left_d[i][j] == 1 and j != 0:
            left_d[i][j] += left_d[i+1][j-1]
        if right_d[i][j] == 1 and j != c-1:
            right_d[i][j] += right_d[i+1][j+1]

# ld와 rd 배열에서 각 위치에서 가능한 최대 다이아몬드 크기를 확인하고, res 값을 업데이트
for i in range(r):
    for j in range(c):
        if left_d[i][j] != 0 and right_d[i][j] != 0:
            max_dia = max(max_dia, 1)
            if left_d[i][j] != 1 and right_d[i][j] != 1:
                n = min(left_d[i][j], right_d[i][j])
                while n > 1:
                    if right_d[i+n-1][j-n+1] >= n and left_d[i+n-1][j+n-1] >= n:
                        max_dia = max(max_dia, n)
                    n -= 1
print(max_dia)