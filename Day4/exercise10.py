import pandas as pd
date = pd.date_range('1/1/2018', periods=5, freq='M')
print(date)

start = pd.datetime(2016,1,1)
end = pd.datetime(2016,3,2)
date = pd.date_range(start, end, freq = 'D')
print(date)

# freq = w: weekend, h: hour, b: businessday, s: second
