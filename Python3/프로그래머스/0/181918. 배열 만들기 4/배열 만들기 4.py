def solution(arr):
    stk = []
    i = 0
    
    while (i < len(arr)):
        
        # stk 빈 배열인 경우
        if stk == []:
            stk.append(arr[i])
            i += 1

        # stk 원소 들어있는 경우
        else:
            # stk 마지막 원소 < arr[i]
            # stk 맨 뒤에 arr[i] 추가, i +1
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1

            # else
            # stk 맨 뒤 제거
            else:
                stk.pop(-1)
            
    return stk