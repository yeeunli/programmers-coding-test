from math import factorial

def solution(n):
    answer = 0
    num = []
    
    for i in range(1, 11):
        if factorial(i) <= n:
            num.append(i)
    
    answer = sorted(num)[-1]
    return answer