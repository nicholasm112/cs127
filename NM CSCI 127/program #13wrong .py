#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 16, 2021


#Program needs to print name of book "by"  initial of author

myString = input("Enter a list of books and their authors:") #user input
nick = myString.split(";") #spltis each book/author combination

#print(nick[0])  #[0] takes the first set from the input
#string are immutable so i couldnt split it again unless i made it into another variable

book = nick[0].split(" - ") #splits the first name of book and name of author and takes
print((book[0]), "by", (book[1]))

acro = book[1]
init = ""
for nym in acro:
    init = init + nym[0]

print(init)
#simp = init.split(" ")    
#print(simp)
#print(simp[1])
simp = ""
for mess in init[0]:
    simp = simp + init[0]

cat  = ""
for intel in init[1]:
    cat = cat + init[1]

dog = ((simp),".",(cat))

print((book[0]), "by", (dog))



#name = book.split(" ") #Splits name into first and second name 

#len returns the lenth of a list 

    


#splits break input into list of words and list(whatever u want to split) breaks
#input into list of characters


#print(#variable, "by", variable)

print( "Thank you for using my book organizer!" )

#from quiz 4 if you have a statement and you want to print last word you would
#use interval [-x,len(varible)+1] /remember these index account for each character
#not each word

#splits break input into list of words and list(whatever u want to split) breaks
#input into list of characters
