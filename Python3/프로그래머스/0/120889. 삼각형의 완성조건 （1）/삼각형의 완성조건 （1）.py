def solution(sides):
    sides = sorted(sides)
    s, m, l = sides
    
    if l < s + m:
        return 1
    return 2