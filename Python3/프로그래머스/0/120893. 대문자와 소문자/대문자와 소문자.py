def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i.isupper():
            # answer += chr(ord(i) + 32)
            answer += i.lower()
        else:
            # answer += chr(ord(i) - 32)
            answer += i.upper()
    
    return answer