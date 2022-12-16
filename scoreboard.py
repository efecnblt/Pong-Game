from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Hobo Std", 36, "normal")

class Scoreboard(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.score = 0
        self.mid_pos = -250
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position_x, position_y)
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def middle_cross(self):
        for i in range(9):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color('#edf2f4')
            new_turtle.penup()
            new_turtle.shapesize(stretch_len=0.5, stretch_wid=1.5)
            new_turtle.goto(0, self.mid_pos)
            self.mid_pos += 60
    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)