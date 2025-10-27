def solution(array, n):
    answer = []
    result = 0
    
    for i in array:
        answer.append(abs(i - n))
    
    i = answer.index(min(answer))
    result = array[i]
    
    for k in range(i+1, len(answer)):
        if min(answer) == answer[k]:
            result = min(array[i], array[k])
            
    return result