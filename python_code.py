import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

source = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text

soup=BeautifulSoup(source, 'html5lib')

postal_codes_dict = {}for table_cell in soup.find_all('td'):
    try:
        postal_code=table_cell.p.b.text
        postal_code_investigate=table_cell.span.text
        neighborhoods_data=table_cell.span.text
        borough=neighborhoods_data.split('(')[0]
        if neighborhoods_data == 'Not assigned':
            neighborhoods = [] else:
                postal_codes_dict[postal_code]={} try:
                    neighborhoods=neighborhoods_data.split('(')[1]
                    neighborhoods=neighborhoods.replace('(','')
                    neighborhoods=neighborhoods.replace(')','')
                    neighborhoods_names=neighborhoods.split('/')
                    neighborhoods_clean=','.join([name.strip()for name in neighborhoods_clean = borough
                        postal_codes_dict[postal_code]['neighborhoods']= neighborhoods_clean
                        except:
                        pass
columns= ['PostalCode', 'Borough', 'Neighborhood']
toronto_data = pd.DataFrame(columns=columns)
toronto_data

for ind,postal_code in enumerate
(postal_codes_dict):
borough = postal_codes_dict[postal_code]['borough']
neighborhood = postal_codes_dict[postal-code]['neighborhoods']
toronto_data = toronto_data.append({"PostalCode":postal_code, "Borough":borough,
    "Neighborhood":neighborhood},
    ignore_index=True)
toronto data.shape[0]

import geocoder
lat_lng_coords = None

while (lat_lng_coords is None):
g=geocoder.google('{}, Toronto, Ontario'.format (postal_code)}
lat_lng_coords = g.latlng

latitude = lat_lng_coords[0]
longitude = lat_lng_coords [1]











