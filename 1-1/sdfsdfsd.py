'''
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.1,4,401)
y1 = np.log(x1)
x2 = np.linspace(-0.9,4,501)
y2 = np.log(x2+1)-1

plt.plot(x1,y1,label='$y=log_2(x)$')
plt.plot(x2,y2,label='$y=log_2(x+1)-1$')
plt.legend(loc='upper left')
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-1,np.pi-1,501)
y1 = np.sin(2*(x1+1))
x2 = np.linspace(0,2*np.pi,501)
y2 = -3*np.cos(x2)+1

plt.plot(x1,y1,label='$sin$')
plt.plot(x2,y2,label='$cos$')
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt
def f (x) :
    return np.sin(x)
def T1 (x) :
    return x
def T2 (x) :
    return T1(x)-(1/6)*x**3
def T3 (x) :
    return T2(x)+(1/120)*x**5
def T4 (x) :
    return T3(x)-(1/5040)*x**7

x = np.linspace(-np.pi,np.pi,1001)
y = f (x)
y1 = T1 (x)
y2 = T2 (x)
y3 = T3 (x)
y4 = T4 (x)

graph, = plt.plot(x,y)
graph1, = plt.plot(x,y1)
graph2, = plt.plot(x,y2)
graph3, = plt.plot(x,y3)
graph4, = plt.plot(x,y4)

plt.legend(handles=(graph, graph1, graph2, graph3, graph4), labels = ('$y=sin(x)$','$y=T_1(x)$','$y=T_2(x)$','$y=T_3(x)$','$y=T_4(x)$'))
plt.show()
