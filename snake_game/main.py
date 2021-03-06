from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.seg[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.seg[0].xcor() > 290 or snake.seg[0].xcor() < -290 or snake.seg[0].ycor() > 290 or snake.seg[0].ycor() < -290:
        game_is_on = False
        score.collision_with_wall()

    for segment in snake.seg[1:]:
        if snake.seg[0].distance(segment) < 10:
            game_is_on = False
            score.collision_with_tail()

screen.exitonclick()
