# numpy slicing

import numpy as np

x1 = np.arange(10)
print(x1)

s = slice(2,7,2)
s2 = slice(0,5)
print(x1[s])
print(x1[2:7:2])
print(x1[s2])
print(x1[0:5])