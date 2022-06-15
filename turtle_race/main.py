from turtle import Turtle,Screen
import random
game_on=False
colors=["grey","yellow","green","red","blue"]
y_pos=[-80,-40,0,40,80]
screen=Screen()
screen.setup(width=500,height=400)
input=screen.textinput(title="welcome to turtle race !!:)", prompt="which color turtle will u choose ? : ").lower()
new_turtle=[]
for x in range(0,5):
    turtle= Turtle("turtle")
    turtle.color(colors[x])
    turtle.penup()
    turtle.goto(-230,y_pos[x])
    new_turtle.append(turtle)
if input:
    game_on=True
while game_on:
    for t in new_turtle:
        if t.xcor() > 230:
            game_on=False
            won_Color=t.pencolor()
            if input==won_Color:
                print(f"you've won ! the winning color is {won_Color}")
            else:
                print(f"you've lost, winning color is {won_Color}")
        rand_dis=random.randint(0,10)
        t.forward(rand_dis)
screen.exitonclick()