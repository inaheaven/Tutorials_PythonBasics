import numpy as np
import pandas as pd

unsorted_df = pd.DataFrame({'col1': [2,1,1,1], 'col2': [1,3,2,4]})
print(unsorted_df)
sorted_df = unsorted_df.sort_values(by='col1', ascending=False)
print(sorted_df)
sorted_df2 = unsorted_df.sort_values(by=['col1', 'col2'], ascending=False)
print(sorted_df2)

print(pd.get_option('display.max_rows'))
(pd.set_option('display.max_rows', 100))
print(pd.get_option('display.max_rows'))

df = pd.DataFrame(np.random.randn(8, 4), index=['a','b','c','d','e','f','g','h'], columns=['A','B','C','D'])
print(df)
print(df.loc[:,'A'])
print(df.iloc[:,-1:])
print(df.loc[:,['A','C']])
print(df.loc['a':'f', 'A':'B'])