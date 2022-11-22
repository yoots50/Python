def yak(num):
    cnt = 2
    if num == 1:
        return 1
    for i in range(2,num):
        if num % i == 0:
            cnt += 1
    return cnt
def solution(left, right):
    sum = 0
    for num in range(left,right+1):
        if yak(num) % 2 == 0:
            sum += num
        else:
            sum -= num
    return sum
