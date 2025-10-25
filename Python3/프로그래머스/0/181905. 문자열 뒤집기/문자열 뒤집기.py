def solution(my_string, s, e):
    
    reverse_word = reversed(my_string[s:e+1])
    
    # reversed() 함수는 결과를 반환하지 않기 때문에 join()으로 문자열로 변환
    # 같은 타입끼리 + 연산 가능해짐
    return my_string[:s] + ''.join(reverse_word) + my_string[e+1:]

    # return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]