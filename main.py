import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    if player.ycor() == FINISH_LINE_Y:
        player.start()
        # level up
        score.refresh()
        car.level_up()
    for c in car.all_cars:
        if c.distance(player) < 22:
            score.game_over()
            game_is_on = False

screen.exitonclick()
