#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 16, 2021


rod = input("Enter a list of books and their authors:")
nick = rod.split("; ")
x = len(nick)
for c in range(0,x): #all inputs
    book = nick[c].split(" - ")  #split book from author for each pair

    for i in range(1): #matches number of imputs
        name = book[1].split(" ")  #split first and last name of author

        init = ""
        for i in name[0]:        #first name of author
            init = init + i
        #cat = init

        mess= ""
        for y in name[1]:        #second name of author
            mess = mess + y
        #dog = mess

        #auth = (init[0]+"."+mess[0]) 
        print(book[0],"by",(init[0]+"."+mess[0]+"."))

print("Thank you for using my book organizer!")


#spent hours trying to figure out what was wrong and then i realized that i missed
#a dot at the end of the authors intitials 
    
