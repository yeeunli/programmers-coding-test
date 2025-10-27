def solution(array, commands):
    answer = []
    cpy = []
    
    for i, j, k in commands:
        cpy = array
        cpy = cpy[i-1:j]
        cpy.sort()
        answer.append(cpy[k-1])
    
    return answer