#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 12, 2021

import matplotlib.pyplot as plt
import pandas as pd

user = input("Enter name of input file:")
mess = input("Enter name of output file:")

nick = pd.read_csv(user)
nick["Date"] = pd.to_datetime(nick["Date"].apply(str))
nick["Total"] = nick["Winner Pts"] + nick["Loser Pts"]
nick["% Points"] = ((nick["Winner Pts"]/nick["Total"])*100)
nick.plot(x = "Date", y = "% Points")
plt.show()
fig = plt.gcf()
fig.savefig(mess)

