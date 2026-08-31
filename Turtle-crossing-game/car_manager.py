from random import choice,randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_speed=STARTING_MOVE_DISTANCE


        self.all_cars=[]







    def create_car(self):
        random_chance=randint(0,6)
        if random_chance==1:


            new_car=Turtle("square")
            new_car.shapesize(1,2)
            new_car.color(choice(COLORS))
            new_car.penup()
            y_axis=randint(-250,250)
            new_car.goto(310,y_axis)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=5
