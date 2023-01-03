from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("gray20")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_wall()

    # Detect collision with a paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 335 and ball.x_move > 0 \
            or ball.distance(l_paddle) < 50 and ball.xcor() < 335 and ball.x_move < 0:
        ball.hit_paddle()

    # Detect if ball gets passed the paddle
    if ball.xcor() > 400:
        scoreboard.increase_score("left")
        ball.reset_position()
    if ball.xcor() < -400:
        scoreboard.increase_score("right")
        ball.reset_position()

screen.exitonclick()
