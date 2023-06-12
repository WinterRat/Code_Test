from sys import stdin

input = stdin.readline
N = int(input())
cost = [[0]*3 for _ in range(N)]

for i in range(N):
    cost[i] = list(map(int, input().split()))

# 빨초파 N개
for i in range(1, N):
    # i번째 집을 빨간색, 이전 집을 초록색 혹은 파란색으로 칠했을 때의 최소비용 더하기
    cost[i][0] += min(cost[i-1][1], cost[i-1][2]) # i-1번째 집이 초록색 혹은 파란색일 때의 비용 중 작은 비용 선택

    # i번째 집을 초록색, 이전 집을 빨간색 혹은 파란색으로 칠했을 때의 최소비용 더하기
    cost[i][1] += min(cost[i-1][0], cost[i-1][2]) # i-1번째 집이 빨간색 혹은 파란색일 때의 비용 중 작은 비용 선택

    # i번째 집을 파란색, 이전 집을 빨간색 혹은 초록색으로 칠했을 때의 최소비용 더하기
    cost[i][2] += min(cost[i-1][0], cost[i-1][1]) # i-1번째 집이 빨간색 혹은 초록색일 때의 비용 중 작은 비용 선택
print(min(cost[N-1]))