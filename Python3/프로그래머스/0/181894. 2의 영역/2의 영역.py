def solution(arr):
    answer = []
    idx_two = []
    
    # for문을 돌려서 2를 찾는다
    # 배열에 인덱스 값을 넣는다
    for i in range(len(arr)):
        if arr[i] == 2:
            idx_two.append(i)
    
    # 처음값과 마지막값을 슬라이싱으로 답을 반환한다
    # 2가 없으면 -1을 넣어두자
    if len(idx_two) == 0:
        answer = [-1]
    elif len(idx_two) == 1:
        answer.append(arr[idx_two[0]])
    else:
        s = idx_two[0]
        e = idx_two[-1] + 1
        answer = arr[s:e]
        
    return answer