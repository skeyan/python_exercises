 #Name: Eva Yan
#Date: 11 Oct 2018
#HW 39 due 7 November
#Asks for a CSV of collision data and list top 3 contributing factors for
   #the primary vehicle of collisions

#Import pandas for reading and analyzing csv data
import pandas as pd

#Get input file name
filename = input("Enter CSV file name: ")

#Read the file to a dataframe
dataframe= pd.read_csv(filename)

print("Top three contributing factors for collisions:")
print(dataframe["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3])
#the above prints out the dataframe for the top 10 in the column specified above


