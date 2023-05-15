#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 28, 2021

import matplotlib.pyplot as plt
import numpy as np

logoImg = np.ones((30,30,3))#30 by 30 array,all white and 3 color channels

logoImg[:,:6,1] = 0
logoImg[:6,5:30,1] = 0
logoImg[6:15,25:30,1] = 0                            #first 5 rows and colums have no green but have 100% red and blue
logoImg[15:21,6:30,1] = 0 # adds other part of p

logoImg[21:30,6:30,:] = 0
logoImg[6:15,6:25,:] = 0

plt.imshow(logoImg)         #Load our new image into pyplot
plt.show() 
plt.imsave("logo.png", logoImg)









     
