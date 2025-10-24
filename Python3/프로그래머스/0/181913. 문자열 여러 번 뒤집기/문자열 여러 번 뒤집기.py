def solution(my_string, queries):
    
    for i in queries:
        
        extract_word = ''
        reverse_word = ''
        
        # 범위만큼 뽑는다
        for e_word in my_string[i[0]:i[1]+1]:
            extract_word += e_word
        
        # 뽑은 걸 뒤집는다
        for r_word in extract_word[::-1]:
            reverse_word += r_word
        
        # 뽑은 자리에 뒤집은 문자열을 넣는다
        answer = ''
        
        answer_first = my_string[:i[0]]
        answer_middle = reverse_word
        answer_last = my_string[i[1]+1:]
        
        answer = answer_first + answer_middle + answer_last
            
        # 다음 반복에서 문자열 갱신해서 적용한다
        my_string = answer
        
    return answer