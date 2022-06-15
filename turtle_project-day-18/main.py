import turtle
from turtle import Turtle,Screen
import random
tim=Turtle()
tim.shape("classic")

turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors
def siporograpf(size):
    for _ in range(int(360/size)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tilt=tim.heading()
        tim.setheading(tilt+size)
siporograpf(5)

screen=Screen()
screen.exitonclick()


