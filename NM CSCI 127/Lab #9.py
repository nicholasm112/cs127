#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 26, 2021

import folium
import pandas as pd

#mapWorld = folium.Map(location=[0,0],zoom_start=1)

#mapWorld.save(outfile="tempMap.html")


#The higher the zoom value the more its zoomed in and zoom start is the center
#point of map #popup funtion creates a name for 

cuny = pd.read_csv('CUNYcampuses.csv')
print(cuny["Campus"])

mapCUNY = folium.Map(location=[40.768731, -73.964915])

for index,row in cuny.iterrows():#itterrows lets you itterrate betweeen rows of cuny
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    newMarker = folium.Marker([lat, lon], popup = name)
    newMarker.add_to(mapCUNY)
    mapCUNY.save(outfile='cunyLocations.html')
