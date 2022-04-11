from turtle import Turtle
import random
colors=["red","green","blue","yellow","black"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=10



class CarManager(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

        

    def make_car(self):
        #here we are using the concept of probability that in every 1 to 6 chance
        #when random choice is 1 we make car
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(colors))
            new_car.penup()
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            #car.setheading(180)
            #car.forward(STARTING_MOVE_DISTANCE)
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
        

