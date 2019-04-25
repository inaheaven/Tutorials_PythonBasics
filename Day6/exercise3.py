from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen
import urllib
import re
from urllib.parse import urljoin
from tqdm import tqdm_notebook

url_base = 'http://www.chicagomag.com/'
url_sub = 'Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/'
page = urlopen(url_base+url_sub)
soup = BeautifulSoup(page, 'html.parser')

# print(soup)

list_soup = soup.findAll('div', 'sammy')
# print(list)

rank = []
main_menu = []
cafe_name = []
url_link = []

for item in tqdm_notebook(list_soup):
    rank.append(item.find(class_='sammyRank').string)
    temp = item.find(class_='sammyListing').getText()
    main_menu.append(re.split(('\n|\r\n'), temp)[0])
    cafe_name.append(re.split(('\n|\r\n'), temp)[1])
    url_link.append(urljoin(url_base, item.find('a')['href']))
print(rank)
print(main_menu)
print(cafe_name)
print(url_link)
# print(len(rank))
# print(len(main_menu))
# print(len(cafe_name))
# print(len(url_link))

data = {'rank':rank, 'menu': main_menu, 'name': cafe_name, 'url': url_link}
df = pd.DataFrame(data, index=rank, columns=['name','menu','url'])
df.to_csv('chicagobestsandwich1.csv', sep=',', encoding='utf-8')

