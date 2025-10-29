from collections import Counter
def solution(nums):
    answer = 0
    key_arr = []
    
    # counter 결과: 인덱스가 len(nums) // 2까지의 값의 개수 출력    
    cnt_num = Counter(nums)
    
    for key in cnt_num:
        key_arr.append(key)
    
    return len(key_arr[:len(nums) // 2])