import time
from turtle import Screen



from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move_turtle,"w")
for i in range(0,10):
    last_time = time.time()
game_is_on = True

scoreboard=Scoreboard()
car_manager = CarManager()

while game_is_on:
    time.sleep(0.1)
    scoreboard.goto(225,225)
    scoreboard.write(f"level:{scoreboard.level}",align="center",font=("Verdana",12,"bold"))
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player)<20:

            scoreboard.lose()
            game_is_on = False



    if player.ycor()>280:
        scoreboard.level+=1
        scoreboard.clear()
        scoreboard.goto(0,0)
        player.goto(0,-280)
        car_manager.level_up()

    screen.update()

screen.exitonclick()
