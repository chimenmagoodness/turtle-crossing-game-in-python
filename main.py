import time
from turtle import Screen, ycor
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()

    # Detect the collision of the car
    for car_ in car.all_cars:
        if car_.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect a successful crossing
    if player.is_at_finish_line():
        player.back_to_start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()