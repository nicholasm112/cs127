#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: August 31, 2021
#This program draws a nonagon using the turtle module

#Imports the turtle command to use below:
import turtle

#Create a turtle, named: nick
nick = turtle.Turtle()

#Repeat 6 times:
for i in range (9):
    nick.forward(100) #move nick forward 100 steps
    nick.left(40)     #turn nick 40 degrees to the left
