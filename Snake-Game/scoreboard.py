from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)

    def game_over(self):

        self.color("white")
        self.hideturtle()

        self.goto(0,0)


        self.write(f"Game Over!", align="center", font=("Courier", 40, "normal"))