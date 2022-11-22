while True:
    checkString = input("회문인지 검사할 영여로 된 문자열을 입력해주세요: ")
    if checkString == "end":
        break
    qu = []
    st = []
    for ch in checkString:
        if ch.isalpha():
            qu.append(ch.lower())
            st.append(ch.lower())
    while qu:
        if qu.pop(0) != st.pop():
            print("%s는 회문이 아닙니다." % checkString)
            break
    else:
        print("%s는 회문입니다." % checkString)
