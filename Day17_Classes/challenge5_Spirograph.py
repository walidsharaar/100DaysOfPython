import random
import turtle as tur

my_turtle = tur.Turtle()
my_turtle.speed("fastest")
tur.colormode(255)

def rand_color():
    r = random.randint(0,255)
    b=random.randint(0,255)
    g=random.randint(0,255)
    random_color = (r,g,b)
    return random_color

# draw the spirograph
def draw_spiro(gap_size):
    for _ in range(int(360/gap_size)):
        my_turtle.color(rand_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading()+gap_size)

draw_spiro(8)