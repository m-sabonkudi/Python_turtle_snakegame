
from turtle import Turtle
START_POSS = [(0, 0), (0,-20), (0, -40)]
class Snake:

    def __init__(self):
        self.segments = []
        self.create_object()

    def create_object(self):
        for i in START_POSS:
            self.add_segment(i)

    def add_segment(self, pos):
        obj = Turtle("square")
        obj.penup()
        obj.speed("slowest")
        obj.color("white")
        obj.goto(pos)
        self.segments.append(obj)

    def reset(self):
        for i in self.segments:
            i.goto(1000, 1000)
        self.segments.clear()
        self.create_object()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i-1].pos())
        self.segments[0].forward(20)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def collision_with_wall(self):
        outcome = True
        if self.segments[0].xcor() > 280 or self  .segments[0].xcor() < -280 or self.segments[0].ycor() > 280 or self.segments[0].ycor() < -280:
            outcome = False
        return outcome

    def collision_with_tail(self):
        outcome = True
        for seg in self.segments[1:]:
            if self.segments[0].distance(seg) < 10:
                outcome = False
        return outcome






