def solution(n):
    answer = ''
    
    for i in range(1, n+1):
        
        # 홀수일 때 '수' 출력
        if i % 2 != 0:
            answer += '수'
            
        # 짝수일 때 '박' 출력
        else:
            answer += '박'
    
    return answer