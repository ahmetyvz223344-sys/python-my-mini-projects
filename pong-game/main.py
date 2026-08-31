
from turtle import Turtle, Screen
from following_each_other import Create_Ball
import time
from scoreboard import GameScore

screen = Screen()
screen.setup(width=900,height=600)
screen.bgcolor("black")
screen.title("My pong Game")

screen.tracer(0)


class Screen_Dots(  Turtle ):

    def __init__(self):
        super().__init__()
        for square in range(-280, 305, 25):
            dots = Turtle("square")
            dots.color("white")
            dots.turtlesize(0.5,0.3)

            dots.penup()
            dots.goto(0, square)
            dots.pendown()




screen_dots=Screen_Dots()



class Paddle:
    def __init__(self):
        self.player_turtle = []

    def create_turtle(self):
        position = [(-440, 0), (430, 0)]

        for square in position:
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.color("white")

            turtle.shapesize(stretch_wid=5, stretch_len=1)

            turtle.goto(square)
            turtle.pendown()
            self.player_turtle.append(turtle)



    def up(self):


            self.player_turtle[0].penup()
            y_cor=self.player_turtle[0].ycor()
            y_cor+=20
            self.player_turtle[0].sety(y_cor)



    def up1(self):


            self.player_turtle[1].penup()
            y_cor=self.player_turtle[1].ycor()
            y_cor+=20
            self.player_turtle[1].sety(y_cor)


    def down(self):



            self.player_turtle[0].penup()
            y_cor=self.player_turtle[0].ycor()
            y_cor-=20
            self.player_turtle[0].sety(y_cor)




    def down1(self):

            self.player_turtle[1].penup()
            y_cor=self.player_turtle[1].ycor()
            y_cor-=20
            self.player_turtle[1].sety(y_cor)





ball=Create_Ball()


move= Paddle()
move.create_turtle()

screen.listen()
screen.onkeypress(move.up,"w")
screen.onkey(move.up1,"Up")
screen.onkey(move.down,"s")
screen.onkey(move.down1 ,"Down")




scores_position = [(400, 250), (-400, 250)]

player1_score = GameScore(scores_position[0])

player2_score = GameScore(scores_position[1])

game_is_on=True
while game_is_on:


    screen.update()
    time.sleep(ball.move_speed)

    ball.move_ball()
    if ball.ycor()>280 or   ball.ycor()<-280:
        ball.y_step*=-1

#ŞURADA YAPTIĞIMIZ ŞEY ÇOK MANTIKLI ÇÜNKÜ FARKLI METODLARA BİLE GİRMEDEN
# TEK YAPTIĞIMIZ İÇERİDEKİ ÖZELLİĞİN BİRİNİ İŞİMİZE GELDİĞİ GİBİ DEĞİŞTİRMEK

    if ball.distance(move.player_turtle[0])<50 and ball.xcor()<-420 or ball.distance(move.player_turtle[1])<50 and ball.xcor()>420:
        ball.x_step*=-1
        ball.move_speed*=0.9




    if ball.xcor()>450:
        ball.goto(0,0)

        ball.x_step*=-1
        player2_score.score+=1
        player2_score.clear()
        player2_score.write(f"Score: {player2_score.score}", align="center", font=("Courier", 12, "normal"))
        ball.move_speed = 0.1



    if ball.xcor()<-450:
        ball.goto(0,0)

        player1_score.score+=1
        player1_score.clear()
        player1_score.write(f"Score: {player1_score.score}", align="center", font=("Courier", 12, "normal"))
        ball.x_step*=-1
        ball.move_speed = 0.1





screen.exitonclick()
