def solution(my_string):
    answer = []
    
    # 문자열에 숫자만 있는가 - isdecimal() ⊂ isdigit() ⊂ isnumeric()
            # isdecimal() - int()로 변환 가능한 기본 숫자(0-9)
            # isdigit() - 숫자처럼 생겼다면 다 가능 ex. 제곱/첨자 숫자
            # isnumeric() - 숫자를 나타내는 문자도 가능 ex. 분수, 로마 숫자 등 숫자 값을 나타내는 모든 유니코드 문자
    # 문자열에 문자만 있는가 - isalpha()
    # 문자열이 수와 문자로 구성되어 있는가 - isalnum()
    
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
            
    return sorted(answer)