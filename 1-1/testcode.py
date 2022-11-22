''' #과목들의 평균 값을 구하는 프로그램
def averageCalculator(dic):
    return sum(dic.values())/len(dic)
test_score = {}
while True:
    try:
        cnt = int(input("평균을 구할 과목의 갯수를 입력하세요: "))
        break
    except ValueError:
        print("숫자만 입력하세요.")
while cnt:
    while True:
        try:
            test_score[input("과목을 입력하세요: ")] = int(input("성적을 입력하세요: "))
            cnt -= 1
            break
        except ValueError:
            print("성적에는 숫자만 넣어 주세요.")
print(f"{list(test_score.keys())}의 평균 값은 {averageCalculator(test_score)}입니다.")
'''
''' #숫자의 홀짝을 판별하는 프로그램
def isEvenOrOdd(num):
    if num % 2:
        return "홀"
    return "짝"
while True:
    try:
        num = int(input("홀짝을 판별할 숫자를 입력하세요: "))
        break
    except ValueError:
        print("숫자를 입력해주세요.")
print(isEvenOrOdd(num))
'''

