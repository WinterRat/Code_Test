def solution(s):
    answer = []
    numbers = s.replace('},{', ',').replace('{', '').replace('}', '').split(',')

    count = {}
    for num in numbers:
        count[int(num)] = count.get(int(num), 0) + 1

    answer = [num[0] for num in sorted(count.items(), key=lambda x: x[1], reverse=True)]
    
    return answer