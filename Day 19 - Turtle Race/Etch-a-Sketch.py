from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()

def move_fowards():
    pen.forward(10)

def move_backwards():
    pen.back(10)

def turn_right():
    pen.right(10)

def turn_left():
    pen.left(10)

def clear():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

screen.listen()
screen.onkeypress(key="w", fun= move_fowards)
screen.onkeypress(key="s", fun= move_backwards)
screen.onkeypress(key="a", fun= turn_left)
screen.onkeypress(key="d", fun= turn_right)
screen.onkeypress(key="c", fun=clear)


screen.exitonclick()