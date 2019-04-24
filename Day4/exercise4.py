import numpy as np
import pandas as pd

path = "/Volumes/MicroSd/Workspace/Python_Workspace/Python_Tutorial/Day4/FAO+database.csv"
data = pd.read_csv(path, encoding='utf-8')

# print(data)
# print(type(data))
# print(data.shape)
# print(data.ndim)
# print(data.head(2))
# print(data.tail(10))
# print(data.dtypes)
# print(data.describe())
# print(data['Y1961'].describe())
# print(data['Area'].describe())
# print(data.iloc[0])
# print(data.sum())
# print(data.mean())
print(data['Y2001'].describe())
# print(data.drop(columns="Area"))
data2 = (data.rename(columns = {'Area': 'Place'}))
print(data2)
print(data)
data.rename(columns = {'Area': 'PL'}, inplace='true')
print(data)

data.to_csv("output_tmp.csv", index = False, encoding='utf-8')

import matplotlib.pyplot as plt
data['latitude'].plot(kind='hist', bins=100)
plt.xlabel('Latitude Value')