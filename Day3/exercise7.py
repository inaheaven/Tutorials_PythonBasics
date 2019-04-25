import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

data2 = np.array(['a','b','c','d'])
s2 = pd.Series(data2, index=[100, 200, 300, 400])
print(s2)

data3 = {'a':0, 'b':1, 'c':2}
s3 = pd.Series(data3)
print(s3)
s4 = pd.Series(data3, index=['b','c','d', 'a'])
print(s4)

s5 = pd.Series(5, index=['a','b','c','d'])
print(s5)
print(s5[:2])
print(s5['b'])


#data frame
df = pd.DataFrame()
print(df)

data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

data2 = [["Alex",2], ["Bob",4],["Charles",6]]
df =pd.DataFrame(data2, columns=['Name', 'Age'], dtype=float)
print(df)

data3 = {'Name': ['Alex', 'Bob', 'Charles'], 'Age': [10,20,30]}
df =pd.DataFrame(data3)
print(df)

data4 = [{"a":1, "b":2, "c":3}, {"d":4,"e":5,"f":6}, {"d":7,"e":8,"f":9}]
df = pd.DataFrame(data4)
print(df)

data5 = {'one' :pd.Series([1,2,4]), 'two':pd.Series([2,4])}
df = pd.DataFrame(data5)
print(df)
print(df['one'])
df['three'] = pd.Series([3,4,5])
print(df)

del df['two']
print(df)
print(df.iloc[2])
print(df[1:2])
data = np.random.rand(2,4,5)
pa = pd.Panel(data)
print(pa)

data = {
            'item1' : pd.DataFrame(np.random.randn(4,3)),
            'item2' : pd.DataFrame(np.random.randn(4,2))}
pa = (pd.Panel(data))
print(pa)
print(data)