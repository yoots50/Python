def deleteStr2FromStr1(str1, str2):
    idx = str1.find(str2)
    if idx > 0:
        return str1[:idx] + str1[idx + len(str2):]
    return str1

s1 = input("문자열 입력: ")
s2 = input("삭제할 문자열 입력: ")

print(deleteStr2FromStr1(s1, s2))
