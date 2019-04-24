import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(4,3), columns=['col1', 'col2', 'col3'], index=[4,3,2,1])
print(df)

for key, value in df.iteritems():
    print(key, value)

df2 = df.sort_index()
print(df2)

df3 = pd.DataFrame(np.random.randn(4,3), columns=['col1', 'col2', 'col3'], index=[1,2,3,4])
df4 = df3.sort_index(ascending=False)
print(df3)
print(df4)