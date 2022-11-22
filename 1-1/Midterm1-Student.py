# 202210947 유태석
txt = """There are many variations of passages of Lorem Ipsum available,
but the majority have suffered alteration in some form, by
injected humour, or randomised words which don't look even
slightly believable. If you are going to use a passage of;
Lorem Ipsum, you need to be? sure there isn't anything embarrassing
hidden in the middle of text. All the Lorem Ipsum generators on the
Internet tend to repeat predefined chunks as necessary, making this
the first true generator on the Internet. It uses a dictionary of
over 200 Latin words, combined with a handful of model sentence
structures, to generate Lorem Ipsum which looks reasonable.
The generated Lorem Ipsum is therefore always free from repetition,
injected humour, or non-characteristic words etc!
"""

# 다음 함수들에서 pass를 지우고 본인 코드를 작성할 것

def getNextPeriodPos(txt, startPos):
    return txt[startPos:].find('.')
        

print(getNextPeriodPos("Hi. I am Tom. I am a boy", 0))  # 2 출력
print(getNextPeriodPos("Hi. I am Tom. I am a boy", 3))  # 9 출력
print(getNextPeriodPos("Hi. I am Tom. I am a boy", 13)) # -1 출력


def getNextLine(txt, startPos):
    if len(txt) <= startPos :
        return ''
    else :
        txt = txt[startPos:]
        if txt.find('.') != -1 :
            return txt[:txt.find('.')+1].strip()
        else :
            return txt.strip()
            
    
print(getNextLine("Hi. I am Tom. I am a boy", 0))  # Hi. 출력
print(getNextLine("Hi. I am Tom. I am a boy", 3))  # I am Tom. 출력
print(getNextLine("Hi. I am Tom. I am a boy", 13)) # I am a boy 출력

def countWordsInLine(line):
    line = line.strip()
    count = 1
    while line.find(' ') != -1 :
        line = line[line.find(' '):].strip()
        count += 1
    if line.find(' ') == -1 :
        return count
        


print(countWordsInLine("I am Tom.")) # 3 출력


def countPunctuationsInLine(line):
    
            
        


print(countPunctuationsInLine("Hi, I am Tom.")) # 2 출력


def main(txt):    
    txt = txt.strip()
    txt1 = txt[:txt.find('.')]
main(txt)
