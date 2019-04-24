import numpy as np
import pandas as pd

s = pd.Series(np.random.rand(4))
print(s)
print(s.axes)
print(s.empty)
print(s.ndim)
print(s.size)
print(s.values)

data2 = {
    'Name' : pd.Series(['tom', 'jane', 'jack', 'nick']),
    'Age'  : pd.Series([20,30,40,50]),
    'Rating': pd.Series([4.21, 4.34, 4.21, 4.11])
}

df = pd.DataFrame(data2)
print(df)
print(data2)

print(df.T)     #transpose
print(df.axes)
print(df.dtypes)

print(df.sum())
print(df.min())
print(df.mean())
print(df.std())
print(df.describe())

def adder(a,b):
    return a + b

N = 20
df = pd.DataFrame(np.random.randn(5,3), columns=['col1', 'col2', 'col3'])
print(df)
df.pipe(adder, 2)
print(df)
print(df.apply((np.mean)))

df = pd.DataFrame(
    {
        'A' : pd.date_range(start='2018-01-01', periods=N, freq='D'),
        'X' : np.random.rand(N),
        'DO': np.random.normal(100, 10, size=(N)).tolist()
    }
)

print(df)
df_reindexed = df.reindex(index=[0,2,5], columns=['A','C','B'])
print(df_reindexed)

df = pd.DataFrame(np.random.randn(6,3), columns=['col1', 'col2', 'col3'])
print(df)

df.rename(columns= {'col1': 'c1', 'col2': 'c2', 'col3': 'c3'}, index={0:'apple', 1:'banana', 2:'cabage'}, inplace='true')
print(df)