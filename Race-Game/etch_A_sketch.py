from turtle import Turtle,Screen

def move_forward():
    tim.forward(10)

def move_back():

    tim.backward(10)


def move_counterclockwise():
    tim.left(10)

    #ya da globale falan hiç girmezsin ve şunu kullanılırsın
    #new_heading=tim.heading()+10
    #tim.setheading(new_heading)
    #YA DA AMK SADECE LEFT RİGHT FONKS KULLANABİLRİDİN SALAK





def move_clockwise():
   tim.right(10)


def move_start_point():
    tim.reset()
    # ya da
    # tim.clear()
    # tim.penup()
    # tim.home()
    # tim.pendown()




tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_back,"s")
screen.onkey(move_clockwise,"d")
screen.onkey(move_counterclockwise,"a")
screen.onkey(move_start_point,"c")







screen.exitonclick()