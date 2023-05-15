#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: August 31, 2021

import turtle

nick = turtle.Turtle()

nick.color("purple")
nick.shape("arrow")
nick.pensize(3)

nick.forward(30)
for i in range(3):
    for i in range(3):
         nick.forward(50)
         nick.right(120)

    nick.backward(30)
    nick.right(90)
    nick.forward(30)

for i in range(3):
    nick.forward(50)
    nick.right(120)

nick.backward(30)
