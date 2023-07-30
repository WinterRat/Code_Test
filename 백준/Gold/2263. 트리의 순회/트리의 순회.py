import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
n = int(input())
inord = list(map(int, input().split()))
postord = list(map(int, input().split()))
pos = [0]*(n+1)
for i in range(n):
    pos[inord[i]] = i
    
def solve(in_start, in_end, p_start, p_end):
    if(in_start > in_end) or (p_start > p_end):
        return
    parents = postord[p_end]
    print(parents, end=" ")

    left = pos[parents] - in_start
    right = in_end - pos[parents]

    solve(in_start, in_start+left-1, p_start, p_start+left-1)
    solve(in_end-right+1, in_end, p_end-right, p_end-1)

solve(0, n-1, 0, n-1)