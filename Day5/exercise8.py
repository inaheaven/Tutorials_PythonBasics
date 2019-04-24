

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import ssl

# This restores the same behavior as before.
context = ssl._create_unverified_context()

url = "https://www.basketball-reference.com/draft/NBA_2014.html"
html = urlopen(url, context=context)
soup = BeautifulSoup(html, 'html.parser')



name = []
college = []

player_data = []
table = soup.findAll("tr")[2:]
for i in range(len(table)):
    player_row = []
    for td in table[i].findAll('td')[2:4]:
        player_row.append(td.getText())
    player_row.append(player_row)

df = pd.DataFrame(player_data, columns=['player', 'college'])
print(df)