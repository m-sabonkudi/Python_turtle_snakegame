import turtle, random, time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
my_screen = turtle.Screen()
my_screen.bgcolor("black")
my_screen.title("SNAKE GAME")
my_screen.tracer(0)
my_screen.setup(height=600, width=600)

sniik = Snake()
fodi = Food()
scoreb = ScoreBoard()

my_screen.listen()
my_screen.onkey(sniik.left, "Left")
my_screen.onkey(sniik.right, "Right")
my_screen.onkey(sniik.up, "Up")
my_screen.onkey(sniik.down, "Down")




game_on = True
while game_on:
    my_screen.update()
    time.sleep(0.1)
    sniik.move()


    if sniik.segments[0].distance(fodi) < 15:
        fodi.refresh_location()
        sniik.extend()
        scoreb.increase_score()

    if not sniik.collision_with_wall() or not sniik.collision_with_tail():
        scoreb.reset()
        sniik.reset()







my_screen.exitonclick()





