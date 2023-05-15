#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 3, 2021

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

user = input("Enter file name:")
nick = pd.read_csv(user)
#df["Stars"] = pd.to_numeric(df["Stars"], downcast="float")
print("The average stars per serving style:", nick.mean())
groupeddata = nick.groupby("Style")


print(groupeddata["Stars"].mean())
Singapore = nick.groupby("Country").get_group("Singapore")
groupedData = nick.groupby("Country")
row = Singapore["Stars"].idxmin()
x = (nick["Brand"][row])
print(x, "has the lowest rating in Singapore with",Singapore["Stars"].min(), "stars")

#Already got 5/5 by just printing KOKA at beginning instead of writing code to
#get it from the list
#didnt get the exact code right but got close ill ask at tutoring some other day
#groupby and get group info was in lab 6 as well as how to create graphs
#regular division returns a float use integer divsion to return an integer
#Lecture 6 shows how to index dimensions from an image when doing the hunter
#sign
#correct program now got tutoring for it 
