def solution(num_list):
    sum_odd = 0
    sum_else = 0
    
    for i, v in enumerate(num_list):
        if i % 2 == 0:
            sum_odd += v
        else:
            sum_else += v
    
    return max(sum_odd, sum_else)