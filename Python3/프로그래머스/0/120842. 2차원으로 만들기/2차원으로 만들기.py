def solution(num_list, n):
    answer = []
    
    # 슬라이싱을 이용하자
    
    # for i in num_list[::n]:
    #     x = num_list.index(i)
    #     answer.append(num_list[x:x+n])
    
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i+n])
    
    return answer