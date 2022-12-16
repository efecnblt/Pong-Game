from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("GAME")
ball = Ball()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

scoreboard_for_r = Scoreboard(-50, 220)
scoreboard_for_l = Scoreboard(50, 220)
scoreboard_for_l.middle_cross()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and (ball.xcor() > 320 or ball.xcor() < -320):
        ball.bounce_x()

    #for r paddle
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard_for_r.increase_score()

    #for l paddle
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard_for_l.increase_score()

screen.exitonclick()

