from turtle import Turtle
from random import choice

Y_CORS = [y for y in range(-220, 241, 20)]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_distance = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.car_list = []

    def create_car(self):
        car = Turtle()
        car.color(choice(COLORS))
        car.shape('square')
        car.shapesize(stretch_wid=0.9, stretch_len=2)
        car.penup()
        car.goto(x=-400, y=choice(Y_CORS))
        self.car_list.append(car)

    def move_and_collision(self, player):
        for car in self.car_list:
            car.goto(x=(car.xcor() + self.move_distance), y=car.ycor())
            if car.xcor() > 350:
                car.goto(x=1000, y=0)
                self.car_list.remove(car)
            car_xs, car_ys = range(car.xcor() - 30, car.xcor() + 30), range(car.ycor() - 20, car.ycor() + 20)
            if player.xcor() in car_xs and player.ycor() in car_ys:
                return True

    def clear_cars(self):
        [car.goto(x=1000, y=0) for car in self.car_list if car.xcor() in range(-300, 300) and car.ycor() in range(-60, 80)]

    def reset_car_manager(self):
        [car.goto(x=1000, y=0) for car in self.car_list]
        self.car_list = []
        self.clear()
        self.move_distance = STARTING_MOVE_DISTANCE

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT
