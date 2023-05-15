#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 25, 2021

import numpy as np
import matplotlib.pyplot as plt

print("-------------------------------------------------\n\
    Welcome to the Color Maker!\n\
    -------------------------------------------------\n\
    Please enter for each rbg color the value in which to increase/decrease them.\n\
    If all 3 values given are 0, the program will end and save the resulting image.")
user = input("Enter outfile name: ")
rnew = 0
gnew = 0
bnew = 0
r = 1
g = 1
b = 1
while not (r == 0 and g == 0 and b == 0):
    r = int(input("How much do you want to change the red value by? ")) 
    g = int(input("How much do you want to change the green value by? "))
    b = int(input("How much do you want to change the blue value by? "))
    
    rnew = rnew + r/255
    gnew = gnew + g/255
    bnew = bnew + b/255
    if rnew > 1:
        rnew = 1
    if rnew < 0:
        rnew = 0
    if gnew > 1:
        gnew = 1
    if gnew < 0:
        gnew = 0
    if bnew > 1:
        bnew = 1
    if bnew < 0:
        bnew = 0
    print("The current rgb values are:", [rnew,gnew,bnew])

    
        
Img2 = np.zeros((10,10,3))
Img2[:,:,0] = rnew
Img2[:,:,1] = gnew
Img2[:,:,2] = bnew
print("You're done! Congrats on the color, it looks beautiful!") 
plt.imsave(user, Img2)
                



    
