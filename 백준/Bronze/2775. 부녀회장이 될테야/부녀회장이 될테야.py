from sys import stdin

input = stdin.readline

T = int(input())
result = []
apartment = [[0]*14 for _ in range(15)] 

#0층 바로넣고
for i in range(14):
    apartment[0][i] = i + 1

# 나머지는 주민수 합
for i in range(1, 15):
    for j in range(14):
        apartment[i][j] = apartment[i-1][j] + apartment[i][j-1]

for _ in range(T):
    k = int(input())
    n = int(input())
    result.append(apartment[k][n-1])
    
print(*result,sep='\n')