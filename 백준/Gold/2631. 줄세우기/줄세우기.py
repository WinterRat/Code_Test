def solve(arr):
    lis = []
    for num in arr:
        if not lis or lis[-1] < num:
            lis.append(num)
        else:
            left, right = 0, len(lis) - 1
            while left <= right:
                mid = (left + right) // 2
                if lis[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            lis[left] = num
    return len(lis)

n = int(input())
children = [int(input()) for _ in range(n)]

print(n - solve(children))