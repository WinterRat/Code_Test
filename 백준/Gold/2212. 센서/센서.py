from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

if N <= K :
    print(0)

else : 
    dist = []
    for i in range(1, N):
        dist.append(sensors[i] - sensors[i-1])
    dist.sort()

    for _ in range(K-1):
        dist.pop()

    print(sum(dist))