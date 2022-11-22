#!/usr/bin/env python
# coding: utf-8

# In[2]:


print ("이슬점 구하는 공식 코드입니다") #시작 메세지
Humid = float(input("습도를 입력하세요 : ")) #습도 입력
Temp = float(input("온도를 입력하세요 : ")) #온도 입력
import math
a = math.log(Humid / 100) #여기서 부터 이슬점 공식
b = 17.62 * Temp
c = 243.12 + Temp
d = b / c
e = a + d
f = 243.12 * e
g = 17.62 - e
Dewpoint = f / g #여기 까지 이슬점 공식
print ('이슬점은', Dewpoint, '입니다.') #결과


# In[ ]:




