import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move_forward, "Up")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_generation()
    car_manager.movement()

    if player.ycor() > 280:
        player.refresh()
        car_manager.increase_speed()
        scoreboard.level_increment()

    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.hitting_a_car()

screen.exitonclick()
