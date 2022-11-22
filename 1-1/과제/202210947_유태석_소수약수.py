def isPrime(num) :
    for i in range (2,num) :
        if num % i == 0 :
            return False
    return True
def getDivisors(num) :
    divisors = []
    for i in range (1,num+1) :
        if num % i == 0 :
            divisors.append(i)
    return divisors
def readNumber(num) :
    while num <= 1 :
        num = int(input('2 이상의 숫자를 입력하라 : '))
    else :
        return num
        
num = readNumber(int(input('2 이상의 정수 입력 : ')))    
n = 1
while num != 1 :
    print('정수 : %s, 약수 개수 : %s, 소수 : %s' % (num, len(getDivisors(num)), isPrime(num)))
    num = num - n
