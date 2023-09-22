from sys import stdin

input = stdin.readline

N = int(input())
ice = list(map(int, input().split()))
ice.sort()

answer = float('inf')

for i in range(N):
    for j in range(i + 1, N):
        target = ice[i] + ice[j]
        l, r = 0, N - 1
        while l < r:

            if l == i or l == j:
                l += 1
                continue
            if r == i or r == j:
                r -= 1
                continue

            curr_sum = ice[l] + ice[r]
            diff = curr_sum - target
            if diff == 0:
                print(0)
                exit(0)
            else:
                answer = min(answer, abs(diff))
                if diff < 0:
                    l += 1
                else:
                    r -= 1

print(answer)