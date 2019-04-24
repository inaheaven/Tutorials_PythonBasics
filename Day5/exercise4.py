import pandas as pd
import numpy as np
seoul_cctv = pd.read_csv('seoul_cctv.csv', encoding='utf-8')
print(seoul_cctv)
print(seoul_cctv.head(1))
print(seoul_cctv.columns)
print(seoul_cctv.columns[0])
seoul_cctv.rename(columns = {seoul_cctv.columns[0] : '구별'}, inplace=True)
print(seoul_cctv)


print(seoul_cctv.head())
print(seoul_cctv.sort_values(by='소계', ascending=False).head(3))
seoul_cctv['최근증가율'] = (seoul_cctv['2016년']+ seoul_cctv['2015년']+seoul_cctv['2014년'])/seoul_cctv['2013년도 이전'] * 100
print(seoul_cctv)



seoul = pd.read_excel('populationSeoul.xls', encoding='utf-8', header=2, usecols='B, D, G, J, N')
print(seoul.head())
seoul.rename(columns={seoul.columns[0]:'구별',
                    seoul.columns[1]:'인구수',
                    seoul.columns[2]:'내국인',
                    seoul.columns[3]:'외국인',
                    seoul.columns[4]:'고령자'}, inplace=True)
print(seoul)
print(seoul.head())
print(seoul['구별'].unique())
seoul[seoul['구별'].isnull()]
seoul.drop([0], inplace=True)
seoul.drop([], inplace=True)
print(seoul)
seoul['외국인비율'] = seoul['외국인']/seoul['인구수'] * 100
seoul['고령자비율'] = seoul['고령자']/seoul['인구수'] * 100
print(seoul.sort_values(by='인구수', ascending=False))

result = pd.merge(seoul_cctv, seoul, on='구별')
del result['2013년도 이전']
del result['2014년']
del result['2015년']
del result['2016년']

print(result)
result.set_index(result['구별'], inplace=True)
print(result)

import matplotlib.pyplot as plt
t = np.arange(0, 12, 0.01)
y = np.sin(t)
y1 = np.cos(t)
plt.plot(t,y, 'r--', label='sin')
plt.plot(t,y1, 'o', label="cos")
plt.grid()
plt.legend()
plt.xlabel('time')
plt.ylabel('height')
plt.title('test demo')
# plt.figure(figsize=[100,60])
plt.show()

s1 = np.random.normal(loc=0, scale=1, size=1000)
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)

plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()

plt.subplot(411)
plt.subplot(423)
plt.subplot(424)
plt.subplot(425)
plt.subplot(426)
plt.subplot(437)
plt.subplot(438)
plt.show()

print(result['소계'])
plt.plot()
result['소계'].plot(kind='barh', grid=True)
plt.show()

plt.figure(figsize=(6,6))
plt.scatter(result['인구수'], result['소계'], s=50)
plt.show()