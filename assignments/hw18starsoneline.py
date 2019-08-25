#Name: Eva Yan
#Date: Sep 14, 2018
#This program prints an opening statement and then asks the user for a number
   #and prints that many stars, one per line

print("The fault is in our stars...")


#Number of times * will be repeated, must make from string to integer
stars = int(input("Please enter a number: "))

for i in range(stars):
    print("*")
