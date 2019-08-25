#Name: Eva Yan
#Date/Users/evayan/Desktop/CSCI127/hw26topographicmap.py: Oct 19, 2018
#Done: Sep 21, 2018
#This program creates a topographic map of the map from Lab 4

#Import libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

#Readin the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take shape/dimensions of the elevations and add another
   #dimension to hold the 3 color channels
mapShape = elevations.shape + (3,)

#create blank map
topoMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            topoMap[row,col,0] = 0
            topoMap[row,col,1] = 0
            topoMap[row,col,2] = 1
        elif (elevations[row,col]%10) == 0:
            topoMap[row,col,0] = 0
            topoMap[row,col,1] = 0
            topoMap[row,col,2] = 0
        else:
            topoMap[row,col,0] = .5
            topoMap[row,col,1] = .5
            topoMap[row,col,2] = .5

#Load the array into matplotlib.pyplot:
plt.imshow(topoMap)

#Display the plot:
plt.show()

#Save
plt.imsave('topo.png', topoMap)

            
            
