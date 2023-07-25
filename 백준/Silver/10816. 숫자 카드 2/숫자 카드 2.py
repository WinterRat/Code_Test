from sys import stdin

input = stdin.readline
  
N = int(input())
nums = list(map(int, input().strip().split()))
M = int(input())
search = list(map(int,input().strip().split()))
dic = {}
for i in nums:
    if i not in dic:
        dic[i] = 1
    else:
        count = int(dic[i])
        dic[i] = count+1

for c in search:
    if c in dic:
        print(dic[c],end=' ')
    else :
        print(0,end=' ')
    