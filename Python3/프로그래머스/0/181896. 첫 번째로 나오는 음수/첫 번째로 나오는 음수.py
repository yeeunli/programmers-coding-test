def solution(num_list):
    answer = []
    
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer.append(i)
        
    if len(answer) == 0:
        return -1
    return answer[0]