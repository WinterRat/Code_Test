from sys import stdin
input=stdin.readline

n = int(input())
l=[]

for i in range(n):
    l.append(int(input()))

for i in sorted(l):
    print(i)