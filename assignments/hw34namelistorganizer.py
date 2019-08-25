#Name: Eva Yan
#Date: Oct 5
#Due Date: Oct 31
#List of names -> first name then last

#study

namelist = input("Please enter your list of names: ")
#namelist = "Epstein, Susan; St. John, Katherine; Vazquez-Abad, Felisa; Xu, Jia; Zamfirescu, Christina"
personlist = namelist.split('; ')
#personlist = ["Epstein, Susan", "St. John, Katherine", "Vazquez-Abad, Felisa", "Xu, Jia", "Zamfirescu, Christina"]
stringify = ""

for combo in personlist:
    stringify = stringify + combo + (', ')
#stringify = "Epstein, Susan, St. John, Katherine, Vazquez-Abad, Felisa, Xu, Jia, Zamfirescu, Christina"

print(stringify)

secondlist = stringify.split(', ')
#secondlist = ["Epstein", "Susan", "St. John", "Katherine", "Vazquez-Abad", "Felisa", "Xu", "Jia", "Zamfirescu", "Christina"]

print(personlist)
print(secondlist)

print("You entered: ")

for i in range(0, len(secondlist)-1, 2):
    print(secondlist[i+1], secondlist[i])
#rearranges it into correct firstname-lastname order
    #ex: Susan Epstein
    #skips forward by 2 to get to next last name (i)
    #Katherine St. John

print("Thank you for using my name organizer!")
    
