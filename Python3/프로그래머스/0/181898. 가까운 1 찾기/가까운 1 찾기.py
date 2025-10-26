def solution(arr, idx):
    answer = []
    
    for i in range(len(arr)):
        if arr[i] == 1 and idx <= i:
            answer.append(i)
    
    if len(answer) == 0:
        answer.append(-1)
        
    return sorted(answer)[0]