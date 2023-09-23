from sys import stdin

input = stdin.readline

def solve(cases):
    n, *heights = cases
    stack = []  
    max_area = 0
    
    for i in range(n):
        # 스택에 있으면 그게 현재 높이
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    #  스택에 바 유지
    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area

result = []
while True:
    cases = list(map(int, input().split()))
    if cases[0] == 0:
        break
    else:
        result.append(solve(cases))

for r in result:
    print(r)