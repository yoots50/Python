def solution(n, arr1, arr2):
    lst1 = []
    lst2 = []
    lst = []
    cnt = 0
    temp = ""
    answer = []
    for ar1 in arr1:
        for i in range(n-1,-1,-1):
            lst1.append(ar1//2**i)
            ar1 = ar1%2**i
    for ar2 in arr2:
        for i in range(n-1,-1,-1):
            lst2.append(ar2//2**i)
            ar2 = ar2%2**i
    for idx in range(len(lst1)):
        lst.insert(idx, lst1[idx]+lst2[idx])
    for idx in range(len(lst)):
        if lst[idx] == 1 or lst[idx] == 2:
            lst[idx] = "#"
        else:
            lst[idx] = " "
    for idx in range(n):
        idx = n*(idx)
        while cnt < n:
            temp = temp + lst[idx]
            cnt += 1
            idx += 1
        answer.append(temp)
        temp = ""
        cnt = 0
    return answer
print(solution(5,[9,20,28,18,11],[30,1,21,17,28]))

