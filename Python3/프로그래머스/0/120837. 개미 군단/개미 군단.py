def solution(hp):
    answer = 0
    
    five = hp // 5
    three = (hp - 5 * five) // 3
    one = hp - (5 * five + 3 * three)
    
    answer = five + three + one
    
    return answer