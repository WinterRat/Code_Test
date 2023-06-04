from sys import stdin

input = stdin.readline

def solve(data):
    stack = []
    result = 0

    for i in range(len(data)):
        if data[i] == '(':  # 파이프or레이저 시작
            stack.append('(')
        else:  # 파이프or 레이저 끝
            if data[i-1] == '(':  # 레이저일때
                stack.pop()  # 레이저의 시작 제거
                result += len(stack)  # 스택의 크기(현재까지 누적된 파이프 개수)만큼 조각 생성
            else:  # 파이프끝일때
                stack.pop()  # 파이프의 시작 제거
                result += 1  # 파이프 하나가 끝났으므로 조각이 하나 생성
    return result

data = input().strip()
print(solve(data))