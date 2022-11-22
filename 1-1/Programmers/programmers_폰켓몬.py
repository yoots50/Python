def solution(nums):
    numset = set(nums)
    if len(nums)/2 > len(numset):
        return len(numset)
    else:
        return len(nums)/2
