def solution(my_strings, parts):
    answer = ''
    
    for i in range(len(parts)):
        for j in range(len(my_strings)):
            s = parts[i][0]
            e = parts[i][1] + 1
            
            if i == j:
                answer += my_strings[j][s:e]
            
    return answer