from turtle import Screen
from screen import PongScreen
from players import Player
from ball import Ball
import time

#setting up screen
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")
pong = PongScreen()

#setting up players
player_1 = Player((-350,0))
player_2 = Player((350,0))


#creating the ball
ball = Ball()

#setting up condition for the game
game_is_on = True

#moving players
screen.listen()

screen.onkey(player_1.move_up,"w")
screen.onkey(player_1.move_down,"s")

screen.onkey(player_2.move_up,"Up")
screen.onkey(player_2.move_down,"Down")


#game in progress
while game_is_on:
  time.sleep(0.01)  
  screen.update()
  ball.move()

  #detect collision with x and -x
  if ball.ycor() > 295 or ball.ycor() < -293:
    ball.bounce_y()
  
  #detect collision with right paddle  
  if ball.distance(player_2) < 50 and ball.xcor() > 340 or ball.distance(player_1) < 50 and ball.xcor() < -340:
    ball.bounce_x()
  
  #detect collision with right and left borders and update score
  #reset position of the ball  
  if ball.xcor() > 380:
    pong.update_player1_score()
    ball.reset_position()
  if ball.xcor() < -380:
    pong.update_player2_score()
    ball.reset_position()

screen.exitonclick()
 