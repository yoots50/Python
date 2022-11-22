def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return i
    return -1
v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18))
print(search_list(v, 33))
print(search_list(v, 900))
def search_list2(a, x):
    alist = []
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            alist.append(i)
    return alist
print(search_list2(v, 40))
print(search_list2(v, 33))
print(search_list2(v, 900))
