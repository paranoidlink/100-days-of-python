from turtle import Turtle, Screen
import random as r


screen = Screen()
screen.setup(width = 500, height = 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def get_bet():
    user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")
    bet_validator(user_bet)
    return user_bet


def bet_validator(bet):
    for color in colors:
        if color == bet.lower():
            return True
    print("Please select a valid color from the turtles you see on screen")
    get_bet()

def turtle_builder(y_pos, col):
    tim = Turtle(shape = "turtle")
    tim.color(col)
    tim.penup()
    tim.teleport(x= -240, y= y_pos)
    return tim

def setup():
    y_pos = 150
    turtles = []
    for color in colors:
        turtle = turtle_builder(y_pos, color)
        turtles.append([turtle, color])
        y_pos = y_pos - 50
    return turtles

def bet_check(bet, winner):
    if bet == winner:
        print(f"Congralations {winner} won you bet correctly")
    else:
        print(f"{winner} Wins! unfortunately your bet of {bet} was incrorect")

def winner_finder(turtle, bet):
    x = turtle[0].xcor()
    if x >= 230:
        winner = turtle[1]
        bet_check(bet, winner)
        return True
    else:
        return False

def race():
    turtle_list = setup()
    bet = get_bet()
    raceover = False
    while not raceover:
        for turtle in turtle_list:
            turtle[0].forward(r.randint(0,10))
            raceover = winner_finder(turtle, bet)
            if raceover:
                break

race()



screen.exitonclick()