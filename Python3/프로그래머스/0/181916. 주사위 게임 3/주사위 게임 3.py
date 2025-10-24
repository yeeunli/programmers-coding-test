from collections import Counter

def solution(a, b, c, d):
    answer = 0
    counts = Counter([a, b, c, d]).most_common()
    
    if counts[0][1] == 4:
        answer = 1111 * counts[0][0]
        
    elif counts[0][1] == 3:
        answer = (10 * counts[0][0] + counts[1][0]) ** 2
        
    elif counts[0][1] == 2:
        if counts[1][1] == 1:
            answer = counts[1][0] * counts[2][0]
        else:
            answer = (counts[0][0] + counts[1][0]) * (abs(counts[0][0] - counts[1][0]))
            
    else:
        answer = min(a, b, c, d)
    
    return answer