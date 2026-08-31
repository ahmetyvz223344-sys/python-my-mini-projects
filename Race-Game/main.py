from turtle import Turtle,Screen
from random import randint


screen = Screen()
screen.setup(width=500,height=400)

user_bet=screen.textinput(title="who win",prompt="Which turtle will win the race? Enter a color:")
colors=["red","yellow","green","blue","purple","orange"]
y_post=[-80,-40,0,40,80,120]

all_turtles=[]

for i in range(0,6):

    new_turtle=Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_post[i])
    all_turtles.append(new_turtle)

is_race_on=False

if user_bet:
    is_race_on=True

while is_race_on:
    step = randint(0, 5)
    which_turtle=randint(0,5)
    all_turtles[which_turtle].forward(step)
    for turtle in all_turtles:
        if turtle.xcor()>=230:

            cizgi,dolgu=turtle.color()
            #YA DA
            #winner_color==turtle.pencolor()




            if user_bet==cizgi:
                print("You win!")

            else:
                print(f"You lose!,the winner is {cizgi} turtle")


            is_race_on=False

