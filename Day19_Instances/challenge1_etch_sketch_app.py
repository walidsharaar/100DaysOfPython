from turtle import Turtle,Screen

my_turtle = Turtle()
screen = Screen()


def move_on():
    my_turtle.forward(10)

def move_back():
    my_turtle.backward(10)

def move_right():
    new_heading= my_turtle.heading()-10
    my_turtle.heading(new_heading)

def move_left():
    new_heading= my_turtle.heading()+10
    my_turtle.heading(new_heading)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen.listen()
screen.onkey(move_on,"Up")
screen.onkey(move_back,"Down")
screen.onkey(move_right,"Right")
screen.onkey(move_left,"Left")
screen.onkey(clear,"c")



screen.exitonclick()