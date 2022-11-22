import time 

n = int(input("n을 입력하세요: "))

start = time.time()
s = 0
for i in range (1, n + 1):
    s = s + i
end = time.time()
print(s, end - start)

start = time.time()
s = 0
s = n * (n + 1) // 2
end = time.time()
print(s, end - start)
