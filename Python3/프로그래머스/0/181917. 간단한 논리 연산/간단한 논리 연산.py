def solution(x1, x2, x3, x4):
    
    # 기본식 정의
    return logical_and(logical_or(x1, x2), logical_or(x3, x4))

def logical_or(a, b):
    return (a or b)

def logical_and(a, b):
    return (a and b)