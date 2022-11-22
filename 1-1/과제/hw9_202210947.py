#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
a = np.array([1,1,1])
b = np.array([1,2,3])
c = np.array([3,2,1])
k = 3

print(np.dot((a+b),c))
print(np.dot(a,c)+np.dot(b,c))
print(np.dot((k*a),b))
print(k*np.dot(a,b))
print(np.dot(a,(k*b)))

