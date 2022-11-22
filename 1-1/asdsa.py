def getFirstword(x):
    x = x.strip()
    idx = x.index(' ')
    #return x[0:idx]
    return x[idx + 1:]
x = "    hello world"
print(getFirstword(x))

    
