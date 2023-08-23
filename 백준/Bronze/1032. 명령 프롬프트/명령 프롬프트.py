n = int(input())
f = [input() for _ in range(n)]

result = ""

for i in range(len(f[0])):
    same = True
    for j in range(1, n):
        if f[j][i] != f[0][i]:
            same = False
            break

    if same:
        result += f[0][i]
    else:
        result += '?'

print(result)