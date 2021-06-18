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

slide_num = 5

for _ in range(slide_num):
    angle = 360/slide_num
    my_turtle.backward(200)
    my_turtle.right(angle)