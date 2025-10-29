def solution(arr):
    answer = []
    
    # 순회를 해
    # 앞에거랑 같니? 그럼 너 out
    cmp1 = [-1]
    cmp1 += arr
    
    n = len(cmp1)
    
    for i in range(1, n):
        if cmp1[i] != cmp1[i-1]:
            answer.append(cmp1[i])
    
    return answer