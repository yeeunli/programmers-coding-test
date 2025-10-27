# def solution(array, n):
#     answer = []
#     result = 0
    
#     for i in array:
#         answer.append(abs(i - n))
    
#     i = answer.index(min(answer))
#     result = array[i]
    
#     for k in range(i+1, len(answer)):
#         if min(answer) == answer[k]:
#             result = min(array[i], array[k])
            
#     return result

def solution(array, n):
    
    # List Comprehension: [ (결과 표현식) (반복문) ]
    tmp = [(abs(num-n), num) for num in array]
    
    # 첫 번째 요소를 기준으로 정렬
    # but, 같다면 두 번째 요소로 정렬
    tmp.sort()
    
    return tmp[0][1]