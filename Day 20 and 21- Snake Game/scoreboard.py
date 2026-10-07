from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Futura", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.teleport(0, 270)
        self.display()


    def eat(self):
        self.score = self.score + 1
        self.clear()
        self.display()

    def display(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)