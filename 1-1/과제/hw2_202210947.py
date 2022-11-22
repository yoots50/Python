#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import matplotlib.pyplot as plt
def f(x) :
    if x <= -1 :
        return x + 2
    if x > -1 :
        return x**2
x = np.linspace(-5,5,1000)
fx = np.zeros_like(x)
for i in range (0,1000):
    fx[i] = f(x[i])
plt.plot(x,fx,'.')
plt.show

