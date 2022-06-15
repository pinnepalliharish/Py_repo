from turtle import Turtle
FONT = ("TimesRoman", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level : {self.level}", False, "left", FONT)
        self.hideturtle()

    def level_increment(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", False, "left", FONT)

    def hitting_a_car(self):
        self.penup()
        self.goto(-130, 0)
        self.write("OOPS ! HIT A CAR , GAME OVER", False, "left", FONT)
