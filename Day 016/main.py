from turtle import *
from prettytable import *


#construct object

turtle=Turtle()
print(turtle)
turtle.shape("turtle")
turtle.color("DarkOrange")
turtle.forward(100)

screen = Screen()
print(screen.canvheight)
screen.exitonclick()

# construct the pretty table object

table = PrettyTable()
table.add_column("Name",["A","B","C"])
table.add_column("Job",["Software","Hardware","HR"])
table.add_column("Department",["IT","IT","HR"])



print(table)

