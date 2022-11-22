def solution(brown, yellow):
    S = brown * yellow
    for i in range(1,yellow+1):
        if brown == i * 2 + (yellow / i) * 2 + 4 and int(yellow / i) == yellow / i :
            return [yellow/i+2,i+2]
    print("X")
