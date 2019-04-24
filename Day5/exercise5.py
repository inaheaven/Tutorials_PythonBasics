import pandas as pd
import numpy as np
data = pd.Series([1,3,4, np.nan, 6, 8])
print(data)

dates = pd.date_range('20130101', periods=6, freq='M')
print(dates)
data2 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=['A','B','C', 'D'])
print(data2)
print(data2.columns)
print(data2.values)
print(data2.info)
print(data2.describe())
print(data2.sort_values(by='B', ascending=False))
print(data2['A'])
print(data2[0:3])
print(data2['20130102':'20130303'])
