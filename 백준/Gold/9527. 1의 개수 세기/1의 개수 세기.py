from sys import stdin
input = stdin.readline

def count_ones(n):
    if n == 0:
        return 0

    # 이진 표현을 얻고, 최상위 비트의 인덱스를 구함
    binary = bin(n)[2:]
    highest_bit_index = len(binary) - 1

    # 최상위 비트 미만의 모든 비트들이 1이 될 수 있는 경우의 수
    ones_until_highest_bit = (1 << highest_bit_index) * highest_bit_index // 2

    # 최상위 비트부터 남은 숫자들의 1의 개수
    remaining_ones = n - (1 << highest_bit_index) + 1 + count_ones(n - (1 << highest_bit_index))

    return ones_until_highest_bit + remaining_ones


A, B = map(int, input().split())
print(count_ones(B) - count_ones(A - 1))