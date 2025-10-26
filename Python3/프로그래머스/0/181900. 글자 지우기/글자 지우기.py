def solution(my_string, indices):
    lst = list(my_string)
    
    for i in indices:
        lst[i] = ""
        
    return "".join(lst)