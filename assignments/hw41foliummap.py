#Name: Eva Yan
#Date: 18 Oct 2018
#Due Date: 9 Nov
#HW 41 writes a program that uses folium to make a map of NYC including a
#marker for hte main campus of Hunter College

#Import folium package for making maps
import folium
#Import pandas
import pandas as pd

#Create a map centered a (40.75, -74.125) and zoom out a bit
mapNY = folium.Map(location=[40.75, -74.125],zoom_start=10)

#Add marker for Hunter
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapNY)

#Save the map
mapNY.save(outfile="nycMap.html")





