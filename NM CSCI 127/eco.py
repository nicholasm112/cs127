import pandas as pd
import matplotlib.pyplot as plt
#weekday
nick = pd.read_csv("sodatax-hw.csv")
x = nick["Price_Tinicum_aftertax"].mean()
y =  nick["Price_Philly_aftertax"].mean()
print(y)
z  = y - x
print(z)
plotdata = pd.DataFrame(
    {"Average price in location after tax" : [x, y]},
    index = ["Tinicum", "Philly"])
plotdata.plot(kind = "bar")



plt.xlabel("Location Average")
plt.ylabel("Average price after tax")
#plt.show()
#fig = plt.gcf()
#fig.savefig("sodatax")
