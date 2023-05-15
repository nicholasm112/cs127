#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 3, 2021

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

user = input("Enter name of input file:")
mess = input("Enter name of output file:")

nick = pd.read_csv(user)

nick["Fraction Single Adults"] = nick["Total Single Adults in Shelter"]/nick["Total Individuals in Shelter"]
nick.plot(x = "Date of Census", y  = "Fraction Single Adults")
plt.show()
fig = plt.gcf()
fig.savefig(mess)


            
