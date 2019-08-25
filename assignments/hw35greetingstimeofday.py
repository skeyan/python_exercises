#Name: Eva Yan
#Date: Oct 5
#Due Date: Nov 1
#Hour of day in 24 hr time --> timely greetings

hour = int(input("Enter hour (in 24 hour time): "))

if hour < 12:
    print("Good Morning")
elif hour >= 12 and hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")
