from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_RESTART = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.display_level()

    def display_level(self):
        self.goto(x=-300, y=240)
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def display_game_over_message(self):
        self.goto(x=0, y=20)
        self.write(f"GAME OVER", align='center', font=FONT)
        self.goto(x=0, y=-20)
        self.write(f"Press R to restart or click anywhere to quit", align='center', font=FONT_RESTART)

    def reset_score_board(self):
        self.level = 0
        self.clear()
        self.display_level()
