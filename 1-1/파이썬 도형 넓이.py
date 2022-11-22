import math
list1 = []
S = []
n = 0
k = 0
while k != 5  :
    choice = input('도형의 종류를 입력하시오 : ')
    if choice == '사각형' :
        list1.append(choice)
        x1 = int(input('x1 좌표를 입력하시오 : '))
        y1 = int(input('y1 좌표를 입력하시오 : '))
        x2 = int(input('x2 좌표를 입력하시오 : '))
        y2 = int(input('y2 좌표를 입력하시오 : '))
        tuple1 = (x1, y1, x2, y2,)
        list1.append(tuple1)
        a1 = x1 - x2
        if a1 < 0 :
            a1 *= -1
        b1 = y1 - y2
        if b1 < 0 :
            b1 *= -1
        S1 = a1 * b1
        S.append(S1)
        k += 1        
    elif choice == '삼각형' :
        list1.append(choice)
        x1 = int(input('x1 좌표를 입력하시오 : '))
        y1 = int(input('y1 좌표를 입력하시오 : '))
        x2 = int(input('x2 좌표를 입력하시오 : '))
        y2 = int(input('y2 좌표를 입력하시오 : '))
        x3 = int(input('x3 좌표를 입력하시오 : '))
        y3 = int(input('y3 좌표를 입력하시오 : '))
        tuple2 = (x1, y1, x2,)
        list1.append(tuple2)
        S2 = (((x1 * y2) + (x2 * y3) + (x3 * y1)) - ((y1 * x2) + (y2 * x3) + (y3 * x1))) / 2
        if S2 < 0 :
            S2 *= -1
        S.append(S2)
        k += 1
    elif choice == '원' :
        list1.append(choice)
        x = int(input('x 좌표를 입력하시오 : '))
        y = int(input('y 좌표를 입력하시오 : '))
        r = int(input('반지름을 입력하시오 : '))
        tuple3 = (x, y, r,)
        list1.append(tuple3)
        S3 = math.pi * r ** 2
        S.append(S3)
        k += 1        
if k == 5 :
    while n < 5 :
        print(str(list1[2*n]))
        print('넓이 : ' + str(S[n]))
        n += 1        
input()
