def solution(my_string, s, e):
    
    reverse_word = my_string[s:e+1]
    
    answer = my_string[:s] + reverse_word[::-1] + my_string[e+1:]
    
    return answer