from turtle import Turtle, Screen
import time

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:



    def __init__(self, size=3):
        self.nagini = []
        self.size = size
        for i in range(self.size):
            donatello = Turtle(shape="square")
            donatello.color("white")
            donatello.shapesize(1)
            donatello.penup()
            self.nagini.append(donatello)

    def move(self):
        for donatello in range(len(self.nagini) - 1):
            self.nagini[donatello].setpos(self.nagini[donatello + 1].pos())
            self.nagini[donatello].setheading(self.nagini[donatello + 1].heading())
        donatello = self.nagini[len(self.nagini) - 1]
        donatello.forward(20)

    def up(self):
        donatello = self.nagini[len(self.nagini) - 1]
        if donatello.heading() != DOWN:
            donatello.setheading(UP)
        else:
            self.illegal_move()

    def down(self):
        donatello = self.nagini[len(self.nagini) - 1]
        if donatello.heading() != UP:
            donatello.setheading(DOWN)
        else:
            self.illegal_move()

    def left(self):
        donatello = self.nagini[len(self.nagini) - 1]
        if donatello.heading() != RIGHT:
            donatello.setheading(LEFT)
        else:
            self.illegal_move()

    def right(self):
        donatello = self.nagini[len(self.nagini) - 1]
        if donatello.heading() != LEFT:
            donatello.setheading(RIGHT)
        else:
            self.illegal_move()

    def illegal_move(self):
        screen = Screen()
        for donatello in self.nagini:
            donatello.color("red")
        screen.update()
        time.sleep(0.5)
        for donatello in self.nagini:
            donatello.color("white")
        screen.update()

    def dir_move(self, x, y):
        for i in range(len(self.nagini) - 1):
            self.nagini[i].setpos(self.nagini[i + 1].pos())
        snake_head = self.nagini[len(self.nagini) - 1]
        snake_head.setpos(snake_head.xcor() + x * 20, snake_head.ycor() + y * 20)
