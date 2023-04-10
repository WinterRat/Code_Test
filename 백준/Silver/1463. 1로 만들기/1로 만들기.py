from sys import stdin
input = stdin.readline

def operate(n):
    dp = [0] * (n + 1)  

    for i in range(2, n + 1):
        # 이전 값에서 1 뺄셈 연산만 사용한 경우
        dp[i] = dp[i - 1] + 1
        
        # 2로 나누어 떨어질 때, 이전 값과 비교 더 작은 값 저장
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        
        # 3으로 나누어 떨어질 때, 이전 값과 비교 더 작은 값 저장
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    return dp[n]

def main():
    n = int(input()) 
    print(operate(n))  

if __name__ == "__main__":
    main()