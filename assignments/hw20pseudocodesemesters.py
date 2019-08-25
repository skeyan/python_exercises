#Name: Eva Yan
#Date: Sep 14, 2018
#This program:
#1.  Ask the user for the number of days until the end of the semester.
#2.  Print out the weeks until the end of the semester (weeks = days // 7)
#3.  Print out the leftover days (leftover = days % 7)

numDays = int(input("Enter number of days: "))

numWeeks = numDays//7 #Note: the // is floor division which removes the decimals
#since we should not have weeks with decimals in this case

leftover = numDays % 7

print("Weeks: ", numWeeks)
print("Days: ", leftover)
