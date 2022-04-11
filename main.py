from turtle import Screen
import time
from player import Player
from car import CarManager
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

scoreboard=Scoreboard()


is_game_on=True
turtle=Player()

screen.listen()
screen.onkey(turtle.move_up,"Up")

car=CarManager()


while is_game_on:
    time.sleep(0.1)
    screen.update()

    car.make_car()
    car.move_car()

 #TO DETECT THE COLLISION BETWEEN THE CAR AND THE TURTLE
    for object in car.all_cars:
        if object.distance(turtle)<20:
            is_game_on=False
            scoreboard.game_over()
    
    #TO DETECT THE TURTLE REACHING THE FINISH LINE
    if turtle.is_at_finish_line():
        turtle.starting_position()
        scoreboard.increase_level()
        car.level_up()
   






screen.exitonclick()
    