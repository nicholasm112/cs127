#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 16, 2021

import turtle

turtle.colormode(255)
nick = turtle.Turtle()
nick.shape("turtle")       #make sure your pen is always up or down when needed
nick.penup()

nick.backward(100)      #needed to back up for the assignment

nick.pendown()

for i in range(255,0,-10):   #becuase i needed i to decrease the color but 
    nick.pensize(255-i) #increase pensize the - and signs are there so it works
    nick.forward(10)
    nick.color(255,i,0)
    
nick.pensize(0)   #resets color and pensize 
nick.penup()
nick.color(0,0,0)

for i in range(0,255,10):
    nick.backward(10)  #brings it back 


nick.pendown()
nick.right(90)



for i in range(255,0,-10):   #draws second thing
    nick.pensize(255-i)
    nick.forward(10)
    nick.color(255,i,0)
#Code took a while because for some reason i had to do penup and change color and
#pensize before going back even though penup so those things shouldnt need to
#change until pen goes back down but this worked in the end 
