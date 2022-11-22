print("삼각형의 세변의 길이를 변c가 가장 길게 입력해주세요. ")
a = int(input("변 a의 길이: "))
b = int(input("변 b의 길이: "))
c = int(input("변 c의 길이: "))

if c*c == a*a + b*b:
    print("직각 삼각형입니다.")
elif c*c < a*a + b*b:
    print("예각 삼각형입니다.")
else:
    print("둔각 삼각형입니다.")

