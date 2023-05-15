#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: September 29, 2021


import numpy as np
import matplotlib.pyplot as plt

user = input("First image:")
nick = input("Second image:")
mess = input("Threshold:")

ca = plt.imread(user)
na = plt.imread(nick)
countSnow = 0
countsnow = 0
t = float(mess) #float used for decimal int used for whole number

for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
                countSnow = countSnow + 1
print("Snow count of first image is:", str(countSnow))

for i in range(na.shape[0]):
    for j in range(na.shape[1]):
        if (na[i,j,0] > t) and (na[i,j,1] > t) and (na[i,j,2] > t): 
                countsnow = countsnow + 1

print("Snow count of second image:", str(countsnow))

tess = (countSnow - countsnow)

print("Difference between first and second image:", str(tess))


# I got thtis program wrong a few times cause i didnt use float, int , str
# correctly
