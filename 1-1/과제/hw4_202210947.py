
# 연이율 3% 1년 마다 복리로 이자 적립 10000을 올해 초 저금 10년 후 얼마?

n = 10
a = 10000
r = 1.03
S = a*r**n
print (S)

# 똑같은 조건에 20년후 매년 마다 10000원씩 얼마?

S1 = 0
for n1 in range (1,21):
    S1 = S1 + a*r**n1
print (S1)
