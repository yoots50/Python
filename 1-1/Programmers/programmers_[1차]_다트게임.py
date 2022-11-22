def solution(dartResult):
    lst = []
    isFirst = True
    Firstisstar = False
    dartList = list(dartResult)
    deleted_idx = ""
    delcnt = 0
    for idx in range(len(dartList)):
        if idx == deleted_idx:
            pass
        elif idx >= len(dartList) - delcnt:
            pass
        elif dartList[idx].isdigit():
            if dartList[idx] == "1":
                if dartList[idx+1] == "0":
                    num = 10
                    deleted_idx = idx+1
                    del dartList[idx+1]
                    delcnt += 1
                    if dartList[idx+1] == "S":
                        pass
                    if dartList[idx+1] == "D":
                        num **= 2
                    if dartList[idx+1] == "T":
                        num **= 3
                    if Firstisstar:
                        num *= 2
                    Firstisstar = False
                    lst.append(num)
                else:
                    num = 1
            else:
                num = int(dartList[idx])
        elif dartList[idx].isalpha():
            if dartList[idx] == "S":
                pass
            if dartList[idx] == "D":
                num **= 2
            if dartList[idx] == "T":
                num **= 3
            if Firstisstar:
                num *= 2
                Firstisstar = False
            lst.append(num)
        else:
            if dartList[idx] == "*" and not isFirst:
                if len(lst) < 2:
                    lst[0] = lst[0]*2
                else:
                    for idx in [-1,-2]:
                        idx = int(idx)
                        lst[idx] = lst[idx]*2
            elif dartList[idx] == "*" and isFirst:
                Firstisstar = True
            else:
                lst[-1] = lst[-1]*(-1)
        isFirst = False
    answer = sum(lst)
    return answer
