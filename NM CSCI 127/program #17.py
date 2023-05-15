#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 22, 2021

user = int(input("Enter number of stamps the turtle will print: "))
import turtle
nick = turtle.Turtle()
turtle.colormode(255)
nick.shape("circle")
nick.penup()
nick.color(186,164,145)
nick.speed(0)
steps = 10

for i in range(user):
    nick.pendown()
    nick.stamp()
    nick.penup()
    m = ((i*3) +3)
    y = (steps + (2*i)+2)
    if (m+186) <= 255:
        nick.color(m+186,m+164,m+145)
    nick.forward(y)
    nick.right(24)
    
    
    
    
