# numpy

import numpy as np

a = np.array([1,2,3])
print(a)
print(a.shape)

a1 = np.array([[1,2],[3,4]])
print(a1)

a2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a2)
print(type(a2))
print(a2.shape)

a3 = np.array([[1,2,3],[4,5,6]])
print(a3)
print(a3.shape)
print(a3.data)
print(a3.dtype)


a4 = np.array([[1.2, 2, 3.5], [2.1, 3, 4.3]])
print(a4)
print(a4.dtype)

a5 = np.array([[1,2,3],[4,5,6]])
print(a5.shape)

a6 = np.arange(24)
print(a6)
print(a6.size)
print(a6.flags)

a7 = np.empty([3,2], dtype=np.int)
print(a7)

a8 = np.zeros((3,2), dtype=np.int)
print(a8)

a9 = np.arange(5,200,5,dtype=float)
print(a9)
