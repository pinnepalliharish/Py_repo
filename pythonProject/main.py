from turtle import Turtle,Screen
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("white")
screen.title("SNAKE GAME")
screen.tracer(0)
x_Pos=[0,-20,-40]
seg=[]
for snakes in range(0,3):
    new_snake=Turtle("square")
    new_snake.color("black")
    new_snake.penup()
    new_snake.goto(x_Pos[snakes],0)
    seg.append(new_snake)
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_n in range(len(seg)-1,0,-1):
        new_x=seg[seg_n-1].xcor()
        new_y=seg[seg_n-1].ycor()
        seg[seg_n].goto(new_x,new_y)
    seg[0].forward(20)


screen.exitonclick()


