#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 3, 2021

import matplotlib.pyplot as plt
import pandas as pd

user = input("Enter name of input file:")
mess = input("Enter name of output file:")

nick = pd.read_csv(user)
ufo = nick.groupby("state")
init =(ufo["duration (seconds)"].mean())
z = init.sort_values(ascending=False)[:10] #this part of code given
#in programming assignment to select top 10 values
z.plot.bar()
plt.xlabel('State')
plt.ylabel('Seconds')
#plt.show()
fig = plt.gcf()
fig.savefig(mess)


