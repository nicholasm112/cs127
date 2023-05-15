#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 25, 2021

import random

huwin = 0 
cowin = 0
result = False 

while not result:
    x = input("Enter 1 for rock, 2 for paper and 3 for scissors:")
    playerMove = int(x)
    computerMove = random.randrange(1,4)
    print("computerMove:", computerMove)
    if playerMove > 3:
        print("winner = invalid")
    elif playerMove < 1:
        if cowin > huwin:
            print("game finished and winner is: computer")
        elif cowin < huwin:
            print("game finished and winner is: human")
        elif cowin == huwin:
            print("game finished and winner is: draw")
        result = False
    elif computerMove == playerMove:
        print("round finished and winner is: draw")
    elif computerMove == 1:
        if playerMove == 2:
            print("round finished and winner is: human")
            huwin = huwin +1 
        elif playerMove == 3:
            print("round finished and winner is: computer")
            cowin == cowin +1
    elif computerMove == 2:
        if playerMove == 1:
            print("round finished and winner is: computer")
            cowin = cowin +1
        elif playerMove ==3:
            print("round finished and winner is: human")
            huwin == huwin +1
    elif computerMove == 3:
        if playerMove == 1:
            print("round finished and winner is: human")
            huwin == huwin +1
        elif playerMove == 2:
            print("round finished and winner is: computer")
            cowin == cowin +1
   
#CORRECT CODE SUBMITTED ON GRADESCOPE WORKED WHEN I SWITHED INPUT TO X THEN MADE PLAYER = X
#ALSO HAD TO USE INT AND NOT PUT QUOTES AROUND NUMBER
