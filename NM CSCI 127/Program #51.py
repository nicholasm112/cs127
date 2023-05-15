#Name: Nicholas Luke Morgan 
#Email: nicholas.morgan12@myhunter.cuny.edu
#Date: October 25, 2021

ADDI $s0, $zero, 100 #sets s0 to 100
ADDI $s1, $zero, 25  # sets s1 to 25
AGAIN: SUB $s0, $s0, $s1 #Subtract $s1 from $s0 and store result in $s0 (i.e. $s0 = $s0 - $s1).
BEQ $s0, $zero, DONE
J AGAIN
DONE: 
