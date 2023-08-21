from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True

    def reset_player(self):
        self.goto(STARTING_POSITION)