import numpy as np
import pandas as pd
data = {
    'one' : pd.Series([1,2,3], index= ['a','b','c']),
    'two' : pd.Series([1,2,3,4], index= ['a','b','c','d'])
}

df = pd.DataFrame(data)
print(df)
print(df['one'])
df['three'] = pd.Series([10,20,30], index=['a','b','c'])
print(df)
print(df['one'])
del df['one']
print(df)
df.pop('two')
print(df)
print(df.loc['a'])
print(df.iloc[1])
print(df[2:4])

df = pd.DataFrame([[1,2],[3,4]], columns = ['a','b'], index=[100,200])
print(df)
df2 = pd.DataFrame([[5,6],[7,8]], columns= ['a','b'], index=[100,200])
df = df.append(df2)
print(df)
df['c'] = pd.Series([9,10], index=[100,200])
print(df)
df = df.drop(100)
print(df)