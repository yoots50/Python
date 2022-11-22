def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    lst = []
    for first in range(len(nums)-2):
        for second in range(first+1,len(nums)-1):
            for third in range(second+1,len(nums)):
                check = nums[first] + nums[second] + nums[third]
                if isPrime(check) == True:
                    answer += 1
    return answer
