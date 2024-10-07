import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SCREEN = Screen()
SCREEN.setup(width=600, height=600)
SCREEN.tracer(0)

player = Player('turtle')
scoreboard = Scoreboard()
car_manager = CarManager(player, scoreboard)

game_is_on = True

def main():
    while game_is_on:
        time.sleep(0.1)
        if random.randint(1, 6) == 1:
            car_manager.generate_new_car()

        # Start the magic
        car_manager.move_car()
        car_manager.handle_next_level()
        car_manager.handle_movements()

        SCREEN.update()

    SCREEN.exitonclick()

if __name__ == '__main__':
    main()