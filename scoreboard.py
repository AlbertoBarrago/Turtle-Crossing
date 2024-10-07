from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.speed(0)
        self.scoreboard.penup()
        self.scoreboard.goto(-280, 250)
        self.score = 0
        self.high_score = 0
        self.scoreboard.write(f"Your Score: {self.score}", font=FONT)

    def update_score(self):
        self.score += 1

