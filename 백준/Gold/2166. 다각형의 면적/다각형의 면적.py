from sys import stdin

input = stdin.readline

vertex = []

def solve(N):
    sum = 0
    x1, y1 = vertex[0]
    for i in range(1, N-1):
        x2, y2  = vertex[i]
        x3, y3  = vertex[i+1]
        sum += sinbalggeun(x1,y1,x2,y2,x3,y3)
    return abs(sum)/2
        
def sinbalggeun(x1,y1,x2,y2,x3,y3):
    A = x1*y2 + x2*y3 + x3*y1
    B = x2*y1 + x3*y2 + x1*y3
    return A-B   
    
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    vertex.append((x, y))
print(f"{solve(N):.1f}")