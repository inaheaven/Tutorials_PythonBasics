import numpy as np

a = np.arange(0,60,5)
print(a)
print(a.shape)
a1 = a.reshape(4,3)
print(a1)

for x in np.nditer(a1):
    print(x)

for x in a1:
    for y in x:
        print(y)

b = np.arange(0,24,3,int)
b1 = b.reshape(2,4)
print(b1)


# 1d -> 2d
c = np.array([1,2,3,4,5])
print(c.shape)
c1 = np.reshape(c.shape[0], 1)
print(c1.shape)
print(c1)

# 2d -> 3d
d = np.array([[10,11], [12,13],[14,15]])
print(d.shape)
d1 = d.reshape(d.shape[0], d.shape[1], 1)
print(d1.shape)
print(d1)
