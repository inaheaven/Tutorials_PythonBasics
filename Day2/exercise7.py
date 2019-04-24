import numpy as np

x = np.array([[1,2],[3,4],[5,6]])
print(x)
y = x[[0,1,2], [0,1,0]]
print(y)

x2 = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(x2)
print(x2[1:4, 1:3])

x3 = np.array([[0,1,2], [3,4,5], [6,7,8], [9,10,11]])
print(x3)

rows = np.array([[0,0], [3,3]])
print(rows)
cols = np.array([[0,2], [0,2]])
print(cols)

y3 = x3[rows, cols]
print(y3)

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[1:])
print(a[:,1:])
print(a[...,1])
print(a[...,1:])