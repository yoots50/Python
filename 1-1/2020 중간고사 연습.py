#1번째 문제
temp = float(input("온도 : "))
humid = float(input("습도 : "))
def DI(temp,humid) :
    return (0.81 * temp) + (0.01 * humid * ((0.99 * temp) - 14.3)) + 46.3
DI = DI(temp,humid)
print("DI = ",DI)
if DI > 83 :
    print ("대부분의 사람들이 불쾌감을 느낌.")
elif DI <= 83 and 80 <= DI :
    print ("50% 정도의 사람들이 불쾌감을 느낌.")
elif DI >= 70 and DI < 80 :
    print ("일부 사람들이 불쾌감을 느낄 수 있음.")
else :
    print ("쾌적함.")

#2번째 문제
str = input()
def string13(x) :
    xx = x.strip()
    if xx.find(" ") == -1 :
        print ('최소 두개 단어 필요')
    else :
        x1 = xx[:xx.find(" ")] #첫번째 문자
        xl = xx[xx.find(" ") + 1:].strip() #두번째 공백부터 자른 문자열 + 양쪽 공백 제거
        if xl.find(" ") == -1 : #입력한 문자열이 두 개일 때
            return x1 #첫 번째 문자열 반환
        else : #입력한 문자열이 세 개 또는 네 개이상일 때
            x3orx4above = xl[xl.find(" ") + 1:].strip()
            if x3orx4above.find(" ") == -1 : #입력한 문자열이 세 개일 때 
                x3 = x3orx4above #입력한 문자열이 세 개라서 곧바로 세 번째 문자열
                return x1 + x3 #첫 번째 + 세 번째 문자열 반환
            else : #입력한 문자열이 세 개보다 많을 때
                x3 = x3orx4above[:x3orx4above.find(" ")].strip() #입력한 문자열이 네 개 이상이라 자르고 세 번째 문자열
                return x1 + x3 #첫 번째 + 잘라서 만든 세 번째 문자열 반환
print (string13(str))

