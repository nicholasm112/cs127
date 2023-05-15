#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 3, 2021

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#skip 5 rows because theres the source and information and stuff in the document
#that we don't need since its not part of the data set


pop.plot(x = "Year", y = "Bronx")

plt.show()

print("The largest number living in the Bronx is", pop["Bronx"].max())

print("The average number living in the Queens is", pop["Queens"].mean())




#Theres a groupby()  function in lab 6 and some other fucntions that we havent pre3viosley used
