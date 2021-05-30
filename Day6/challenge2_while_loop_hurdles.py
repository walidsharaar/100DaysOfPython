# Suppose there is a robot and try to go to a destination but there are some barriers to jump on
# try to automate the jumping task inside writing the code one by one .
#Pretend Some functions are decalared before

# each time the wall placement differs

# 1 2 wall 3  wall 4 5 6 wall 7 8  9 10 wall 11 12 wall 13 14 Goal

def turn_left():
    print("Turn left!")

def turn_right():
    print("Turn Right!")

def jump():
    print("Jump!")

def move():
    print("Move!")

def is_wall():
    print("Wall!")

def goal():
    print("You Reached!")



while not goal():
    if is_wall():
        jump()
    else:
        move()
