#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 12, 2021

import matplotlib.pyplot as plt
import pandas as pd

user = input("Enter file name:")
nick =  pd.read_csv(user)#vgsales.csv
x = nick["Rank"].max()
print("There are",x,"total games")
print(nick["Genre"].value_counts())
print(nick["Publisher"].value_counts()[:3])
print(nick["Genre"].count())
#Doesnt say it in programming challenge but you need to print total number of
#genres as well. Gradescope tells you that you need it and won't give you full
#credit until you do

