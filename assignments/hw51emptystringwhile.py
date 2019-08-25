#Eva Yan
#Date: Nov 1
#Due: Nov 28
#HW 51: empty string

check = input("Enter a non-empty string: ")

while check == "":
    print("That was empty. Try again.")
    check = input("Enter a non-empty string: ")

print("You entered: ", check)
