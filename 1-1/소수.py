def f(x) :
    for i in range (2,x) :
        if x % i == 0 :
            return 0
    return x
k = 1
while k > 0 :
    k += 1
    if f(k) != 0 :
        print (f(k))
