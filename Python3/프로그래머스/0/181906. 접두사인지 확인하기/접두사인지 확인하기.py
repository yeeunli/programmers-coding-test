def solution(my_string, is_prefix):
    arr_prefix = []
    
    for i in range(len(my_string)):
        arr_prefix.append(my_string[:i])
    
    if is_prefix in arr_prefix:
        return 1
    return 0