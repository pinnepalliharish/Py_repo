from turtle import  Turtle

ALIGNMENT = "center"
FONT = ("TimesRoman", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 270)
        self.write(f"SCORE = {self.l_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 270)
        self.write(f"SCORE = {self.r_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score_r_paddle(self):
        self.r_score += 1
        self.update_scoreboard()

    def increase_score_l_paddle(self):
        self.l_score += 1
        self.update_scoreboard()