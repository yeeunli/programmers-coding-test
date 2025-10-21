def solution(arr):
    answer = []
    min_num = min(arr)
    
#   배열에서 최소수를 제거
    for i in arr:
        if i != min_num:
            answer.append(i)
            
#   배열에 원소가 하나라면 -1 리턴
    if len(arr) == 1:
        answer.append(-1)
    
    return answer