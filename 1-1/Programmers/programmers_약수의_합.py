def solution(n):
    if n <= 1:
        return n
    sum = 1+n
    for num in range(2,n):
        if n % num == 0:
            sum += num
    return sum
