def solution(my_string, is_suffix):
    
    if is_suffix in arr_suffix(my_string):
        return 1
    return 0

def arr_suffix(my_string):

    result = []
    
    for i in range(len(my_string)):
        result.append(my_string[i:])
        
    return sorted(result)