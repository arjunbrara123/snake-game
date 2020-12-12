from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self, screen_size):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.refresh(0, screen_size)
        self.speed(0)

    def refresh(self, score, screen_size):
        self.clear()
        self.goto(0, (screen_size / 2) - 30)
        self.write("Score = " + str(score), True, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)

    def debug_mode(self):
        self.goto(0, 0)
        self.color("red")
        self.write("DEBUGGING MODE", True, align="center", font=FONT)