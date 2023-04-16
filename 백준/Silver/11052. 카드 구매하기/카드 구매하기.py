from sys import stdin

input = stdin.readline

def main():
    N = int(input())
    max_price = [0] + list(map(int, input().split()))

    dp = [0] * (N + 1)
    dp[1] = max_price[1]

    for i in range(2, N + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i-j] + max_price[j])

    print(dp[N])

if __name__ == "__main__":
    main()