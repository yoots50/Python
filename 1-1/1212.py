a1 = 5
an = a1
anp1 = an

nlist = []
nlist.append(1)

anlist = []
anlist.append(a1)

for n in range (1,10) :
    
    anp1 = 2**an
    
    anlist.append(anp1)
    nlist.append(n+1)
    
    an = anp1

print(anlist)
print(nlist)
