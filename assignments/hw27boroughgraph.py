#Name: Eva Yan
#Due Date: 22 October 2018
#Date: 25 Sep 2018
#This program modifies Lab 6 to ask the user for a borough, a name for an output
   #file, and displays the fraction of the population that has lived in that
   #borough, over time

#libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

#open the CSV, store in pop w/ skip first five rows
pop = pd.read_csv('nycHistPop.csv', skiprows=5)

selectBorough = input("Enter borough name: ")
outputfile = input("Enter output file name: ")

#compute fraction of population in borough chosen and save as new column,
  #'Fraction'
pop['Fraction'] = pop[selectBorough]/pop['Total']

#create plot of year vs fraction of pop in chosen borough w/labels
pop.plot(x='Year', y='Fraction')

#display the plot
#plt.show()

#save the image using the 'get current figure' function
fig = plt.gcf()
fig.savefig(outputfile)
