def yoon (x) : #x는 주민등록번호, 윤년 판단 함수
    if x % 400 == 0 :
        return True
    if x % 4 == 0 and x % 100 != 0 :
        return True
    return False

def year (x) : #x는 주민등록번호, 년도 판단 함수
    if x[:2].isdigit() == False :
        print ('년도가 숫자가 아닙니다.')
        return 0
    else :
        year = str(x)[:2]
        if int(year) >= 0 and int(year) <= 22 :
            return int(year) + 2000
        return int(year) + 1900

def month (x) : #x는 주민등록번호, 달 판단 함수
    if x[2:4].isdigit() == False :
        print ('달이 숫자가 아닙니다.')
        return 0
    else :
        month = int(x[2:4])
        if month > 12 or month < 1:
            print('달이 1에서 12사이가 아닙니다.')
            return 0
        else :
            return month

def day (x,y,z) : #x는 주민등록번호, y는 달, z는 연도 (4자리), 일 판단 함수
        if x[4:6].isdigit() == False :
            print ('일이 숫자가 아닙니다.')
            return 0
        else :
            day = int(x[4:6])
            month = y
            year = z
            if year == 0 or month > 12 or month < 1 : 
                print ('년을 잘못 적었거나 달을 잘못 적었습니다.')
                return 0
            elif month == 2 :
                if yoon(x) == False and day > 28 :
                    print ('윤년이 아니고 2월이지만 28일이 넘습니다.')
                    return 0
                if yoon(x) == True and day > 29 :
                    print ('윤년이고 2월이지만 29일이 넘습니다.')
                    return 0
            elif month >= 8 :
                if month % 2 == 0 :
                    if day > 31 :
                        print ('8,10,12월이지만 31일이 넘습니다.')
                        return 0
                    else :
                        return month
                else :
                    if day > 30 :
                        print ('9,11월이지만 30일이 넘습니다.')
                        return 0
                    else :
                        return month
            else :
                if month % 2 == 0 :
                    if day > 30 :
                        print ('2,4,6월이지만 30일이 넘습니다.')
                        return 0
                    else :
                        return month
                else :
                    if day > 31 :
                        print ('1,3,5,7월이지만 31일이 넘습니다.')
                        return 0
                    else :
                        return month

def nextn(x,y) : #x는 주민등록번호, y는 년도 4자리, -다음 판단 함수
    if x[7:].isdigit() == False :
        print ('-다음이 숫자가 아닙니다.')
        return 0
    else :
        nextn = int(x[7])
        year = int(y)
        if 1900 <= year and 1999 >= year :
            if nextn != 1 and nextn != 2 :
                print ('년도와 -다음 숫자가 맞지 않습니다.')
                return 0
            else :
                return 1
        else :
            if nextn != 3 and nextn != 4 :
                print ('년도와 -다음 숫자가 맞지 않습니다.')
                return 0
            else :
                return 1

def isValid (x) : #x는 주민등록번호, 주민등록번호 판단 함수
    error = False 
    if x.find('-') == -1: #- 존재 판단
        print ('-가 없습니다.')
        error = True
    else :
        if x.index('-') != 6: #-위치 판단
            print ('-가 잘못된 위치에 있습니다.')
            error = True
    if len(x) != 14 : #길이 판단
        print ('주민등록 번호의 길이가 맞지 않습니다.')
        error = True
    if nextn(x,year(x)) == 0 :
            error = True
    elif year(x) == 0 :
        error = True
    if month(x) == 0 :
        error = True
    if day(x,month(x),year(x)) == 0:
        error = True
    if error == True :
        return False
    else :
        return True

TorF = isValid(input('주민등록번호를 입력하세요 : '))
while TorF == False : #적합한 주민등록번호를 입력할 때 까지 계속 입력
    print ('주민등록번호가 적합하지 않습니다. 이유는 위와 같습니다.')
    TorF = isValid(input('주민등록번호를 다시 입력해주세요 : '))
if TorF == True :
    print ('주민등록번호가 적합해보입니다.')
