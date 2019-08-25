#CSci 127 Teaching Staff
#February 2018
#A template for a program that draws nested triangles 
#Modified by:  Eva Yan

import turtle
def setUp(t, dist, col):
    """
    Takes three parameters, a turtle, t, the distance, dist, 
    to move the turtle and a color, col, to set the turtle's color.
    """
    t.speed(1)
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def triangle(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 3 times:  moves forward that length, turns 120 degrees, 
    and calls triangle(t, length/2).
    """
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
        triangle(t, length/2)
#This works because it first draws the larger triangle,
        #then repeats/calls the entire function again
        #but for half the length until the "length"
        #value is 10 or less


def nestedTriangle(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 3 times:  moves forward that length, turns 120 degrees, 
    and calls nested triangle(t, length/2).
    """
    if length > 10:
        for i in range(3):
            t.forward(length)
            t.left(120)
            nestedTriangle(t, length/2)
#This works because as it draws each side of the larger triangle,
        #it also draws the smaller triangles within until
        #the side lengths of those triangles is 10 or less
        #in which case it continues to the next side (or range)


def main():
    n = int(input('Enter length: '))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    triangle(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    nestedTriangle(tess, n)

if __name__ == "__main__":
     main()
     
          
