from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

game_active = True

screen.onkey(lambda: snake.turn("w"), "w")
screen.onkey(lambda: snake.turn("s"), "s")
screen.onkey(lambda: snake.turn("a"), "a")
screen.onkey(lambda: snake.turn("d"), "d")

while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.eat()
        snake.grow()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_active = False
        scoreboard.game_over()


    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_active = False
            scoreboard.game_over()














screen.exitonclick()