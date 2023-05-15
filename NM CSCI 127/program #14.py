#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 16, 2021

import turtle

thea = turtle.Turtle()
thea.shape("turtle")
user = input("Please enter a 6-digit hexadecimal number:")
nick = (("#")+user)
thea.color(nick)

for i in range(4):
    thea.left(90)
    thea.forward(100)
    thea.stamp()
#took me a while but i figure out how to add the hashtag in/ in gradescope and
#the program they never made it clear whether or not you have to include hashtag
