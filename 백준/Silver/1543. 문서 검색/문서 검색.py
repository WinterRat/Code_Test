from sys import stdin

input = stdin.readline

def find(MS, to_find):
    count = 0
    idx = 0
    while idx <= len(MS) - len(to_find):
        if MS[idx:idx+len(to_find)] == to_find:
            count += 1
            idx += len(to_find)  # 찾은 문자열만큼 건너뛰기
        else:
            idx += 1

    return count

if __name__ == "__main__":
    MS = input().strip()
    to_find = input().strip()
    print(find(MS, to_find))