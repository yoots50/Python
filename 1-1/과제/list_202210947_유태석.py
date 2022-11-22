score = [50,30,90,70,60]
idx, val, cnt = 0, 0, 0

print('현재 입력된 점수는')
print(score, '이고, 모두 ', len(score), '개 입니다.')

print()
print("append 연습")
val = int(input("append할 값 : "))
score.appenc(val)
print(score)

print()
print("insert 연습")
idx = int(input("insert할 위치 : "))
val = int(input("insert할 값 : "))
score.insert(idx,val)
print(score)

print()
print("index 연습")
val = int(input("찾고 싶은 값 : "))
idx = score.index(val)
print("%d는 %d번째 위치하고 있습니다." % (val, idx))

print()
print("remove 연습")
val = int(input("삭제하고 싶은 값 : "))
score.remove(val)
print(score)

print()
print("del 연습")
idx = int(input("삭제할 위치 : "))
del(score[idx])
print(score)

print()
print("count 연습")
val = int(input("갯수를 알고싶은 값 : "))
cnt = score.count(val)
print(score)
print("%d는 %d번 나옵니다." % (val, cnt))

print()
print("sort 연습")
score.sort()
print(score)

print()
print("reverse sort 연습.")
score.reverse()
print(score)


