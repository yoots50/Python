import numpy as np
import matplotlib.pyplot as plt
x = np.linspace (0.1,5,501)
fx = (np.log(x)/np.log(3))**2-(np.log(x**4)/np.log(3))+3
plt.plot(x, fx)
plt.show()
