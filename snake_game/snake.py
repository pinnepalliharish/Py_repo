from turtle import Turtle

POS = ((0, 0), (-20, 0), (-40, 0))
MOVEMENT = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.seg = []
        self.create_snake()

    def create_snake(self):
        for snakes in POS:
            self.add_segment(snakes)

    def add_segment(self, snakes):
        new_snake = Turtle("square")
        new_snake.color("red")
        new_snake.penup()
        new_snake.goto(snakes)
        self.seg.append(new_snake)

    def extend(self):
        self.add_segment(self.seg[-1].position())

    def move(self):
        for seg_n in range(len(self.seg) - 1, 0, -1):
            new_x = self.seg[seg_n - 1].xcor()
            new_y = self.seg[seg_n - 1].ycor()
            self.seg[seg_n].goto(new_x, new_y)
        self.seg[0].forward(MOVEMENT)

    def up(self):
        if self.seg[0].heading() != DOWN:
            self.seg[0].setheading(UP)

    def down(self):
        if self.seg[0].heading() != UP:
            self.seg[0].setheading(DOWN)

    def right(self):
        if self.seg[0].heading() != LEFT:
            self.seg[0].setheading(RIGHT)

    def left(self):
        if self.seg[0].heading() != RIGHT:
            self.seg[0].setheading(LEFT)
