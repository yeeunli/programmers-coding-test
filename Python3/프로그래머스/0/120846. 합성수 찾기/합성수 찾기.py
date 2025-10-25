def solution(n):
    answer = []
    
    for i in range(1, n+1):
        
        num = []
        
        for j in range(1, n+1):
            if i % j == 0:
                num.append(j)
                
        if len(num) >= 3:
            answer.append(i)
            
    return len(answer)