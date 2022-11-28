from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 70, 'bold')

class PongScreen(Turtle):
  def __init__(self):
    super().__init__()
    self.player1_score = 0
    self.player2_score = 0
    self.draw()


  def draw(self):
    """Draws the center line and scores"""
    self.ht()
    self.penup()
    self.goto(0.00,-300.00)
    self.setheading(90)
    self.color("white")
    
    while self.ycor() < 300.00:
      self.pendown()
      self.forward(20)
      self.penup()
      self.forward(7)
      
    self.goto(-50,200)
    self.write(f"{self.player1_score}",False,align=ALIGNMENT,font=FONT)
    self.goto(50,200)
    self.write(f"{self.player2_score}",False,align=ALIGNMENT,font=FONT)
  
  def update_player1_score(self):
    """Updates the score of player 1"""
    self.player1_score += 1
    self.clear()
    self.draw()
    
  def update_player2_score(self):
    """Updates the score of player 2"""
    self.player2_score += 1
    self.clear()
    self.draw()      
    