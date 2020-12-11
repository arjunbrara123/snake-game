from turtle import Screen
from snake import Snake
from food import Food
import time

# Initialise the screen and environment
screen_size = 600
screen = Screen()
screen.setup(width=screen_size, height=screen_size)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialise game componenets
snake = Snake()
pizza = Food(600)

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

    # Detect collision with food


screen.exitonclick()
