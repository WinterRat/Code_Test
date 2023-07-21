from sys import stdin
input = stdin.readline

def solve(N, num, stt):
    count = 0
    
    for i in range(N):
        # 0인덱스와 맨뒤는 양옆에 데이터 하나씩 없으므로 처리후
        # 지뢰가 있다는 가정하에 지뢰가 없는 경우로 제거 처리
        if i == 0:
            if num[0] != 0 and num[1] != 0:
                num[0] -= 1
                num[1] -= 1
                count += 1
        elif i == (N-1):
            if num[i] != 0 and num[i-1] != 0:
                num[i-1] -= 1
                num[i-2] -= 1
                count += 1
        else:
            if num[i-1] != 0 and num[i] != 0 and num[i+1] != 0:
                num[i-1] -= 1
                num[i] -= 1
                num[i+1] -= 1
                count += 1
            
    return count

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    num = list(map(int, input().strip()))
    stt = input().strip()
    result.append(solve(N, num, stt))
    
print(*result, sep='\n')
