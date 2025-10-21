def solution(left, right):
    answer = 0

    # 주어진 수를 주어진 수 내에서 1부터 나눈다
    for i in range(left, right + 1):
        
        factor = []
        
        # 약수를 찾아서 factor 배열에 넣는다
        for j in range(1, i+1):
            
            if i % j == 0:
                factor.append(j)

        # 약수의 개수가 짝수면 주어진 수를 더하고
        # 약수의 개수가 홀수면 주어진 수를 뺀다
        if len(factor) % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer