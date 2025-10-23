def solution(arr, queries):
    answer = []
    
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        
        for i in range(s, e+1):
            if i == 0:
                arr[i] += 1
            else:
                for mul in range(len(arr)):
                    if k * mul == i:
                        arr[i] += 1
    
    return arr