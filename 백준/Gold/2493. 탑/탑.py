from sys import stdin

def func_solve(N, input_list):
    index_list = [0] * N
    stack = []

    for i, value in enumerate(input_list):
        while stack and input_list[stack[-1]] < value:
            stack.pop()
        if stack :
            index_list[i] = stack[-1] + 1 
        else :  
            index_list[i]== 0
        stack.append(i)

    return index_list

def main():
    N = int(input())
    input_list = list(map(int, stdin.readline().split()))
    result = func_solve(N, input_list)

    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()