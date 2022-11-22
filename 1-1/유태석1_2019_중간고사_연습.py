def munji(d1,d2,d3,d4,d5,d6,d7) :
    return (d1 + d2 + d3 + d4 + d5 + d6 + d7) / 7
def cho_munji(d1,d2,d3,d4,d5,d6,d7) :
    return (d1 + d2 + d3 + d4 + d5 + d6 + d7) / 7

d1 = 44
d2 = 44
d3 = 32
d4 = 60
d5 = 84
d6 = 112
d7 = 41

if munji(d1,d2,d3,d4,d5,d6,d7) >= 0 and munji(d1,d2,d3,d4,d5,d6,d7) <= 15 :
    print('미세먼지 좋음')
if munji(d1,d2,d3,d4,d5,d6,d7) > 15 and munji(d1,d2,d3,d4,d5,d6,d7) <= 35 :
    print('미세전지 보통')
if munji(d1,d2,d3,d4,d5,d6,d7) > 35 and munji(d1,d2,d3,d4,d5,d6,d7) <= 75 :
    print('미세먼지 나쁨')
if munji(d1,d2,d3,d4,d5,d6,d7) > 75 :
    print('미세먼지 매우 나쁨')

d1 = 29
d2 = 21
d3 = 18
d4 = 34
d5 = 67
d6 = 79
d7 = 18

if cho_munji(d1,d2,d3,d4,d5,d6,d7) >= 0 and cho_munji(d1,d2,d3,d4,d5,d6,d7) <= 30 :
    print('초미세먼지 좋음')
if cho_munji(d1,d2,d3,d4,d5,d6,d7) > 30 and cho_munji(d1,d2,d3,d4,d5,d6,d7) <= 80 :
    print('초미세전지 보통')
if cho_munji(d1,d2,d3,d4,d5,d6,d7) > 80 and cho_munji(d1,d2,d3,d4,d5,d6,d7) <= 100 :
    print('초미세먼지 나쁨')
if cho_munji(d1,d2,d3,d4,d5,d6,d7) > 100 :
    print('초미세먼지 매우 나쁨')




cho_munji(d1,d2,d3,d4,d5,d6,d7)
