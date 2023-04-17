from turtle import Turtle , Screen

my_turtle = Turtle()
screen = Screen()

def move_on():
    my_turtle.forward(10)


screen.listen()
screen.onkey(key="space",fun=move_on)
screen.exitonclick()