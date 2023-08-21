import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from random import randint
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.up, 'Up')

car_manager = CarManager()
scoreboard = Scoreboard()


def game():
    car_creation_factor = 90
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        if randint(0, 100) > car_creation_factor:
            car_manager.create_car()
        collision = car_manager.move_and_collision(player)
        if collision:
            car_manager.clear_cars()
            screen.update()
            scoreboard.display_game_over_message()
            break
        if player.finish():
            player.reset_player()
            scoreboard.display_level()
            car_creation_factor -= 5
            car_manager.speed_up()
            time.sleep(1)
        screen.update()


def restart_game():
    car_manager.reset_car_manager()
    player.reset_player()
    scoreboard.reset_score_board()
    game()


[screen.onkeypress(restart_game, key) for key in ['R', 'r']]
game()
screen.exitonclick()
