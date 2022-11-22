print ('두 정수를 더하는 계산기입니다.')
n1 = int(input('1과 100사이의 정수 입력: '))
n2 = int(input('1과 100사이의 정수 입력: '))
if n1 >= 1 and n1 <= 100 and n2 >= 1 and n2 <= 100:
    print (n1 + n2)
else :
    if n1 >= 1 and n1 <= 100:
        print ('두 번째 정수가 범위 밖')
    if n2 >= 1 and n2 <= 100:
        print ('첫 번째 정수값이 범위 밖')    
    else:
        print('첫 번째와 두 번째 정수값이 범위 밖')
