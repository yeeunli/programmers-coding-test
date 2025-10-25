def solution(intStrs, k, s, l):
    answer = []
    
    for i in intStrs:
        
        slice_arr = int(i[s:s+l])
        
        if k < slice_arr:
            answer.append(slice_arr)
    
    return answer