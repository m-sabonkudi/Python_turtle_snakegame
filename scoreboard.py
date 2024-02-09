from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(270)
        self.setx(0)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", move=False, align="center", font=("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as t_file:
                t_file.write(str(self.high_score))
        self.score = 0
        self.write_score()





