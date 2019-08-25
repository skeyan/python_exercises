#Name: Eva Yan
#Date: Sep 14, 2018
#This program: asks the user for the name of a png and prints the # of pixels
   #that are nearly white (r/g/b fractions all above .75)

#import pkgs for images and arrays
import matplotlib.pyplot as plt
import numpy as np

filename = input("Enter file name: ")

pic = plt.imread(filename) #read in image
countSnow = 0 #number of pixels almost white set to 0 for now
t = .75 #threshhold for almost white, can adjust between 0 and 1.0

#for every pixel
for i in range(pic.shape[0]):
    for j in range(pic.shape[1]):
        if (pic[i,j,0] > t) and (pic[i,j,1] > t) and (pic[i,j,2] > t):
            countSnow = countSnow + 1

print("Snow count is", countSnow)
