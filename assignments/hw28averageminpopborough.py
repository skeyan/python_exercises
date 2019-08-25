#Name: Eva Yan
#Due Date: 23 October 2018
#Date: 25 Sep 2018
#This program computes the average and max population over time for a chosen
   #borough

#libraries for plotting and data processing:
import matplotlib.pyplot as plt
import pandas as pd

#open the CSV, store in pop w/ skip first five rows
pop = pd.read_csv('nycHistPop.csv', skiprows=5)

#chosen borough by user
selectBorough = input("Enter borough name: ")

#print average
print('Average population: ', pop[selectBorough].mean())

#print max
print('Maximum population: ', pop[selectBorough].max())

