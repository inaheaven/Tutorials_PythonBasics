import pandas as pd
import numpy as np

data = np.random.rand(2, 4, 5)
print(data)

p = pd.Panel(data)
print(p)

# data2 = np.random.rand(3, 2, 4, 5)
# print(data2)

data = {
    'item1' : pd.DataFrame(np.random.randn(4, 3)),
    'item2' : pd.DataFrame(np.random.randn(4, 2))
}
print(data)
p =pd.Panel(data)
print(p)
print(p['item1'])
print(p['item2'])
print(p.minor_xs(1))

print(p.major_xs(0))
print(p.major_xs(1))
print(p.major_xs(2))
print(p.major_xs(3))