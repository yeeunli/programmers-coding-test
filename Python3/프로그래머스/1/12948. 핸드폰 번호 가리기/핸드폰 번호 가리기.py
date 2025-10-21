def solution(phone_number):
    answer = ''
    
#   문자열 맨 뒤에서 4자리 앞부터 반복문 순회
#   해당 문자열을 *로 변경
    for i in phone_number[:-4]:
        answer += '*'    
    
    return answer + phone_number[len(answer)::]