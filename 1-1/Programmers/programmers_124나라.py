'''
def threeSum(r):
    sum = 0
    while not(r == 0):
        sum += 3**r
        r -= 1
    return sum
def solution(n):
    r = 1
    k = 0
    answer = ''
    while not(threeSum(r-1)<n<=threeSum(r)):
        r += 1
    diff = n - threeSum(r-1)
    while not(r == 0):
        if 0<diff<=3**(r-1):
             answer += '1'
             k = 0
        elif 3**(r-1)<diff<=(3**(r-1))*2:
             answer += '2'
             k = (3**(r-1))
        else:
             answer += '4'
             k = 2*(3**(r-1))
        diff -= k
        r -= 1
    return answer
'''
def solution(n):
    k = 0



print(solution(1))
print(solution(2))
print(solution(3))
print(solution(5))
print(solution(10))
