'''
You are going to write a virtual coin toss program.
It will randomly tell the user "Heads" or "Tails".
e.g.
1 means Heads
0 means Tails
'''
# use random module
import random

value = random.randint(0,1)

if value == 1:
    print("It is head")
else:
    print("It is tail")


