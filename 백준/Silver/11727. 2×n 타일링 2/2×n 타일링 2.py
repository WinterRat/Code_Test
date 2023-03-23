def find_dp(n):
    dp = [0] * (n+1) # 먼저 배열 초기화
    dp[0] = 1 # 나중에 출력은 안하지만 dp 계산시 필요 따라서 값 필요
    dp[1] = 1 # 2*1 하나만 존재

    for i in range(2, n+1):
        dp[i] = dp[i-1] + 2 * dp[i-2] # n이 2일때 3가지, n이 3일때 양옆으로 이동해서 전에꺼 똑같이 찍는 *2, 전에꺼에서 하나더 추가해서 한경우 한가지 더함
        dp[i] %= 10007

    return dp[n]

def main():
    n = int(input().strip())
    print(find_dp(n))

if __name__ == "__main__":
    main()