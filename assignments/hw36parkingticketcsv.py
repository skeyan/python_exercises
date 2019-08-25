#Name: Eva Yan
#Date: 10 Oct 2018
#HW 36 due 2 November

#Import pandas for reading and analyzing CSV data:
import pandas as pd

#get input and attribute column
ifile = input("Enter file name: ")
atrib = input("Enter attribute: ") #ask for column in data to search by

csvFile = ifile #Name of the CSV file up to input
someval = pd.read_csv(csvFile) #Read in the file to a dataframe
#print(tickets)

print("The 10 worst offenders are:")
print(someval[atrib].value_counts()[:10]) #print out the dataframe for top 10

#note: the thing on the bottom with the name and dtype is done automatically?

