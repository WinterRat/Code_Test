from sys import stdin

input =  stdin.readline

def count(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    # 1
    if n >= 1:
        dp[1] = 1
    # 11, 2
    if n >= 2:
        dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]

def main():
    pr_list = []
    T = int(input())
    for _ in range(T):
        n = int(input())
        pr_list.append(count(n))
        
    for i in pr_list:
        print(i)
        
if __name__ == "__main__":
    main()