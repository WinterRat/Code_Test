from sys import stdin
input = stdin.readline

N = int(input())
student = []
for _ in range(N):
    student.append(int(input()))

bulman = 0
student_sort = sorted(student)
for i in range(N-1,-1,-1):
    bulman += abs(i+1-student_sort[i])

print(bulman)