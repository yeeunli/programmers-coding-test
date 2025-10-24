def solution(numbers, k):
    answer = 0
    extend_arr = numbers
    
    # 주어진 배열을 k에 맞게 늘린다
    if len(numbers) < (k * 2):
        extend_arr = numbers * ((k * 2) // len(numbers) + 1)
    
    # 해당 요소를 추출한다
    return extend_arr[(k * 2) - 2]