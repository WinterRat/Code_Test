from sys import stdin

def main():
    count = 0
    N = int(stdin.readline())

    for _ in range(N):
        input_stack = list(stdin.readline().strip())
        find_stack = []

        for char in input_stack:
            if find_stack and find_stack[-1] == char:
                find_stack.pop()
            else:
                find_stack.append(char)
        # 이게 조금더 파이써닉함 len = 0 대신
        if not find_stack:
            count += 1

    print(f'{count}')

if __name__ == "__main__":
    main()
