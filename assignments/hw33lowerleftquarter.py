#Name: Eva Yan
#Date: 5 Oct
#Due Date: 30 Oct
#This program asks the user for the name of an image, and name of an output file.
#It saves the lower left quarter of the image to the output file specified.

#note: this was done before lecture and might not be the right way to do it

#import packages for images and arrays
import matplotlib.pyplot as plt
import numpy as np

iimage = input("Enter image file name: ")
oimage = input("Enter output file: ")

#getting input image file
img = plt.imread(iimage) #read in the image from input file specified
#plt.imshow(img) #load image into pyplot
#plt.show() #show the image (waits until closed to continue)

#cropping the lower left quarter of the image for output
dim = img.shape
x = int(dim[0]) #height
y = int(dim[1]) #width
newx = int(x/2) 
newy = int(y/2)

# img1 = img[newx:x,newy:y] #this takes the lower right quarter
# img1 = img[0:newx,newy:y] #this takes the top right quarter

#ok why the heck did this work
#it's because the first value is up-down, and the second left-right
img1 = img[newx:x, 0:newy]

plt.imshow(img1)
plt.show()

plt.imsave(oimage, img1)
