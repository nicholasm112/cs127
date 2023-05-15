#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 16, 2021

import turtle          #import turtle

turtle.colormode(255)    # Allows colors to be given from 0 to 255
nick= turtle.Turtle()    # named nick 
nick.shape("turtle")     #turtle shape
nick.penup()             


nick.left(60)

nick.pendown()

for i in range(0,255,10):        #draws yellow lightbulb thing
    nick.forward(10)
    nick.pensize(i)
    nick.color(i,i,0)
    
nick.penup()

for i in range(255,0,-10): #reset pensize color distance
    nick.backward(10)
    

nick.pensize(0)    # for some reason resetting pensize and color using the for 
nick.color(0,0,0)  # i in range wasn't working using nick.pensize(i) and 
                   # nick.color(i,i,0) so i set everthing to 0 & it worked
nick.left(60)      #

nick.pendown()


for i in range(0,255,10):   #draws another lightbulb thing
    nick.forward(10)
    nick.pensize(i)
    nick.color(i,i,0)


