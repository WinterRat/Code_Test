from sys import stdin

input = stdin.readline

word = input().strip().upper()
word_set = list(set(word))
count_list = []

for char in word_set:
    count = word.count(char)
    count_list.append(count)

max_count = max(count_list)

if count_list.count(max_count) > 1:
    print('?')
else:
    max_index = count_list.index(max_count)
    print(word_set[max_index])