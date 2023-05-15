#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 26, 2021

import folium
import pandas as pd

user = input("Enter CSV file name:")
mess = input("Enter output file:")
nick = pd.read_csv(user)

mapAttract = folium.Map(location = [40.768731, -73.964915])


for index,row in nick.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["NAME"]
    newMarker = folium.Marker([lon, lat], popup = name)
    newMarker.add_to(mapAttract)
    mapAttract.save(outfile = mess)
#long and lat needed to be switched
    
