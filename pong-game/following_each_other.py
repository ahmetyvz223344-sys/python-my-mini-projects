from turtle import Turtle




class Create_Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.width(20)
        self.x_step = 10
        self.y_step = 10
        self.move_speed=0.1


        self.penup()
        self.goto(0,0)
        self.pendown()

    def move_ball(self):


            self.penup()
            new_x = self.xcor()+self.x_step
            new_y = self.ycor()+self.y_step
            self.goto(new_x,new_y)

    def move(self):

        self.penup()
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)


