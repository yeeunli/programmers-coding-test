def solution(numbers, n):
    num = 0
    
    for i in numbers:
        if num <= n:
            num += i
            
    return num