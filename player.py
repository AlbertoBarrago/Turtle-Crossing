from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
   def __init__(self, shape):
       super().__init__()
       self.penup()
       self.color('black')
       self.shape(shape)
       self.setheading(90)
       self.goto(STARTING_POSITION)
       self.setup_control()

   def move(self):
       """
       Move the player forward.
       :return:
       """
       new_y = self.ycor() + MOVE_DISTANCE
       if new_y < FINISH_LINE_Y:
           self.goto(self.xcor(), new_y)

   def setup_control(self):
       """
       Setup control for movement up
       :return:
       """
       self.screen.onkey(key='Up', fun=self.move)
       self.screen.listen()

