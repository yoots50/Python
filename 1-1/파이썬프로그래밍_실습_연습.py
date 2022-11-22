#파이썬프로그래밍 실습 2

#실습 02-01 : 사용자에게 0~100사이의 정수를 입력 받고 입력한 값을 화면에 출력하기

int_zero_to_hundred = input('0~100사이의 정수를 입력 : ')
print (int_zero_to_hundred)
    
#실습 02-02 : 위와 같음

#실습 02-03 : 사용자로부터 문자열 3개를 연속해서 입력 받고, 3 개의 문자열을 붙여서 한 개의 문자열로 출력하기

str_1 = input('첫 번째 문자열 입력 : ')
str_2 = input('두 번째 문자열 입력 : ')
str_3 = input('세 번째 문자열 입력 : ')

print(str_1,str_2,str_3)

#파이썬프로그래밍 실습 3

#실습 03-01 : 사용자로부터 월을 영어 단어로 입력 받고 해당 월이 몇 일까지 있는지 화면에 출력하는 프로그램을 작성

#조건 : 월의 이름은 첫 글자만 대문자로 쓰도록 함, 단 월은 1-4월까지만 처리함, 윤년은 계산하지 않음 (2월은 무조건 28일), 1-4월과 다른 달이 입력되면 아무것도 하지 않음.

month = input('1월 ~ 4월을 영어로 입력 (단, 첫 글자만 대문자로 입력.) : ')

if month == 'January' :
    print ('31일')
elif month == 'February' :
    print ('28일')
elif month == 'March' :
    print ('30일')
elif month == 'April' :
    print ('31일')
    
#실습 03-02 : 컴퓨터와 사람의 주사위 던지기

#조건 : 컴퓨터는 무작위 숫자 발생기를 이용해서 주사위를 굴리는 것과 같은 효과를 내도록 함, 사람은 원하는 숫자 입력, 두 개를 비교해서 누가 이겼는지 화면에 출력, 사암이 입력한 숫자가 1-6사이가 아니면 오류 출력.

import random 

comp = random.randint(1,6)
human =  int(input('주사위 값을 입력 : '))

if not (human >= 1 and human <= 6) :
    print ('오류')
elif comp == human : 
    print ('비김')
elif comp > human :
    print ('컴퓨터 승')
else :
    print ('인간 승')
    
#파이썬프로그래밍 실습 4

#실습 04-01 : 두 개 이상의 단어가 ㅇ;ㅆ는 문자열에서 첫 번째 단어 찾는 함수 구현하기

#조건 : 앞과 뒤에 있는 공백 문자는 먼저 제거한 후에 단어를 찾을 것, 이 함수를 사용해서 사용자로부터 문자열을 입력 받고, 첫 번째 단어를 출력하는 프로그램 작성.

def getFirstWord (str) :
    str = str.strip()
    return str[:str.find(' ')]

str = input ('문자열 입력 : ')

getFirstWord(str)

#실습 04-02 : 사용자로부터 1 ~ 100까지의 숫자를 입력 받고 화면에 출력하는 함수를 작성할 것.

#조건 : 만약 사용자가 1 ~ 100 범위 밖의 숫자를 입력하면 잘못 입력했다고 출력하고 False 반환, 범위 안의 숫자를 입력하면 값을 출력하고 True 반환, 이 함수를 사용해서 제대로 출력되었는지 확인하는 프로그앰 작성.

def getOnetoHund (int) :
    if not (0 <= int and int <= 100) :
        print('범위 밖 숫자')
        return False
    else : 
        print(int)
        return True
    
int1 = int(input ('1 ~ 100 사이의 숫자 입력 : '))

getOnetoHund(int1)

#실습 04-03 : 문자열 두 개를 인자로 전달 받고, 첫 번째 문자열에서 두 번째 문자열을 삭제한 나머지 문자열을 반환하는 함수 구현

#조건 : 첫 번째 문자열에 두 번째 문자열이 포함되어 있지 않다면 원본 문자열 반환

def delSecondWord (str_1,str_2) :
    str_1 = str_1.strip()
    str_2 = str_2.strip()
    if str_1.find(str_2) == -1 :
        return str_1
    else : 
        return str_1[:str_1.find(str_2)] + str_1[str_1.find(str_2)+len(str_2):]
    
print(delSecondWord (input('첫 번째 문자열 입력 : '),input('두 번째 문자열 입력 : ')))

#파이썬프로그래밍 실습 6

#실습 06-01 : 사용자로부터 숫자 5개를 입력 받고, 가장 큰 값을 찾아서 반환하는 함수를 작성하고 이를 활용하는 프로그램을 구현할 것.

def maxFive(n1,n2,n3,n4,n5) :
    return max(n1,n2,n3,n4,n5)

print(maxFive (input('첫 번째 숫자 입력 : '),input('두 번째 숫자 입력 : '),input('세 번째 숫자 입력 : '),input('네 번째 숫자 입력 : '),input('다섯 번째 숫자 입력 : ')))

#실습 06-02 : 동전을 던져서 앞/뒷면이 나오는 횟수를 세고 1/2 확률에 수렴하는지 확인하는 프로그램을 작성한다.

#조건 : 동전을 실제로 던질 수는 없으므로, randint() 함수를 이용해서 두 개의 숫자 중 한 개를 무작위로 생성해서 동전의 앞/뒷면을 대신한다, 100, 1000, 10000회 던져서 앞/뒷면이 나오는 횟수를 각각 출력해본다, 함수에 입력으로 몇 번 던질 것인지 전달하고, 함수에서는 앞/뒷면이 나온 횟수를 세서 화면에 출력한다.

import random

def coin(count) :
    count = int(count)
    front = 0
    back = 0
    for n in range (0,count) :
        num = random.randint(1,2)
        if num == 1 :
            front += 1
        else : 
            back += 1
    print ('앞이 나온 횟수 : ',front,', 뒤가 나온 횟수 : ',back)
    return (front + back) / 2

print(coin(input('얼마나 반복할 것인지 입력 : ')))

#실습 06-03 : 1000이하의 숫자를 사용자로부터 입력 받고, 해당 숫자의 모든 약수의 합을 화면에 출력하는 프로그램을 작성한다.

#조건 : 단 정수 한 개를 인자로 전달 받고 약수의 합을 구해서 결과로 반환하는 함수를 구현해서 사용한다, getSumOfDivisiors(number), number : 1000 이하의 정수, 반환값 : 약수의 합.

def getSumOfDivisors (number) :
    sum = 0
    for i in range (1,number+1) :
        if number % i == 0 :
            sum += i
    return sum

print(getSumOfDivisors(int(input('1000 이하의 숫자 입력 : '))))

#실습 06-04 : 사용자가 1000을 입력할 때까지 정수를 지속적으로 입력 받고, 가장 큰 수를 찾아서 화면에 출력하는 프로그램을 작성하라.

num = int(input ('숫자 입력 : '))

maxnum = 1000

while num != 1000 : 
    num = int(input ('숫자 다시 입력 : '))
    if num > maxnum :
        maxnum = num

if num == 1000 :
    print (maxnum)
    
#파이썬프로그래밍 실습 7

#07-01 : 사람 1과 사람 2에 대해서 받은 입력을 바탕으로 가위바위보 게임 진행.

hum1 = input('사람 1 입력 : ')
hum2 = input('사람 2 입력 : ')

if hum1 == hum2 :
    print ('비김')
else :
    if hum1 == '가위' :
        if hum2 == '보' :
            print('사람 1 승.')
        else : 
            print('사람 2 승.')
    elif hum1 == '바위' :
        if hum2 == '보' :
            print('사람 2 승.')
        else :
            print('사람 1 승.')
    else :
        if hum2 == '가위' :
            print('사람 2 승.')
        else :
            print('사람 1 승.')
