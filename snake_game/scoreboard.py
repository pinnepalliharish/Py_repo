from turtle import Turtle
ALIGNMENT = "center"
FONT = ("TimesRoman", 12, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto((0, 270))
        self.write(f"SCORE = {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE = {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def collision_with_wall(self):
        self.goto(0, 0)
        self.color("red")
        self.write("OOPS! SNAKE HIT THE WALL :( ", False, ALIGNMENT, FONT)
        self.goto(0, -20)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def collision_with_tail(self):
        self.goto(0, 0)
        self.color("red")
        self.write("OOPS! SNAKE HIT HIMSELF :( ", False, ALIGNMENT, FONT)
        self.goto(0, -20)
        self.write("GAME OVER", False, ALIGNMENT, FONT)
