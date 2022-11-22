age = int(input('나이를 입력하세요 : '))
time = int(input('눈을 감고 양팔을 벌리고 외발로 서있을 수 있는 시간을 입력하세요. : '))
age_1 = 0
age = int(age / 10) * 10

if time >= 80 :
    age_1 = 20
if time >= 75 and time < 80 :
    age_1 = 30
if time >= 50 and time < 75 :
    age_1 = 40
if time >= 35 and time < 50 :
    age_1 = 50
if time >= 10 and time < 35 :
    age_1 = 60
if time >= 5 and time < 10 :
    age_1 = 70
if time < 5 :
    age_1 = '80대 이상'

print ('당신의 나이는 ',age,' 대 이지만, 균형 나이는 ',age_1,' 대 입니다.')

    
