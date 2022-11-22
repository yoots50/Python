def getSecondWord(str) :
    str = str.strip()
    if str.find(' ') == -1 :
        return ' '
    else :
        return str[str.find(' ')+1:].strip()
str = input ('문자열 입력 : ')
if getSecondWord(str) == ' ' :
    print ('빈 문자열이 반환되었습니다.')
else :
    print (getSecondWord(str),len(str))
