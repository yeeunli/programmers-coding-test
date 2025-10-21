def solution(l, r):
    answer = []
    # num_to_str = ''
    
    for k in range(l, r+1):
        
#         num_to_str = str(k)
        
#         for i in num_to_str:
            
#             if k % 5 == 0:
#                 if i != '0' and i != '5':
#                     break
#                 else:
#                     answer.append(k)
        
        # 0과 5로만 이루어진 숫자를 찾자 
        if k % 5 == 0:
            if ('1' in str(k) or '2' in str(k) or 
                '3' in str(k) or '4' in str(k) or 
                '6' in str(k) or '7' in str(k) or 
                '8' in str(k) or '9' in str(k)):
                continue
            else:
                answer.append(k)
            
    if len(answer) == 0:
        answer = [-1]
        
    return answer