def turn_right():
    turn_left()
    turn_left()
    turn_left()

def movement():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()

while not at_goal():
    movement()