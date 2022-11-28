from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape("circle")
    self.color("white")
    self.x_move = 4
    self.y_move = 3
  
  
  def move(self):
    x = self.xcor() + self.x_move
    y = self.ycor() + self.y_move
    self.setpos(x,y)
    
  def bounce_y(self):
    self.y_move *= -1
  
  def bounce_x(self):
    self.x_move *= -1
  
  def reset_position(self):
    self.home()
    self.x_move = 4    
    self.y_move = 3    