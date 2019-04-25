from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import urllib
import ssl
from tqdm import tqdm_notebook

# This restores the same behavior as before.
context = ssl._create_unverified_context()

url_base = "https://movie.naver.com/"
url_sub = "movie/sdb/rank/rmovie.nhn?sel=cur&date=20180428"
page = urlopen(url_base+url_sub, context=context)
soup = BeautifulSoup(page, "html.parser")

print(soup.find_all('div', 'tit5')[0])
print(soup.find_all('div', 'tit5')[0].a)
print(soup.find_all('div', 'tit5')[0].a.string)

print(soup.find_all('td', 'point')[0].string)
print(soup.find_all('div', 'tit5'))

movies = [soup.find_all('div','tit5')[inx]for inx in range(0, 49)]
# print(movies)
movies = [soup.find_all('div','tit5')[inx].a.string for inx in range(0, 49)]
# print(movies)
point = [soup.find_all('td','point')[inx].string for inx in range(0, 49)]
# print(point)

date = pd.date_range('2018-04-01', periods = 28, freq='D')
# print(date)
movie_date = []
movie_name = []
movie_point = []

for selectedDate in tqdm_notebook(date):
    url_base = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date={date}"
    temp = urlopen(url_base.format(date=urllib.parse.quote(selectedDate.strftime('%Y%m%d'))), context=context)
    # print(url_base.format(date=urllib.parse.quote(selectedDate.strftime('%Y%m%d'))))
    soup = BeautifulSoup(temp, "html.parser")
    # print(soup)
    # point = [soup.find_all("td", 'point')[inx].string for inx in range(0,10)]
    # print(point)
    end = len(soup.findAll('td','point'))
    movie_date.extend([selectedDate for n in range(0, end)])
    movie_name.extend([soup.findAll('div','tit5')[n].a.string for n in range(0, end)])
    movie_point.extend([soup.findAll('td','point')[n].string for n in range(0, end)])


movie = pd.DataFrame({'date': movie_date, 'name': movie_name, 'point': movie_point})
print(movie.head())

movie.sort_values(by='point', ascending=True)
print(movie.head())

# print(movie['date'])
# print(movie['point'])
# print(movie.iloc[0])
data = movie.query('name == ["덕구"]')
data1 = movie.query('name == ["원더"]')
import matplotlib.pyplot as plt
plt.figure(figsize=(6,3))
plt.plot(data['date'], data['point'])
plt.plot(data1['date'], data1['point'])
plt.gca().invert_yaxis()
plt.grid()
plt.legend()
plt.show()