def solution(s):
    answer = 0
    num = s.split(' ')
    
    for i in range(len(num)):
        
        if num[i].isnumeric() or '-' in num[i]:
            answer += int(num[i])
            
        if num[i] == 'Z':
            answer -= int(num[i-1])
    
    # 본래 의도
    # num + ' Z' 를 빈 문자열로 변환
    # 공백을 구분자로 하여 각 숫자의 합 구하기
    
    return answer