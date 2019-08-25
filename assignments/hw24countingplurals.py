#Name: Eva Yan
#Date: due Oct 17, 2018
#This program counts the number of plural nouns and returns fraction plural

this = input("Enter nouns: ") #This returns a STRING
#print(this)
#print(type(this))

wordsplit = this.split() #splits the nouns in the string, "this" into a LIST
#so you can isolate each word to check
#print(wordsplit)

#prints the number of total words in the list
print("Number of words: ", len(wordsplit))

new = 0

#accounts for all nouns except the last one
#counting the number of 's ' works because it's like "bananas orange peaches"
   #this is not wordsplit
increase = this.count('s ')
new = new + increase #counts the number of plural nouns as it checks the list

#accounts for last noun because there is no space after the 's'
last = wordsplit[-1]
if last[-1] == 's': #if last letter of the last word is 's'
    new = new + 1 #it's plural as well

#fraction
new = new/len(wordsplit)

print("Fraction of your list that is plural is", new)

        
