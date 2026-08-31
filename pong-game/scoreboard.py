from turtle import Turtle


class GameScore(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0

        self.goto(position)

        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))
        self.hideturtle()