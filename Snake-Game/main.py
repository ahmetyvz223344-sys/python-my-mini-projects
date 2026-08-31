from turtle import Screen
import time

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)



# YA DA



snake=Snake()
food=Food()




screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

scoreboard = Scoreboard()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



    if snake.head.distance(food) < 15:
        scoreboard.score+=1
        scoreboard.clear()
        scoreboard.write(f"current score is:{scoreboard.score}", align="left", font=("Courier", 12, "normal"))
        snake.add_segment()
        snake.extend()
        food.refresh()



    if  snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        game_is_on=False
        scoreboard.game_over()


    for segment in snake.segments[1:]:

        # Aslında buradan anlayacağımız bir listenin belli bi
        # bölümünü kullanmak istyorsak o zaman slicing yapmak mantıklı baya

        if snake.head.distance(segment)<10:

            game_is_on=False
            scoreboard.game_over()




















screen.exitonclick()

