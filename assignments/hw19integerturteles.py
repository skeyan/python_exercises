#Name: Eva Yan
#Date: Sep 14, 2018
#This program: Write a program that asks the user
   #for 5 whole (integer) numbers. For each number,
   #turn the turtle left the degrees entered and then
   #the turtle should move forward 100.

one = int(input("Enter a number: "))
two = int(input("Enter a number: "))
three = int(input("Enter a number: "))
four = int(input("Enter a number: "))
five = int(input("Enter a number: "))

combine = [one, two, three, four, five]

import turtle

yasha = turtle.Turtle()

for i in combine:
    yasha.left(i)
    yasha.forward(100)


