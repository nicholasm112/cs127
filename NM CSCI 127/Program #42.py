#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 26, 2021

import folium


mapWorld = folium.Map(location=[40.75,-74.125],zoom_start=3)
newMarker = folium.Marker([40.7420577, -74.0101494], popup = "Little Island").add_to(mapWorld)
mapWorld.save(outfile="nycMap.html")

