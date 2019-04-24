import numpy as np
a = np.array([1,2,3,4])
print(a)
print(type(a))
print(a[-1])
print(a[-4])
print(a[1:2])

data = [[2,3,4],[5,6,7]]
a1 = np.array(data)
print(a1)
print(type(a1))
print(a1[0][0])
print(a1[0][1])
print(a1[1][2])
print(a1[1:2])
print(a1[0,])
print(a1[0,0])
print(a1[-2:])

data = [[2,3,4],[5,6,7], [8,9,10]]
a2 = np.array(data)
print(a2)
print(a2.shape)
x1 = a2[:, :-1]
print(x1)
x2 = a2[:, -1:]
print(x2)
x3 = a2[:-1, :]
print(x3)
x4 = a2[:-1, :-1]
print(x4)