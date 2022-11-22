def solution(d, budget):
    d.sort()
    sum = 0
    answer = 0
    while True:
        if len(d) == 0:
            return answer
        else:
            sum += min(d)
            if sum > budget:
                break
            del d[0]
            answer += 1
    return answer

