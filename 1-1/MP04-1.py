def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# ******-*******
# 011111-
# -1
def getYear(idStr):
    s = idStr[:2]
    if s.isdigit() == False: # not s.isdigit()
        print("주민등록번호의 년도가 숫자가 아닙니다")
        return 0
    year = int(s)
    if year >= 0 and year <= 22:
        #y = 2000 + year
        return 2000 + year
    else: # year >= 23 and year <= 99
        return 1900 + year       
   
#print(getYear("000000-1111111"))

def getMonth(idStr):
    s = idStr[2:4]
    if s.isdigit() == False: # not s.isdigit()
        print("주민등록번호의 월이 숫자가 아닙니다")
        return 0
    m = int(s)
    if m < 1 or m > 12:
        print("월 정보가 1~12범위 밖입니다.")
        return 0
    return m

#print(getMonth("000000-1111111"))
#print(getMonth("001200-1111111"))
#print(getMonth("000100-1111111"))
#print(getMonth("000700-1111111"))
#print(getMonth("001000-1111111"))

"""
def getDay(idStr, year, month):
    s = idStr[4:6]
    if s.isdigit() == False: # not s.isdigit()
        print("주민등록번호의 일 정보가 숫자가 아닙니다")
        return 0
    d = int(s)
    if month == 2:
        if isLeapYear(year) and d >= 1 and d <= 29:
            return d
        elif not isLeapYear(year) and d >= 1 and d<= 28:
            return d
        print("범위 밖")
        return 0
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if d >= 1 and d <= 31:
            return d
        print("범위 밖")
        return 0
    else:
        if d >= 1 and d <= 30:
            return d
        print("범위 밖")
        return 0
"""
def getDay(idStr, year, month):
    maxDay = 31
    s = idStr[4:6]
    if s.isdigit() == False: # not s.isdigit()
        print("주민등록번호의 일 정보가 숫자가 아닙니다")
        return 0
    d = int(s)
    if month == 2:
        if isLeapYear(year):
            maxDay = 29
        else:
            maxDay = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        maxDay = 30
    if d >= 1 and d <= maxDay:
        return d
    else:
        print("범위 밖")
        return 0 
    
#print(getDay("000230-1111111", 2000, 2)) # 0
#print(getDay("000229-1111111", 2000, 2)) # 29
#print(getDay("000228-1111111", 2000, 2)) # 28
#print(getDay("010229-1111111", 2001, 2)) # 0
#print(getDay("010230-1111111", 2001, 2)) # 0
#print(getDay("010228-1111111", 2001, 2)) # 28
#print(getDay("000332-1111111", 2000, 3)) # 0
#print(getDay("000331-1111111", 2000, 3)) # 31
#print(getDay("000430-1111111", 2000, 4)) # 30
#print(getDay("000431-1111111", 2000, 4)) # 0

def getSecondNum(idStr, year):
    n = int(idStr[7])
    #if year >= 1923 and year <= 1999:
    if (year >= 2000 and (n == 3 or n == 4)) or (year < 2000 and (n == 1 or n == 2)):
        return n
#    elif (year < 2000 and (n == 1 or n == 2)):
#        return n
    print("두 번째 숫자가 맞지 않습니다")
    return 0

#print(getSecondNum("000230-1111111", 2000))
#print(getSecondNum("000230-2111111", 2000))
#print(getSecondNum("000230-3111111", 2000))
#print(getSecondNum("000230-4111111", 2000))
#print(getSecondNum("870229-1111111", 1987))
#print(getSecondNum("870229-2111111", 1987))
#print(getSecondNum("870229-3111111", 1987))
#print(getSecondNum("870229-4111111", 1987))

def isValid(idStr):
    if len(idStr) != 14:
        print("주민등록번호의 길이가 짧거나 깁니다")
        return False
    elif idStr[6] != '-': # idStr.find('-') != 6
        print("-의 위치가 틀립니다")
        return False
    year = getYear(idStr)
    month = getMonth(idStr)
    day = getDay(idStr, year, month)
    sn = getSecondNum(idStr, year)
#    return bool(year and month and day and sn) 
    return year != 0 and month != 0 and day != 0 and sn != 0
#    if year == 0 or month == 0 or day == 0 or sn == 0:
#        return False
#    return True

print(isValid("000230-1111111")) # False
print(isValid("000230-2111111")) # False
print(isValid("000230-3111111")) # False 
print(isValid("000229-4111111")) # True
print(isValid("870229-1111111")) # False
print(isValid("870228-2111111")) # True
print(isValid("870332-1111111")) # False
print(isValid("870430-1111111")) # True
print(isValid("870431-22111111")) # False
"""
def printValid(v):
    if v:
        print(True)
    else:
        print(False)

printValid(isValid("000230-1111111"))
printValid(isValid("000230-2111111"))
printValid(isValid("000230-3111111"))
printValid(isValid("000229-4111111"))
printValid(isValid("870229-1111111"))
printValid(isValid("870228-2111111"))
printValid(isValid("870332-1111111"))
printValid(isValid("870430-1111111"))
printValid(isValid("870431-22111111"))
"""


