# Not sure what to do now? Enter your mips code here 
# and hit step (to run one line at a time) or 
# hit run (to run them all at once)

# Keep an eye on the register and stack tracker
# to see what changes are being made to them.

# If you want to preload the stack or some registers
# with data, you can click on them to change edit them.

# If you would like more infomation, check out the user
# guide linked in the menu.


ADDI $s0, $zero, 10
ADDI $s1, $zero, 9
SB $s0, -10($sp)
SB $s1, -9($sp)
LB $s2, -9($sp)
ADDI $sp, $sp, -1
ADDI $sp, $sp, -2
ADDI $sp, $sp, -3
ADDI $sp, $sp, -5
ADDI $sp, $sp, -9
ADDI $sp, $sp, -14
ADDI $sp, $sp, -23
ADDI $sp, $sp, -37
LB $s3, 0($sp)
