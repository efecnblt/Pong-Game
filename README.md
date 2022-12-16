# Pong-Game
Simple Pong Game in Python

*This is simple Pong Game implemented in python. There are 4 .py files in the file. These are respectively;*  

**ball.py:** It is the file that provides the creation, movement and direction of the ball in motion.    

**paddle.py:** It creates a pedal in that region with the coordinates sent via ***main.py***. It contains 2 functions. these functions are **`go_up`** and **`go_down`**. These allow us to move the pedals up and down.    

**scoreboard.py:** It creates a scoreboard that will display the score of 2 players at the top of the screen. A point is awarded to the opponent of the user who missed the ball. The **`middle_cross`** function creates dashed lines that divide the screen in half. *(optional)*    

**main.py:** It is our main file. We create 2 pedals by sending the coordinates of each one, right and left. İf the ball passes the pedal, we increase the score and take the ball back to the middle position. The **`ball.bounce_x()`** function causes the ball to bounce back and change direction when it hits the pedal.  

*This game starts with the ball thrown from the middle to the corner and the users send this ball across with the pedals they control. If the user misses the ball, the score is written to the opposite side and the ball moves again.*

![pong_game](https://github.com/efecnblt/Basics-Games-with-Python/blob/main/Pong%20Game/pong_game.gif?raw=true)
