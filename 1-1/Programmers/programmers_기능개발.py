def solution(progresses, speeds):
    lst = []
    day = 1
    answer = []
    for num in range(len(progresses)):
        while progresses[num]+speeds[num]*day<100:
            day += 1
        else:
            lst.append(day)
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            lst[i+1] = lst[i]
    lst1 = list(set(lst))
    lst1.sort()
    for i in lst1:
        answer.append(lst.count(i))
    return answer
print(solution([93,30,55],[1,30,5]))
