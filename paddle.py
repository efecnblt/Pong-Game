from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(position_x, position_y)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)
    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)