from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level=1
        self.goto(0,0)

    def lose(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Verdana",20 ,"bold"))