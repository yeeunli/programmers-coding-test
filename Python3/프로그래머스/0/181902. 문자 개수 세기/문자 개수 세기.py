from collections import Counter

def solution(my_string):
    answer = [0 for i in range(52)]
    arr_num = []
    
    for i in range(len(my_string)):
        if 'a' <= my_string[i] <= 'z':
            arr_num.append(ord(my_string[i])-97+26)
        if 'A' <= my_string[i] <= 'Z':
            arr_num.append(ord(my_string[i])-65)
    
    arr_num = Counter(arr_num).most_common()
    
    for k, v in arr_num:
        answer[k] = v
        
    return answer