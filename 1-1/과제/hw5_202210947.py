import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,1001)
fx = np.zeros_like(x)

def f(x):
    if np.abs(x) < 1 :
        return 0
    if np.abs(x) > 1 :
        return x
    if x == 1 :
        return 1/2
    if x == -1 :
        return -1/2
        
for i in range(0,1001):
    fx[i] = f(x[i])

plt.plot(x,fx,'.')
plt.show
