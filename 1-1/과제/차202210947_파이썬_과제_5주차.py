a = int(input('년도를 입력하세요. : '))
if a % 4 == 0 :
    if a % 400 == 0 :
        print (a,'는 윤년입니다.')
    elif a % 100 == 0 :
        print (a,'는 윤년이 아닙니다.')
    else :
        print (a,'는 윤년입니다.')
else :
    print (a,'는 윤년이 아닙니다.')
