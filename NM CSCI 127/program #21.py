#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 28, 2021

import numpy as np
import matplotlib.pyplot as plt #import libraries and arrays  

user = (input("Enter the size: ")) #input from user 
mess = input("Enter the output file:")
x = int(user)
Img2 = np.ones((x,x,3)) #create array and color channel



Img2[1::2,::2,0] = .94
Img2[1::2,::2,1] = .9               #rgb(74%,56%,56%)- Rosy Brown
Img2[1::2,::2,2] = .55              #rgb(94%,90%,55%)- khaki

Img2[:,1::2,0] = .73
Img2[:,1::2,1:3] = .56 

plt.imshow(Img2)
plt.show()
plt.imsave(mess, Img2)


#couldve enterd numbers like this but i didnt know at the time
#Img2[1::2,::2,:] = .94, .9, .55
#Img2[:,1::2,:] = .73, .56, .56
