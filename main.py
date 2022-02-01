from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)


player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
score = Score()




screen.listen()
screen.onkey(player1.go_up, "Up")
screen.onkey(player1.go_down, "Down")

screen.onkey(player2.go_up, "w")
screen.onkey(player2.go_down, "s")


is_on = True
while is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(player1) < 55:
        ball.bounce_x()
        score.increase_score_of_player1()

    if ball.xcor() < -320 and ball.distance(player2) < 55:
        ball.bounce_x()
        score.increase_score_of_player2()

    if ball.xcor() > 380:
        ball.refresh()
        score.increase_score_of_player2()

    if ball.xcor() < -380:
        ball.refresh()
        score.increase_score_of_player1()



screen.exitonclick()