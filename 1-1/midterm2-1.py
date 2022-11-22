def getFirstWord(str):
    idx = str.find(' ')
    if idx == -1:
        return str
    else: 
        return str[:idx]

def getRestExceptFirst(str):
    idx = str.find(' ')
    if idx == -1:
        return ""
    else:
        next = str[idx:]
        return next.strip()

def retrieveWords2(str):
    first = getFirstWord(str)
    print("first = ", first)
    next = getRestExceptFirst(str)
    if next == "": # 두 단어로만 구성됨
        return first
    else:
        second = getFirstWord(next)
        next = getRestExceptFirst(next)
        third = getFirstWord(next)
        return first + ' ' + third
    
def retrieveWords(str):
    # 두 번째 단어를 잘라내기
    idx = str.find(' ') # idx는 -1이 될 수 없음
    # 첫 번째 단어 잘라내기
    first = str[:idx]
    print("first = ", first)
    next = str[idx:] # 나머지 문자열
    next = next.strip() # 공백 문자 제거
    idx = next.find(' ')
    if idx != -1: # 두 개 단어 이상
        second = next[:idx]
        next = next[idx:] # 나머지 문자열
        next = next.strip()
        idx = next.find(' ')
        if idx == -1: # 세 개 단어밖에 없음
            return first + ' ' + next
        else:            
            return first + ' ' + next[:idx]
    else: # 두 개 단어 밖에 없음
        return first        

s = input("최소 한 단어 이상의 문자열을 입력하세요: ")
print("입력한 문자열: ", s)
# 공백 제거
s = s.strip()
if s.find(' ') != -1: # 두 개 단어 이상 있음
    t = retrieveWords2(s)
    print("새로운 문자열: ", t)
else:
    print("최소한 두 개 단어 이상은 입력해야 합니다.")
