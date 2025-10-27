def solution(arr, queries):
    
    # for s, e in queries:
    #     for i in range(len(arr)):
    #         if s <= i <= e:
    #             arr[i] += 1
    
    # 배수든 범위든 우선 슬라이싱을 생각하자
    for s, e in queries:
        for i in range(s, e+1):
            arr[i] += 1
                
    return arr