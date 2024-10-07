import random
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player('turtle')
scoreboard = Scoreboard()
car_manager = CarManager(player, scoreboard)

game_is_on = True

def main():
    while game_is_on:
        time.sleep(0.1)
        if random.randint(1, 6) == 1:
            car_manager.generate_new_car()

        car_manager.move_car()

        car_manager.handle_next_level()

        car_manager.handle_movements()

        screen.update()

if __name__ == '__main__':
    main()