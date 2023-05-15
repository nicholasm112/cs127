#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 25, 2021

import random

def Rules(playerMove):
    if playerMove > 3:
        winner = "invalid"
    if playerMove < 1:
        return False
    

def Gamelogic(computerMove, playerMove):
    
    while not playerMove < 1 and playerMove > 3:
        if computerMove == playerMove:
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
            elif playerMove == 3:
                print("round finished and winner is: human")
                huwin == huwin +1
        elif computerMove == 3:
            if playerMove == 1:
                print("round finished and winner is: human")
                huwin == huwin +1
            elif playerMove == 2:
                print("round finished and winner is: computer")
                cowin == cowin +1
    while playerMove < 1 and playerMove > 3:
        Rules(playerMove)
    
    
    



def main():

    huwin = 0 
    cowin = 0
    
    result = False
    while not result:
        playerMove = (int(input("Enter 1 for rock, 2 for paper and 3 for scissors:")))
        computerMove = random.randrange(1,4)
        print("computerMove:", computerMove)
        Gamelogic(computerMove, playerMove)

if __name__ == '__main__':
    main()

#PROBABLY COULDVE GOTTEN THIS TO WORK BUT IT WAS EASIER TO JUST USE ONE FUNCTION

