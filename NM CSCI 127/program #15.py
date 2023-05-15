#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 22, 2021

#This program loads an image, displays it, and then creates, displays,
#    and saves a new image that has only the red channel displayed.

#Import the packages for images and arrays:

import matplotlib.pyplot as plt
import numpy as np


inputfile = input("Enter name of the input file:")
outputfile = input("Enter name of the output file:")

img = plt.imread(inputfile)   #Read in image from csBridge.png
plt.imshow(img)		                 #Load image into pyplot
plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image          #Set the green channel to 0#Set the blue channel to 0
img2[:,:,2] = 0

plt.imshow(img2)         #Load our new image into pyplot
plt.show()              #Show the image (waits until closed to continue)

plt.imsave(outputfile, img2)  #Save the image we created to the file: reds.png

#most of code copied from lab 3, both plt.show() has to be taken out when submitting
#


