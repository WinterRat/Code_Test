from sys import stdin

input = stdin.readline

N = int(input())
MOD = 1000000000

# dp[length][last_digit][used_mask]
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N + 1)]

for i in range(1, 10):  # 0으로 시작 안되니까
    dp[1][i][1 << i] = 1  

for length in range(2, N + 1):
    for last_digit in range(10): # 0~9
        for used_mask in range(1024): # 0~9 2^10
            if last_digit == 0:
                dp[length][0][used_mask | (1 << 0)] += dp[length - 1][1][used_mask]
                dp[length][0][used_mask | (1 << 0)] %= MOD
            elif last_digit == 9:
                dp[length][9][used_mask | (1 << 9)] += dp[length - 1][8][used_mask]
                dp[length][9][used_mask | (1 << 9)] %= MOD
            else:
                dp[length][last_digit][used_mask | (1 << last_digit)] += dp[length - 1][last_digit - 1][used_mask]
                dp[length][last_digit][used_mask | (1 << last_digit)] += dp[length - 1][last_digit + 1][used_mask]
                dp[length][last_digit][used_mask | (1 << last_digit)] %= MOD

result = 0
for i in range(10):
    result += dp[N][i][1023]
    result %= MOD

print(result)