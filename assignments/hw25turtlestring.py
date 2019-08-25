#Name: Eva Yan
#Date: Due Oct 18, 2018. Sep 20, 2018.
#This program takes a string as input and uses that string to control what the
#turtle draws on the screen. It uses the commands 'B' 'S' 'l' 'r' 'p' and more.

import turtle
matt = turtle.Turtle()

command = input("Enter a command string for turtle: ")

for chara in command:
    if chara == "B":
        matt.backward(50)
    elif chara == "S":
        matt.stamp()
    elif chara == "l":
        matt.left(45)
    elif chara == "r":
        matt.right(45)
    elif chara == "p":
        matt.pencolor("purple")
    elif chara == "F":
        matt.forward(50)
    elif chara == "L":
        matt.left(90)
    elif chara == "R":
        matt.right(90)
    elif chara == "^":
        matt.penup()
    elif chara == "v":
        matt.pendown()


        
