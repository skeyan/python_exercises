#Name: Eva Yan
#Date: 24 Oct
#Due Date: 16 Nov
#HW 46

import turtle
import random

tracy = turtle.Turtle()
tracy.speed(10)

for i in range(100):
    tracy.forward(10)
    a = random.randrange(0,360)
    tracy.right(a)
