from turtle import Turtle, Screen
import time

# Constants
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
SNAKE_COL = "white"


class Snake:

    def __init__(self, size=7):
        """Initialise the snake object"""
        self.nagini = []
        self.size = size
        for i in range(self.size):
            donatello = Turtle(shape="square")
            donatello.color(SNAKE_COL)
            donatello.shapesize(1)
            donatello.penup()
            self.nagini.append(donatello)
        self.head = self.nagini[len(self.nagini) - 1]  # Set the lead turtle as the snake 'head'

    def move(self):
        """Move the entire snake forward"""
        for donatello in range(len(self.nagini) - 1):
            self.nagini[donatello].setpos(self.nagini[donatello + 1].pos())
            self.nagini[donatello].setheading(self.nagini[donatello + 1].heading())
        donatello = self.nagini[len(self.nagini) - 1]
        if abs(donatello.xcor()) >= 300: donatello.setx(-donatello.xcor())
        if abs(donatello.ycor()) >= 300: donatello.sety(-donatello.ycor())
        donatello.forward(20)

    # Functions to turn the snake in a different direction
    def up(self):       self.move_dir(UP)
    def down(self):     self.move_dir(DOWN)
    def left(self):     self.move_dir(LEFT)
    def right(self):    self.move_dir(RIGHT)

    def move_dir(self, dir):
        """Move the snake, checking it isn't doubling back on itself first"""
        if int(self.head.heading()) != ((dir + 180) % 360):   self.head.setheading(dir)
        else:                                                   self.illegal_move()

    def illegal_move(self):
        """Flash the snake red to show the move was illegal"""
        screen = Screen()
        for donatello in self.nagini:   donatello.color("red")
        screen.update()
        time.sleep(0.5)
        for donatello in self.nagini:   donatello.color(SNAKE_COL)
        screen.update()

    # Currently unused user controls
    def jump_up(self):      self.jump_dir(0, 1)
    def jump_down(self):    self.jump_dir(0, -1)
    def jump_left(self):    self.jump_dir(-1, 0)
    def jump_right(self):   self.jump_dir(1, 0)

    def jump_dir(self, x, y):
        """Move snake without changing heading"""
        snake_head = self.nagini[len(self.nagini) - 1]
        snake_head.setpos(snake_head.xcor() + x * 20, snake_head.ycor() + y * 20)