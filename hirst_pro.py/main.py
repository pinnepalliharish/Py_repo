import turtle
from turtle import Screen,Turtle

import random
turtle.colormode(255)
tim=Turtle()

colors_list=[(197, 165, 119), (144, 81, 56), (220, 201, 138), (61, 95, 121), (165, 150, 54), (136, 162, 180), (131, 34, 23),
        (52, 119, 87), (73, 37, 29), (190, 96, 82), (145, 177, 150), (100, 76, 80), (165, 147, 157), (21, 92, 68),
        (28, 59, 75), (225, 177, 167), (59, 44, 46), (133, 29, 33), (180, 202, 179), (26, 84, 89), (88, 147, 129),
        (13, 70, 58), (42, 65, 89), (180, 99, 102), (216, 181, 186), (182, 191, 204)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.speed(1000)
no_of_dots=100
for dots in range(1,no_of_dots+1):
    tim.dot(20,random.choice(colors_list))
    tim.forward(50)
    if dots%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen=Screen()
screen.exitonclick()