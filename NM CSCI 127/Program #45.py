#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 26, 2021

import folium
import pandas as pd

user = input("Please enter the name of the input file:")
mess = input("Please enter the name of the output file:")
nick = input("Please enter the name of the borough:")
unit = pd.read_csv(user)
groupdata = unit.groupby("City").get_group(nick)
MapWifi = folium.Map(Location = [40.768731, -73.964915])

for index,row in groupdata.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Location"]
    newMarker = folium.Marker([lat, lon], popup =name)
    newMarker.add_to(MapWifi)
MapWifi.save(outfile = mess)
#needed to switch lat and lon and use location not name
