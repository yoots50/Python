#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

A = np.zeros((3,2))
sum = 0
for i in range(1,4):
    for j in range(1,3):
        A[i-1][j-1] = (i+2*j)
        sum += i+2*j

print(A)
print(sum)

