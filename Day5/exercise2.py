import numpy as np
from matplotlib import pyplot as plt



x = np.arange(1, 11)
print(x)
y = 2*x+5
print(y)
plt.title("test plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,y, ":") # , o, v, ob 등으로 표현 가능
plt.show()

x1 = np.arange(0,3 * np.pi, 0.1)
y1 = np.sin(x1)
plt.plot(x1, y1)
plt.show()

x2 = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x2)
y_cos = np.sin(x2)
plt.subplot(2, 1, 1)
plt.plot(x2, y_sin)
plt.subplot(2, 1, 2)
plt.plot(x2, y_cos)
plt.show()