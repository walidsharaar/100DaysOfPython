import random
from turtle import Turtle

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.turtlesize(3)
my_turtle.color("red")


for _ in range(4):

    my_turtle.forward(100)
    my_turtle.right(90)

# dash line
for _ in range(15):
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()

# create different shapes
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
slide_num = 5
def draw_shape(slide_num):
    angle = 360 / slide_num
    for _ in range(slide_num):
        my_turtle.forward(200)
        my_turtle.right(angle)

# generate the shapes
for shape_side_no in range(3,11):
    my_turtle.color(random.choice(colours))
    draw_shape(shape_side_no)


# draw random move
# directions = [east,north,west,south]
my_turtle.pensize(20)
my_turtle.speed("fastest")
directions =[0,90,180,270]
for _ in range(200):
    my_turtle.forward(30)
    my_turtle.color(random.choice(colours))
    my_turtle.setheading(random.choice(directions))

