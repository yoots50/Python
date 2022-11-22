#DI = 0.81 * Temp + 0.01 * Humid * (0.99 * Temp – 14.3) + 46.3
def calcDI(temp, humid):
    return 0.81 * temp + 0.01 * humid * (0.99 * temp - 14.3) + 46.3

temp = float(input("온도를 입력하세요: "))
humid = float(input("습도를 0~100%로 입력하세요: "))
di = calcDI(temp, humid)
#print(di)
print("DI =", di)
if di < 70:
    print("쾌적함")
elif di >= 70 and di < 80:
    print("일부 사람들이 불쾌감을 느낄 수 있음")
elif di >= 80 and di <= 83:
    print("50%정도의 사람들이 불쾌감을 느낄 수 있음")
else:
    print("대부분의 사람들이 불쾌감을 느낄 수 있음")
