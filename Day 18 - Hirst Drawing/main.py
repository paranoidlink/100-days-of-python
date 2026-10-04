import turtle as t
import random as r

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t.colormode(255)
pen = t.Turtle()
pen.speed(0)
pen.hideturtle()

def Hirst(grid_size, spacing):
    start_point = ((grid_size - 1) * spacing) / 2
    pen.teleport(x=-start_point, y=-start_point)
    for row in range(grid_size):
        for column in range(grid_size):
            pen.color(r.choice(color_list))
            pen.dot(20)
            pen.penup()
            pen.forward(spacing)
            pen.pendown()
        pen.penup()
        pen.setx(-start_point)
        current_y = pen.pos()
        pen.sety(current_y[1] + spacing)
        pen.pendown()

Hirst(10, 50)

screen = t.Screen()
screen.exitonclick()
