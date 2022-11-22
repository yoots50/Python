def solution(s):
    lst = []
    cnt = 0
    answer = ""
    for idx in range(len(s)):
        if s[idx] == " ":
            lst.append(" ")
            cnt = 0
        else:
            if cnt % 2:
                lst.append(s[idx].lower())
            else:
                lst.append(s[idx].upper())
            cnt += 1
    for l in lst:
        answer = answer + l
    return answer

