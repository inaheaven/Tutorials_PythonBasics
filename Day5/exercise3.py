import numpy as np
from matplotlib import pyplot as plt
x = [5, 8, 10]
y = [12,14,6]

x2 = [6, 9, 11]
y2 = [6, 14, 8]

plt.bar(x, y, align='center')
plt.bar(x2, y2, color='r')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.show()


a = np.array([22, 87, 5, 43, 56, 55, 54, 11, 20, 51, 5, 59])
hist, bins = np.histogram(a, bins=[0, 20, 40, 60, 80, 100])
print(hist)
print(bins)

plt.hist(a, bins=[0,20,40,60,80,100])
plt.show()