import pandas as pd
import numpy as np

data= np.array(['a','b', 'c', 'd'])
p = pd.Series(data, index=[10,20,30,40])
print(p[10])

data1 = [[1,2],[2,3]]
d = pd.DataFrame(data1, columns=["Name", "Age"], index= ['first', 'second'], dtype=float)
print(d)
print(d['Name'])
print(d.loc['first'])