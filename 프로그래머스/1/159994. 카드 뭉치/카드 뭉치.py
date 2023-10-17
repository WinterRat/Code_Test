def solution(cards1, cards2, goal):
    answer = 'Yes'
    i, j = 0, 0
    
    for word in goal:
        if i < len(cards1) and word == cards1[i]:
            i += 1
        elif j < len(cards2) and word == cards2[j]:
            j += 1
        else:
            return "No"
        
    return answer