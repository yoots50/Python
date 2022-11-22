def solution(id_list, report, k):
    set1 = set() #신고 횟수가 k번 이상인 사람들
    lst = [] #신고 당한 사람
    lst1 = [] #신고한 사람
    report = list(set(report))
    for idx in range(len(report)):
        a = report[idx].split(' ')[1]
        b = report[idx].split(' ')[0]
        lst.append(a)
        lst1.append(b)
        if lst.count(a) > 1:
            set1.add(a)
    print(lst)
    print(lst1)
    print(set1)
    answer = []
    lst2 = [] #메일 받을 사람
    for idx in range(len(lst)):
        if lst[idx] in set1:
            lst2.append(lst1[idx])
    for i in id_list:
        answer.append(lst2.count(i))
    return answer
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
