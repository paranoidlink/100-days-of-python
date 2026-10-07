from turtle import Turtle
AMOUNT = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_SPEED = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(AMOUNT):
            self.add_segment()


    def add_segment(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        try:
            if self.segments[-1].position() == self.segments[0].position():
                turtle.goto(x = self.segments[0].xcor() - 20, y=0)
            else:
                turtle.goto(self.segments[-1].position())
        except (IndexError, TypeError):
            turtle.teleport(0,0)
        self.segments.append(turtle)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].teleport(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def turn(self, dir):
        match dir:
            case "w":
                if self.head.heading() != DOWN:
                    self.head.setheading(UP)
            case "s":
                if self.head.heading() != UP:
                    self.head.setheading(DOWN)
            case "a":
                if self.head.heading() != RIGHT:
                    self.head.setheading(LEFT)
            case "d":
                if self.head.heading() != LEFT:
                    self.head.setheading(RIGHT)

    def grow(self):
        self.add_segment()

        #x= self.segments[-1].xcor() - 20, y=0