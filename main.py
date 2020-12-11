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

# Initialise game components
snake = Snake()  # Player snake
# basilisk = Snake()  #Enemy (Computer) snake
pizza = Food(screen_size)

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
hunger = 0

while game_on:
    hunger += 1
    screen.update()
    time.sleep(0.05)
    snake.move(screen_size)
    if hunger > 80:
        pizza.refresh(screen_size)
        hunger = 0

    # basilisk.move(screen_size)

    # Detect collision with self
    for donatello in range(len(snake.nagini) - 1):
        donatello = snake.nagini[donatello]
        if snake.head.distance(donatello) < 10:
            scoreboard.game_over()
            game_on = False

    # Detect collision with food
    if snake.head.distance(pizza) <= 15:
        pizza.refresh(screen_size)
        score += 1
        scoreboard.refresh(score, screen_size)
        snake.grow()
        hunger = 0

screen.exitonclick()
