from turtle import Turtle
import random
font = ["Courier", "Book Antiqua", "Bradley Hand ITC", "Comic Sans MS", "Forte", "Ink Free", "Tempus Sans ITC"]
FONT = (random.choice(font), 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Level {self.level}", align="center", font=FONT)
        self.goto(100, 260)
        self.write(f"Score {self.score}", align="center", font=FONT)

    def refresh(self):
        self.level += 1
        self.score += 2
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
