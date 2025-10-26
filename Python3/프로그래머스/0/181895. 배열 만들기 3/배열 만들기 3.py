def solution(arr, intervals):
    answer = []
    
    for s, e in intervals:
        
        # 리스트는 +로 이어붙이기가 가능하다
        answer += arr[s:e+1]
    
    return answer