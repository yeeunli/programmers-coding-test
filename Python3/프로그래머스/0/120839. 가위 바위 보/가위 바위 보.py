def solution(rsp):
    answer = ''
    
    list_rsp = list(rsp)
    
    for i in list_rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    
    return answer