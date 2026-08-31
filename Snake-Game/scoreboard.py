from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as file:
            self.highscore=int(file.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280, 280)


    # def game_over(self):
    #
    #     self.color("white")
    #     self.hideturtle()
    #
    #     self.goto(0,0)
    #
    #
    #     self.write(f"Game Over!", align="center", font=("Courier", 40, "normal"))
    #


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")




        self.score = 0

    def current_score(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-200,200)

        self.write(f"Score: {self.score}                                                                Highest score:{self.highscore}", font=("Arial", 12, "normal"))



