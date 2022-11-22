# 1. 문자열을 입력 받기
# 2. 양 끝에 있는 공백 문자 제거
# 3. 공백 문자가 문자열 중간에 있는지 확인
# 4. 만약 있으면, 두 개 단어 이상 입력하라고 출력
# 5. 만약 없으면 getString() 호출하며 문자열 전달
# 6. getString()
# 7. 양 끝의 공백 문자 제거
# 8. 문자열 중간의 공백 문자의 인덱스 찾기
# 9. 0부터 인덱스까지의 문자열 분리 후 첫 번째 단어로 저장
# 10. s = 인덱스 + 1부터 끝까지 문자열 분리
# 11. s의 양끝에 있는 공백문자 제거
# 12. s의 중간에 있는 공백문자 확인
# 13. 만약 공백문자 없으면 9번에서 분리한 첫 번째 단어 반환
# 14. 있으면, s = 인덱스 + 1부터 끝까지 문자열 분리
# 15. 양끝의 공백 문자 제거
# 16. 중간의 공백 문자 확인
# 17. 공백문자가 없으면 9번에서 찾은 첫 번째 단어 + ' ' + 14번에 찾은 나머지 문자열 반환
# 18. 공백문자가 있으면, 9번에서 찾은 첫 번째 단어 + ' ' + 0부터 인덱스까지의 문자열 분리
def getString(str):
    s = str.strip()
    #print(s)
    idx = s.find(' ')
    firstWord = s[:idx]
    rest = s[idx + 1:].strip()
    idx = rest.find(' ')
    if idx == -1:
        return firstWord
    rest = rest[idx + 1:].strip()
    idx = rest.find(' ')
    if idx == -1:
        return firstWord + ' ' + rest
    else:
        return firstWord + ' ' + rest[:idx]

#twoWords = "   a    hello     "       
#str = getString(twoWords)
#print(str)
#s = "    a    hello    b   c  "
#str = getString(s)
#print(str)
#s = "    a    hello    b   "
#str = getString(s)
#print(str)
str = input("최소한 두 개 단어 이상의 문자열을 입력하세요: ")
s = str.strip()
if s.find(' ') == -1:
    print("최소한 두 개 단어 이상의 문자열을 입력해야 합니다.")
else:
    str = getString(s)
    print(str +  ",", len(str))
