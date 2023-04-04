from sys import stdin
from collections import deque

input = stdin.readline

def operate(lst, i, j, k):
    # 0부터 인덱스니까 i-1부터 j-1까지 접근하기위해
    temp = lst[i - 1 : j]
    # rotate() deque method로 양수면 오른쪽회전 음수면 왼쪽 회전함
    temp = deque(temp)
    temp.rotate(j - k +1 )

    lst[i - 1 : j] = list(temp)
    return lst

def main() :
    N,M = map(int, input().split())
    lst = [i for i in range(1,N+1)] # 0 인덱스부터 채워짐
    for _ in range(M) :
        i,j,k = map(int, input().split())
        lst = operate(lst, i, j, k)

    print(" ".join(map(str, lst)))
    
if __name__ == "__main__":
    main()