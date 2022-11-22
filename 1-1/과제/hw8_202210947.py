#!/usr/bin/env python
# coding: utf-8

# In[25]:


import sympy as sp

x = sp.Symbol('x')

answer1 = sp.simplify(sp.integrate((sp.exp(2*x)/(sp.exp(x)+1)),(x,0,2))-sp.integrate(1/(sp.exp(x)+1),(x,0,2)))
answer2 = sp.simplify(sp.integrate(sp.Abs(sp.sin(x)),(x,-1*sp.pi,sp.pi)))
answer3 = sp.simplify(sp.integrate(x*sp.sqrt(x**2+2),(x,1,3)))
answer4 = sp.simplify(sp.integrate(sp.exp(x)*sp.sin(x),(x,0,sp.pi/2)))

print(answer1)
print(answer2)
print(answer3)
print(answer4)

