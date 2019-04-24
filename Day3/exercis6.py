import numpy as np

names = np.array(['tom', 'joe', 'will', 'thomas'])
print(names)
data = np.random.rand(7,4)
print(data)
print(names == 'tom')
print(data[data<0])
data[data < 0] = 0
print(data)


arr = np.empty((8,4))
print(arr)
for i in range(8):
    arr[i] = i
print(arr[[4,3,0,6]])


arr2 = np.random.randn(6)
print(arr2)
arr2.sort()
print(arr2)