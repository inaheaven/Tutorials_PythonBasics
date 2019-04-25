from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import urllib
import re
from urllib.parse import urljoin
from tqdm import tqdm_notebook

df = pd.read_csv('chicagobestsandwich1.csv', index_col=0)
address = []
price = []
# urls = df['url']
# for url in urls:
#     # print(url)
#     html = urlopen(url)
#     soup = BeautifulSoup(html, 'html.parser')
#     data = soup.findAll('p', 'addy')
# print(data)
# print("!")

for n in tqdm_notebook(df.index):
    html = urlopen(df['url'][n])
    temp = BeautifulSoup(html, 'lxml')
    gettings = temp.find('p', 'addy').get_text()
    price.append(gettings.split()[0][:-1])
    address.append(' '.join(gettings.split()[1:-2]))

df['price'] = price
df['address'] = address

df = df.loc[:, ['name', 'menu', 'price', 'address', 'url']]
df.to_csv('chicagobestsandwich2.csv', sep=',', encoding='utf-8')