from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.chicagomag.com/Chicago-Magazine/November-2012/Best-Sandwiches-Chicago/"
import pandas as pd
import re
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
# print(soup.title())
# print(soup.body)

# links = soup.find_all('div', 'sammyListing')
# # links = soup.find_all('div', class_='sammyListing')
# # print(links)
#
# for list in links:
#     print(list.get_text())
#
# temp = soup.find(class_='sammyListing').get_text()
# print(temp)
# re.split('\n|\r\n', temp)[0]
# re.split('\n|\r\n', temp)[1]

# print(temp)


rank = []
main_menu = []
cafe_name = []
url_add = []

list_soup = soup.find_all('div', 'sammy')
for item in list_soup:
    rank.append(item.find(class_='sammyRank').get_text())
    temp = item.find(class_='sammyListing').get_text()
    main_menu.append(re.split('\n|\r\n', temp)[0])
    cafe_name.append(re.split('\n|\r\n', temp)[1])
print(rank)
print(temp)
print(main_menu)
print(cafe_name)

data = {'Name': cafe_name, 'Menu': main_menu}
df = pd.DataFrame(data, index=rank, columns={'Name', 'Menu'})
print(df.head())