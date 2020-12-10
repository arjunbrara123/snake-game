import time
from turtle import Screen
from snake import Snake

# Initialise game setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()

# Set keyboard game controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Give the user a key to quit the game
def esc_game():  screen.bye()
screen.onkey(esc_game, "Escape")

# Start the game running
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
