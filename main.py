import time
from turtle import *


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

paddle = Turtle("square")
paddle.color("white")
paddle.penup()
paddle.goto(-380, 0)
screen.update()

























screen.exitonclick()