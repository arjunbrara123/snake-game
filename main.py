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

# Initialise user game components
snake = Snake(col="white")  # Player snake
pizza = Food(screen_size)

# # Initialise computer game components
# basilisk = Snake(col="red")  #Enemy (Computer) snake
# basilisk.jump_down()
# basilisk.jump_down()
# basilisk.move(screen_size)

# Set keyboard game controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def debugger():
    scoreboard.debug_mode()
    snake.debug()

screen.onkey(debugger, "d")


# Give the user a key to quit the game
def esc_game():  screen.bye()


screen.onkey(esc_game, "Escape")

# Start the game running
game_on = True
hunger = 0

while game_on:
    hunger += 1
    screen.update()
    time.sleep(0.1)
    snake.move(screen_size)
    if hunger > 100:
        pizza.refresh(screen_size)
        hunger = 0

    #basilisk.move(screen_size)

    # Detect collision with self
    for segment in range(len(snake.nagini) - 3):
        donatello = snake.nagini[segment]
        if snake.head.distance(donatello) < 10:
            print(f"Head: {snake.head.position()} - Segment {segment+1}: {donatello.position()}")
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
