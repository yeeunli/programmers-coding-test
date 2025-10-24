def solution(balls, share):
    answer = 0
    print(factorial(balls))
    return factorial(balls) // (factorial(balls - share) * factorial(share))

def factorial(num):
    
    if num <= 1:
        return 1
    
    else:
        return num * factorial(num-1)