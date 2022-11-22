
def numToKor (num,digit) :
    if num == '1' :
        if digit != '일' :
            return digit
        else :
            return '일'
    if digit == '일' :
        digit = ''
    if num == '2' :
        return '이' + digit
    elif num == '3' :
        return '삼' + digit
    elif num == '4' :
        return '사' + digit
    elif num == '5' :
        return '오' + digit
    elif num == '6' :
        return '육' + digit
    elif num == '7' :
        return '칠' + digit
    elif num == '8' :
        return '팔' + digit
    elif num == '9' :
        return '구' + digit
    if num == '0' :
        return 0

def getMoneyText(amount) :
    hund = ''
    ten = ''
    one = ''
    amount = int(amount)
    if amount >= 100 :
        amount = str(amount)
        amounthund = amount[:1]
        amountten = amount[1:2]
        amountone = amount[2:3]
    elif 100 > amount >= 10 :
        amount = str(amount)
        amounthund = '0'
        amountten = amount[:1]
        amountone = amount[1:2]
    else :
        amount = str(amount)
        amounthund = '0'
        amountten = '0'
        amountone = amount
    if numToKor(amounthund,'백') == 0 :
        hund = ''
    else :
        hund = numToKor(amounthund,'백')
    if numToKor(amountten,'십') == 0 :
        ten = ''
    else :
        ten = numToKor(amountten,'십')
    if numToKor(amountone,'일') == 0 :
        one = ''
    else :
        one = numToKor(amountone,'일')            
    print (hund,ten,one)

amount = input('1000이하의 숫자 입력 : ')
getMoneyText (amount)

