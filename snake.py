from turtle import Turtle, Screen
import time

# Constants
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
SNAKE_COL = "white"


class Snake:

    def __init__(self, size=2):
        """Initialise the snake object"""
        self.nagini = []
        self.size = size
        for i in range(self.size):
            self.grow()
        self.head = self.nagini[len(self.nagini) - 1]  # Set the lead turtle as the snake 'head'

    def move(self, screen_size=600, add=0):
        """Move the entire snake forward"""
        edge_limit = (screen_size / 2) - 20
        for donatello in range(len(self.nagini) - 1):
            self.nagini[donatello].setpos(self.nagini[donatello + 1].pos())
            self.nagini[donatello].setheading(self.nagini[donatello + 1].heading())
        self.head = self.nagini[len(self.nagini) - 1]
        if abs(self.head.xcor()) >= edge_limit:
            if self.head.heading() == LEFT or self.head.heading() == RIGHT:
                self.head.setx(-self.head.xcor())
        if abs(self.head.ycor()) >= edge_limit:
            if self.head.heading() == UP or self.head.heading() == DOWN:
                self.head.sety(-self.head.ycor())
        self.head.forward(20)

        #Check for weird cross hatching bug and ensure snake is always on same side!
        if self.head.heading() == LEFT or self.head.heading() == RIGHT:
            for donatello in range(len(self.nagini) - 1):
                if self.nagini[donatello].ycor() != self.head.ycor():
                    self.nagini[donatello].sety(self.head.ycor())
        if self.head.heading() == UP or self.head.heading() == DOWN:
            for donatello in range(len(self.nagini) - 1):
                if self.nagini[donatello].xcor() != self.head.xcor():
                    self.nagini[donatello].setx(self.head.xcor())

    # Function to grow the snake
    def grow(self):
        donatello = Turtle(shape="square")
        donatello.color(SNAKE_COL)
        donatello.shapesize(1)
        donatello.penup()
        if len(self.nagini) > 0:
            self.head = self.nagini[len(self.nagini) - 1]
            donatello.setpos(self.head.xcor(), self.head.ycor())
            donatello.setheading(self.head.heading())
            donatello.forward(20)
        self.nagini.append(donatello)
        self.head = donatello

    # Functions to turn the snake in a different direction
    def up(self):       self.move_dir(UP)
    def down(self):     self.move_dir(DOWN)
    def left(self):     self.move_dir(LEFT)
    def right(self):    self.move_dir(RIGHT)

    def move_dir(self, dir):
        """Move the snake, checking it isn't doubling back on itself first"""
        if int(self.head.heading()) != ((dir + 180) % 360):
            self.head.setheading(dir)
            self.move()
        else:
            self.illegal_move()

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