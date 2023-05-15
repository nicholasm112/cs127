#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: August 31, 2021

import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("khaki")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("darkblue")
tess.pensize(5)

alex = turtle.Turtle()           # create alex
alex.color("violet")
alex.pensize(5)

tess.forward(100)                 # make alex draw a square
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(100)
tess.left(90)

alex.left(90)
alex.forward(100)

alex.right(30)
alex.forward(100)                 # Let tess draw an equilateral triangle
alex.right(120)
alex.forward(100)
alex.right(120)
alex.forward(100)
                   # complete the triangle

                  # turn tess around
                 # move her away from the origin



wn.exitonclick()
