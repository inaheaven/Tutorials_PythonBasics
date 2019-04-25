import numpy as np
import pandas as pd
import folium
import googlemaps

data = pd.read_csv('data.csv', thousands=',', encoding='euc-kr')
print(data)

mykey = 'your google map key'
gmaps = googlemaps.Client(key=mykey)
print(gmaps.geocode('서울중부경찰서', language='ko'))


police_name = []
police_address= []
police_lat = []
police_lng = []

for name in data['관서명']:
    police_name.append('서울'+str(name[:-1])+'경찰서')

print(police_name)

for name in police_name:
    tmp = gmaps.geocode(name, language='ko')
    police_address.append(tmp[0].get('formatted_address'))
    tmp2 = tmp[0].get('geometry')
    police_lat.append(tmp2['location']['lat'])
    police_lng.append(tmp2['location']['lng'])

print(len(police_lat))
print(len(police_lng))

print(police_address)