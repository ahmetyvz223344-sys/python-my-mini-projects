from turtle import Turtle
from random import randint
up=90
down=270
right=0
left=180

move_distance=20
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.position=[(0,0),(-20,0),(-40,0)]
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        self.distance=[]


    def create_snake(self):
        for position in self.position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def add_segment(self):
        self.segment=Turtle("square")
        self.segment.color("white")

        self.segment.penup()


        self.segments.append(self.segment)





    def extend(self):
        self.x_cor = self.segments[len(self.segments) - 2].xcor()
        self.y_cor = self.segments[len(self.segments) - 2].ycor()
        self.segments[len(self.segments) - 1].goto(self.x_cor,self.y_cor)





    def move(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x = self.segments[seg_num-1].xcor()
                new_y = self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.head.forward(move_distance)


    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)


    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:

            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)





    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

        self.move()
