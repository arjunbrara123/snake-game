from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, screen_size):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh(screen_size)

    def refresh(self, screen_size):
        edge_limit = (screen_size / 2) - 20
        rand_x = random.randint(-edge_limit, edge_limit)
        rand_y = random.randint(-edge_limit, edge_limit)
        self.goto(rand_x, rand_y)
