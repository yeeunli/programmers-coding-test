def solution(my_string, queries):
    
    # 간단 버전을 알아보자
    
    # 문자열은 불변이기에 한 번 만들어진 문자열의 특정 부분 수정 불가
    # 따라서, 리스트로 변환하자
    answer = list(my_string)
    
    # 각 쿼리를 언패킹 적용하여 하나씩 꺼냄
    for s, e in queries:
        
        # 슬라이싱한 문자열을 뒤집어 할당
        answer[s:e+1] = answer[s:e+1][::-1]

    # 리스트에 하나씩 담겨있는 문자들을 하나의 문자열로 반환
    return ''.join(answer)
    
#     for i in queries:
        
#         extract_word = ''
#         reverse_word = ''
        
#         # 범위만큼 뽑는다
#         for e_word in my_string[i[0]:i[1]+1]:
#             extract_word += e_word
        
#         # 뽑은 걸 뒤집는다
#         for r_word in extract_word[::-1]:
#             reverse_word += r_word
        
#         # 뽑은 자리에 뒤집은 문자열을 넣는다
#         answer = ''
        
#         answer_first = my_string[:i[0]]
#         answer_middle = reverse_word
#         answer_last = my_string[i[1]+1:]
        
#         answer = answer_first + answer_middle + answer_last
            
#         # 다음 반복에서 문자열 갱신해서 적용한다
#         my_string = answer
        
    return answer