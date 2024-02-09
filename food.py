import random
from turtle import Turtle
from snake import Snake

class Food(Turtle ):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh_location()

    def refresh_location(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
