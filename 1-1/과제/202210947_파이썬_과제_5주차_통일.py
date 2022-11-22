year = int(input('년도를 입력하세요. : '))
month = int(input('월을 입력하세요. : '))
day = int(input('일을 입력하세요. : '))
if year % 4 == 0 :
    if year & 400 == 0 :
        year = 'year+'
    elif year & 100 == 0 :
        year = 'yearl'
    else :
        year = 'year+'
else :
    year = 'yearl'
dayOfYear = (month - 1) * 31 + day
if year == 'yearl' :
    if month <= 2:
        print('통일 : ',dayOfYear)
    else:
        print('통일 : ',dayOfYear - ((4 * month + 23) // 10))
if year == 'year+':
    if month == 1:
        print('통일 : ',dayOfYear)
    elif month == 2:
        print('통일 : ',dayOfYear + 1)
    else :
        print('통일 : ',dayOfYear - ((4 * month + 23) // 10) + 1)
        
