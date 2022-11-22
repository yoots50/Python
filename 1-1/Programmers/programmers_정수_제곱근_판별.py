import math
def solution(n):
    root = math.sqrt(n)
    if f"{root}" == f"{int(root)}.0":
        return (math.sqrt(n)+1)**2
    return -1
