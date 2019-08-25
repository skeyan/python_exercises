#Name: Eva Yan
#Date: Sep 14, 2018
#This program colors part of the floodmap gray
   #(color the region of the map with elevation greater
   #than 6 feet and less than or equal 20 feet above sea
   #level the color grey (50% red, 50% green, and 50% blue)

#Import libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

#Readin the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take shape/dimensions of the elevations and add another
   #dimension to hold the 3 color channels
mapShape = elevations.shape + (3,)

#create blank map
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] > 6:
            if elevations[row,col] <= 20:
               floodMap[row,col,0] = .5
               floodMap[row,col,1] = .5
               floodMap[row,col,2] = .5
        if elevations[row,col] <= 0:
            #below sea
            floodMap[row,col,2] = 1.0
        elif elevations[row,col] <= 6:
            #below storm surge, flooding likely
            floodMap[row,col,0] = 1.0
        if elevations[row,col] > 20:
            floodMap[row,col,1] = 1.0

#Load the array into matplotlib.pyplot:
plt.imshow(floodMap)

#Display the plot:
plt.show()

#Save
plt.imsave('floodMap.png', floodMap)
