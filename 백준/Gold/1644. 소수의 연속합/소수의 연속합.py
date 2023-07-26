from sys import stdin
input = stdin.readline

# n 까지 수중에 소수만 찾아서 반환
def prime_filter(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]
# 투 포인터로 count
def prime_sum(n):
    primes = prime_filter(n)
    start, end, p_sum, cnt = 0, 0, 0, 0

    while True:
        if p_sum >= n:
            if p_sum == n:
                cnt += 1
            p_sum -= primes[start]
            start += 1
        elif end == len(primes):
            break
        else:
            p_sum += primes[end]
            end += 1
    return cnt

N = int(input())
print(prime_sum(N))