import numpy as np

a = np.empty([3,2], dtype=int)
print(a)
a1 = np.zeros([3,2], dtype=float)
print(a1)
a2 = np.ones([3,2], dtype=int)
print(a2)
a3 = np.asarray(a2, dtype=float)
print(a3)
a4 = np.arange(0, 20, 4, float)
print(a4)
a5 = np.arange(10)
print(a5)
s5 = slice(2,10,3)
print(a5[s5])
print(a5[2:10:3])

a6 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a6)
print(a6.shape)
print(a6.dtype)
print(a6.size)
print(a6[1:])
print(a6[1:,:-1])

a7 = np.array([[1,2],[4,5], [6,7]])
print(a7)
print(a7[0])
print(a7[1])
print(a7[2])
a8 = a7[2]
print(a8)


#     0   1
# -------------
# 0   1   2
# 1   4   5
# 2   6   7
a9 = a7[[0,1,2], [0,1,0]]
print(a9)

a10 = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(a10.shape)
r10 = np.array([[0,0],[3,3]])
c10 = np.array([[0,2],[0,2]])
result = a10[r10, c10]
print(r10)      #0,0    3,3
print(c10)      #0,2    0,2
print(result)
print(a10[r10])
print(a10[c10])
print(a10[[[0,0],[3,3]],[[0,2],[0,2]]])
a11 = a10[1:4, 1:3]
print(a11)

#   0   1   2
# -------------
# 0 0   1   2
# 1 3   4   5
# 2 6   7   8
# 3 9   10  11


a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print(c)

d = np.array([[1,2,3,4],[5,6,7,8]])
e = np.array([2,2,2,2])

f = d + e
print(f)