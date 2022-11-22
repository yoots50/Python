#1. 사용자로부터 입력을 받아야 함
#  - 거리
#  - 컴퓨터 가격
#  input() 사용
#  문자열 --> 숫자값 (float)
#2. 공식을 가지고 계산
#3. 화면에 출력

mileage = 10
gasPrice = 1900
speed = 40
wage = 9160
distanceA = input("쇼핑몰 A까지의 거리를 km단위로 입력하세요: ")
computerPriceA = input("쇼핑몰 A의 컴퓨터 가격을 입력하세요: ")

cost1 = float(distanceA) / mileage * gasPrice
cost2 = float(distanceA) / speed * wage

costA = float(computerPriceA) + (cost1 + cost2) * 2
print("쇼핑몰 A에서 구입하는 전체 비용은", costA, "입니다.")

distanceB = input("쇼핑몰 B까지의 거리를 km단위로 입력하세요: ")
computerPriceB = input("쇼핑몰 B의 컴퓨터 가격을 입력하세요: ")

cost1 = float(distanceB) / mileage * gasPrice
cost2 = float(distanceB) / speed * wage
costB = float(computerPriceB) + (cost1 + cost2) * 2
print("쇼핑몰 B에서 구입하는 전체 비용은", costB, "입니다.")

onlineComputer = input("온라인 컴퓨터 가격을 입력하세요: ")
onlineShipping = input("택배 비용을 입력하세요: ")
costOnline = float(onlineComputer) + float(onlineShipping)
print("온라인 쇼핑몰에서 구입하는 전체 비용은", costOnline, "입니다")

minCost = min(costA, costB, costOnline)
if minCost == costOnline:
    print("A 쇼핑몰에서 구입하는 것이 좋습니다")
elif minCost == costB:
    print("B 쇼핑몰에서 구입하는 것이 좋습니다")
elif minCost == costA:
    print("온라인 쇼핑몰에서 구입하는 것이 좋습니다")
