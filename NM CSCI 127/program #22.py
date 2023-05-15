#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 29, 2021

import turtle
turtle.colormode(255)
nick = turtle.Turtle()
nick.speed(0)
nick.pensize(5)
wn = turtle.Screen()
wn.bgcolor("khaki")


for i in range(36):
    nick.pencolor(0,i*7,0)
    nick.forward(10)
    nick.left(10)
    for x in range(4):
        nick.left(90)
        nick.forward(300)
        nick.backward(50)
