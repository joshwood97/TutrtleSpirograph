import turtle as t
import random

josh = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


josh.speed("fastest")

def draw_spirohraph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        josh.color(random_color())
        josh.circle(100)
        josh.setheading(josh.heading() + size_of_gap)

draw_spirohraph(5)

screen = t.Screen()
screen.exitonclick()
