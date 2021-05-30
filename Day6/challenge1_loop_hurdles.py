# Suppose there is a robot and try to go to a destination but there are some barriers to jump on
# try to automate the jumping task inside writing the code one by one .
#Pretend Some functions are decalared before

def turn_left():
    print("Turn left!")

def turn_right():
    print("Turn Right!")

def jump():
    print("Jump!")

def move():
    print("Move!")

# after each two number the robot has to jump over
# 1 2 wall 3 4 wall 5 6 wall 7 8 wall 9 10 wall 11 12 wall 13 14 Goal

for step in range(6):
    jump()