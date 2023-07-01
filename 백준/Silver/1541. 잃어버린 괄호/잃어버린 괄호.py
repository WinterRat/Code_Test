inp = input().split('-')
total = 0

for num in inp[0].split('+'):
    total += int(num)

for i in inp[1:]:
    for num in i.split('+'):
        total -= int(num)

print(total)