#Name: Eva Yan
#Date: 18 Oct 2018
#Due Date: 12 Nov
#HW42: asks for CSV, name foutput file, creates a map with markers for all
#traffic collisios fom the imput file

csv_file = input("Enter CSV fie name: ")
output_file = input("Enter output file: " )

import folium
import pandas as pd

reader = pd.read_csv(csv_file)

mapNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

for index,row in reader.iterrows():
    tiles = "Cartodb Positron"
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapNY)

mapNY.save(outfile=output_file)

