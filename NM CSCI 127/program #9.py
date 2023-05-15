#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 15, 2021

nick = input("Enter a phrase: ") #user input
print( "Reversed phrase:", nick[::-1]) #reversed phrase given by user

mess= nick.upper() # made input uppercase
acro= mess.split(" ") #split user input at each space/between each word
                                 #since () have only have a space in it

init= "" #need a blank so that no additional input is given when
                       #trying to get only first letter

for nym in acro: #Started a loop of uppercase split input
    init = init + nym[0] #takes first letter of each word plus init
                            #which is nothing
print( "Last letters of reversed words:", init[::-1])
#printed capital reversed first letter
