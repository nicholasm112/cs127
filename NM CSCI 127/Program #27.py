#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 3, 2021

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pop = pd.read_csv('covidCases.csv')

user = input("Enter borough name:")
nick = input("Enter output name:")


print("Min:", pop[user].min())
print("Max:", pop[user].max())
print("Mean:", pop[user].mean())
print("Median:", pop[user].median())
print("Standard Deviation:", pop[user].std())

pop["Fraction"] = pop[user]/pop["Case Count"]
pop.plot(x = "Date of Interest", y = "Fraction")
fig = plt.gcf()
fig.savefig(nick)

#plt.show()

# Case Count Date of interest variables were columns given in the data set from the
#csv file of those variables arent colums in that file you'll get an error

