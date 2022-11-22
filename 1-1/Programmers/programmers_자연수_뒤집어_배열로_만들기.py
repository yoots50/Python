def solution(n):
    lst = list(str(n))
    answer = []
    for l in lst:
        l = int(l)
        answer.append(l)
    answer.reverse()
    return answer
