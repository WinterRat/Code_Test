from sys import stdin

nums = []
for i in range(9):
    nums.append(int(stdin.readline()))

max_value = max(nums)
max_index = nums.index(max_value) + 1

print(max_value)
print(max_index)