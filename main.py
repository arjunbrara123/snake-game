from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Initialise the screen and environment
screen_size = 600
score = 0
screen = Screen()
screen.setup(width=screen_size, height=screen_size)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
scoreboard = Scoreboard(screen_size)

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
    snake.move(0)

    # Detect collision with food
    if snake.head.distance(pizza) <= 15:
        pizza.refresh(screen_size)
        score += 1
        scoreboard.refresh(score, screen_size)
        # snake.grow()
        print("Michelangelo would love this!")
        if score > 3:
            scoreboard.game_over()
            screen.update()
            game_on = False

screen.exitonclick()
