import folium
import googlemaps
import pandas as pd
import numpy as np
df = pd.read_csv('chicagobestsandwich2.csv', index_col=0)
# print(df.head())

mykey = 'AIzaSyDTKbfF0BeYempdaV1buP5aJ9gw3lxRYYE'
gmaps = googlemaps.Client(key=mykey)

lat = []
lng = []
for n in df.index:
        target = df['address'][n] + ',' + 'Chicago'
        output = gmaps.geocode(target)
        location = output[0].get('geometry')
        lat.append(location['location']['lat'])
        lng.append(location['location']['lng'])

# print(len(lat))
# print(len(lng))

df['lat'] = lat
df['lng'] = lng

# print(df)

mapping = folium.Map(location=[df['lat'].mean(), df['lng'].mean()],zoom_start=11)
folium.Marker([df['lat'].mean(), df['lng'].mean()], popup='center').add_to(mapping)
mapping
