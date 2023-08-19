S = input().strip()
P = input().strip()

l_S, l_P = len(S), len(P)

dp = [1e9] * (l_P + 1)
dp[0] = 0

for i in range(1, l_P + 1):
    for j in range(l_S):
        k = 0
        while i + k <= l_P and j + k < l_S and P[i + k - 1] == S[j + k]:
            k += 1
        dp[i + k - 1] = min(dp[i + k - 1], dp[i - 1] + 1)

print(dp[l_P])