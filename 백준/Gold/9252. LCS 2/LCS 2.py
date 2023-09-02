from sys import stdin
input = stdin.readline

a = input()
b = input()

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

result = []
i, j = len(a), len(b)
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        result.append(a[i - 1])
        i -= 1
        j -= 1

print(dp[len(a)][len(b)]-1)
print(''.join(reversed(result)))