from turtle import Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PADDLE GAME")
screen.tracer(0)

r_paddle = Paddle(x=360, y=0)
l_paddle = Paddle(x=-360, y=0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "W".lower())
screen.onkey(l_paddle.down, "S".lower())
score_board = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 410:
        ball.refresh()
        score_board.increase_score_l_paddle()
    if ball.xcor() < -410:
        ball.refresh()
        score_board.increase_score_r_paddle()

screen.exitonclick()
