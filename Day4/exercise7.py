import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(10,4), index= pd.date_range('2018-01-01', periods=10), columns=['a','b','c','d'])
print(df)

print(df.rolling(window=8).mean())



df = pd.DataFrame(np.random.randn(5,3), index=['a','b','c', 'd', 'e'], columns=['one', 'two', 'three'])
print(df)
df = df.reindex(['a','z','b','c','d','e','f','g','h'])
# print(df)
# print(df['one'].isnull())
# print(df['one'].sum())

print(df.fillna(3))
print(df.dropna())
print(df)

data = {
    'Team' : ['Warriors', 'Cavaliers', 'Warriors', 'Rockets'],
    'Rank' : [1,2,3,4],
    'Year' : [2014, 2015, 2016, 2017],
    'Points': [30, 30, 30, 30]
}
df = pd.DataFrame(data)
print(df)
df1 = df.groupby(['Team', 'Year']).groups
print(df1)
df2 = df.groupby(['Team', 'Year'])
for name, group in df2:
    print(name)
    print(group)