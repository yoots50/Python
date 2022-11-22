#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sympy as sp

x = sp.Symbol('x')
fx = sp.integrate(1/(x*(x+1)),x)
gx = sp.integrate((2*x-3)/(x**2-3*x+2))
print('(a) answer : ',fx,',(b) answer : ',gx)

