lst1, lst2, answer = [], [], []
with open("MP09Data1.txt") as Data1:
    lst = Data1.readlines()
for num in lst:
    lst1.append(num.strip('\n'))
with open("MP09Data2.txt") as Data2:
    lst = Data2.readlines()
for num in lst:
    lst2.append(num.strip('\n'))
lst = lst1 + lst2
leng = len(lst)
while len(answer) != leng:
    answer.append(max(lst))
    maxnum = max(lst)
    while lst.count(maxnum) != 0:
        lst.remove(maxnum)
print(len(lst1))
print(len(lst2))
for line in answer:
    print(line)
