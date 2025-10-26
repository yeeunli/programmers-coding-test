def solution(str_list):
    
    if "l" not in str_list and "r" not in str_list:
        return []
    else:
        for i in str_list:
            if i == "l":
                return str_list[:str_list.index(i)]
            elif i == "r":
                return str_list[str_list.index(i)+1:]
            
    return answer