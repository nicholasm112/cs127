#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 15, 2021

nick = input("Enter a word: ") #input from user
finalmess = ""  #needed later after changing each character
                                #to bring it back together


for c in nick:
    offset = ((ord(c)- ord("A")) + 13) #how many letters past a 
    wrap = offset % 26 #if larger than 26 numbers wrap back to start/ letter a
    newchar = (chr((ord("A") + wrap)))   #gets final letters
    finalmess = finalmess + newchar     #puts everything together 


print( "Your word in code is:", finalmess)
    



# this code was in the lecture 2 slides slide 60 basically.
#remember to use correct CAPITALIZATION and to count perenthesis 
