import numpy as np
import csv

data = np.loadtxt("numpy_data.csv", delimiter=",", skiprows=2)
print(data)
print(data[:2])
print(data[:,:2])

names = ["xdata", "y1", "y2", "y3"]
data3 = np.genfromtxt("numpy_data.csv", dtype=None, delimiter=",", names=names)
print(data3.dtype.names)
print(data3)
print(data3["y1"])

