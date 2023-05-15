#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 22, 2021


print("Please enter the conversion you want to do:")
print("'a' for Light-Year to Parsec conversion")
print("'b' for for Parsec to Light-Year conversion")

user = input("Your selection:")

if user == "a":
    Light = float(input("Please Enter a number of Light-Years:"))
    years =Light/3.26156
    print(Light,"Light-Years is equal to",years,"Parsecs.")

elif user == "b":
    Parsec = float(input("Please Enter a number of Parsecs:"))
    mess = 3.26156*Parsec
    print(Parsec,"Parsecs is equal to",mess,"Light-Years.")

#first time i did a program that gradescope acceptedon first try
